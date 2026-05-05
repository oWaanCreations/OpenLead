"""
WhatsApp Filter — Validates which leads have WhatsApp accounts.
Adapted from private whatsapp_checker.py with rich CLI and browser picker.
"""

import asyncio
import re
import os
import csv
from pathlib import Path
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeoutError

# ─── Constants ───────────────────────────────────────────────────────────────
NO_RESULT_TEXTS = [
    "No results found",
    "No chats, contacts or messages found",
    "No chats, contacts, or messages found",
]

SEARCH_BOX_SELECTORS = [
    'div[aria-label="Search name or number"][contenteditable="true"]',
    'div[title="Search name or number"][contenteditable="true"]',
    'div[aria-placeholder="Search name or number"][contenteditable="true"]',
    'div[contenteditable="true"][role="textbox"]',
    'input[placeholder="Search name or number"]',
]

NEW_CHAT_SELECTORS = [
    'button[title="New chat"]',
    '[aria-label="New chat"]',
    '[data-testid="new-chat-btn"]',
    'span[data-icon="new-chat-outline"]',
]

PROFILE_DIR = str(Path("profiles/whatsapp").resolve())
os.makedirs(PROFILE_DIR, exist_ok=True)


# ─── Helpers ─────────────────────────────────────────────────────────────────
def clean_phone(phone: str) -> str:
    digits = re.sub(r"\D", "", phone)
    return f"+{digits}" if digits else ""


def digits_only(value: str) -> str:
    return re.sub(r"\D", "", value or "")


def short_name(name: str, max_len=32):
    name = " ".join((name or "").split())
    return name if len(name) <= max_len else name[: max_len - 1] + "\u2026"


async def first_visible_locator(page, selectors, timeout_each=700):
    for sel in selectors:
        loc = page.locator(sel).first
        try:
            await loc.wait_for(state="visible", timeout=timeout_each)
            return loc
        except Exception:
            continue
    return None


async def get_search_box(page):
    """Return the New Chat drawer search box."""
    candidates = page.locator('div[contenteditable="true"][role="textbox"], input[placeholder="Search name or number"]')
    count = await candidates.count()
    for i in range(count):
        loc = candidates.nth(i)
        try:
            if not await loc.is_visible(timeout=250):
                continue
            label = (await loc.get_attribute("aria-label")) or ""
            title = (await loc.get_attribute("title")) or ""
            placeholder = (await loc.get_attribute("placeholder")) or ""
            aria_placeholder = (await loc.get_attribute("aria-placeholder")) or ""
            text = " ".join([label, title, placeholder, aria_placeholder]).lower()
            if "search name or number" in text:
                return loc
        except Exception:
            continue
    return await first_visible_locator(page, SEARCH_BOX_SELECTORS, timeout_each=300)


async def click_new_chat_button(page):
    """Click the enabled parent button for New Chat."""
    icon = page.locator('span[data-icon="new-chat-outline"]').first
    try:
        if await icon.is_visible(timeout=700):
            handle = await icon.element_handle()
            parent = await page.evaluate_handle(
                'el => el.closest(\'button, div[role="button"], [aria-label="New chat"], [title="New chat"]\')',
                handle,
            )
            parent_el = parent.as_element()
            if parent_el:
                await parent_el.click(force=True)
                return
    except Exception:
        pass

    for sel in NEW_CHAT_SELECTORS:
        loc = page.locator(sel).first
        try:
            if await loc.is_visible(timeout=700):
                await loc.click(force=True)
                return
        except Exception:
            continue
    raise RuntimeError("New Chat button not found.")


async def open_new_chat_panel(page, force_reopen=False):
    """Open New Chat drawer and return search box locator."""
    if not force_reopen:
        existing = await get_search_box(page)
        if existing:
            return existing
    await click_new_chat_button(page)
    await asyncio.sleep(0.8)
    search = await get_search_box(page)
    if not search:
        raise RuntimeError("Search box not found after opening New Chat panel.")
    return search


async def paste_number_into_active_box(page, phone: str):
    """Paste number into the active WhatsApp search box."""
    await page.keyboard.press("Control+A")
    await asyncio.sleep(0.05)
    try:
        await page.evaluate("value => navigator.clipboard.writeText(value)", phone)
        await page.keyboard.press("Control+V")
    except Exception:
        await page.keyboard.insert_text(phone)
    await asyncio.sleep(0.25)


async def read_active_search_value(page):
    """Read the currently focused WhatsApp search box text."""
    try:
        return await page.evaluate(
            """() => {
                const el = document.activeElement;
                if (!el) return '';
                return ('value' in el ? el.value : el.textContent || '').trim();
            }"""
        )
    except Exception:
        return ""


async def classify_current_result_fast(page, phone: str):
    """Wait until WhatsApp shows either no-result text or a profile/result row."""
    target_digits = digits_only(phone)
    no_result_for_number = f"No results found for '{phone}'"

    for _ in range(200):  # max ~20 seconds
        active_value = await read_active_search_value(page)
        active_digits = digits_only(active_value)
        if active_digits != target_digits:
            await asyncio.sleep(0.1)
            continue

        body_text = await page.evaluate("document.body.innerText || ''")
        lowered = body_text.lower()

        if no_result_for_number.lower() in lowered:
            return "Invalid", no_result_for_number

        for text in NO_RESULT_TEXTS:
            if text.lower() in lowered:
                return "Invalid", text

        if target_digits and target_digits in digits_only(body_text) and "no results found" not in lowered:
            return "Valid", "Number/contact appeared in results"

        try:
            rows = page.locator(
                '#app div[role="gridcell"] >> visible=true, '
                '#app [data-testid="cell-frame-container"] >> visible=true, '
                '#app div[role="listitem"] >> visible=true'
            )
            count = await rows.count()
            if count > 0 and "no results found" not in lowered:
                return "Valid", f"Profile/result appeared ({count} visible row(s))"
        except Exception:
            pass

        await asyncio.sleep(0.1)

    return "Unknown", "Timed out waiting for No Result or profile"


# ─── Browser Picker ──────────────────────────────────────────────────────────
def pick_browser(console):
    """Ask user which browser to use for WhatsApp Web."""
    console.print()
    console.print("[bold cyan]Choose Browser for WhatsApp Web:[/bold cyan]")
    console.print("  [1] Playwright Chromium (bundled, recommended)")
    console.print("  [2] Google Chrome")
    console.print("  [3] Microsoft Edge")
    console.print("  [4] Opera")
    console.print("  [5] Custom path")
    console.print()
    
    choice = console.input("[bold cyan]Enter choice [1-5, default: 1]:[/bold cyan] ").strip() or "1"
    
    paths = {
        "1": None,  # Use bundled chromium
        "2": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        "3": r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        "4": r"C:\Users\%USERNAME%\AppData\Local\Programs\Opera\opera.exe",
    }
    
    if choice == "5":
        custom = console.input("[bold cyan]Enter full path to browser executable:[/bold cyan] ").strip()
        return custom, True
    
    exe_path = paths.get(choice)
    use_bundled = exe_path is None
    
    if exe_path and not os.path.exists(exe_path):
        console.print(f"[yellow]\u26a0\ufe0f  Browser not found at {exe_path}, falling back to bundled Chromium.[/yellow]")
        return None, True
    
    return exe_path, use_bundled


# ─── Main Filter Function ────────────────────────────────────────────────────
async def filter_whatsapp_leads(leads, console):
    """
    Filter leads through WhatsApp Web to find valid WhatsApp numbers.
    
    Args:
        leads: List of lead dicts from scraper
        console: Rich Console instance
    
    Returns:
        List of leads that have WhatsApp
    """
    if not leads:
        return []
    
    exe_path, use_bundled = pick_browser(console)
    
    valid_leads = []
    invalid_count = 0
    unknown_count = 0
    
    console.print()
    console.print("[bold blue]\U0001f310 Opening WhatsApp Web...[/bold blue]")
    
    async with async_playwright() as p:
        if use_bundled:
            context = await p.chromium.launch_persistent_context(
                user_data_dir=PROFILE_DIR,
                headless=False,
                viewport={"width": 1366, "height": 850},
                args=[
                    "--disable-blink-features=AutomationControlled",
                    "--no-first-run",
                    "--no-default-browser-check",
                ],
            )
        else:
            context = await p.chromium.launch_persistent_context(
                user_data_dir=PROFILE_DIR,
                executable_path=exe_path,
                headless=False,
                viewport={"width": 1366, "height": 850},
                args=[
                    "--disable-blink-features=AutomationControlled",
                    "--no-first-run",
                    "--no-default-browser-check",
                ],
            )
        
        page = context.pages[0] if context.pages else await context.new_page()
        
        await page.goto("https://web.whatsapp.com/", wait_until="domcontentloaded", timeout=0)
        
        console.print("[bold blue]\U0001f510 Waiting for login (scan QR if needed)...[/bold blue]")
        try:
            await page.wait_for_selector("#pane-side", timeout=120_000)
        except PlaywrightTimeoutError:
            console.print("[bold red]\u274c Login timeout. Scan QR code and run again.[/bold red]")
            await context.close()
            return []
        
        console.print("[bold green]\u2705 Logged in![/bold green]")
        console.print("[bold blue]\U0001f4ac Opening New Chat panel...[/bold blue]")
        
        try:
            await open_new_chat_panel(page)
        except Exception as e:
            console.print(f"[bold red]\u274c Could not open New Chat panel: {e}[/bold red]")
            await context.close()
            return []
        
        console.print(f"[bold green]\u2705 Ready. Checking {len(leads)} leads...[/bold green]\n")
        
        from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn
        
        progress = Progress(
            SpinnerColumn(style="green"),
            TextColumn("[bold]{task.description}"),
            BarColumn(bar_width=30, complete_style="green", finished_style="bright_green"),
            TaskProgressColumn(),
            console=console,
        )
        
        with progress:
            task = progress.add_task("[green]Filtering WhatsApp...[/green]", total=len(leads))
            
            for idx, lead in enumerate(leads, 1):
                company = lead.get("company_name", "Unknown")
                phone = clean_phone(lead.get("phone", ""))
                
                if not phone:
                    progress.update(task, advance=1)
                    continue
                
                progress.update(task, description=f"[green]{idx}/{len(leads)}[/green] [cyan]{short_name(company)}[/cyan] [dim]{phone}[/dim]")
                
                try:
                    await paste_number_into_active_box(page, phone)
                    status, reason = await classify_current_result_fast(page, phone)
                except Exception as e:
                    status, reason = "Unknown", f"Error: {e}"
                
                if status == "Valid":
                    lead["whatsapp_status"] = "Valid"
                    lead["whatsapp_reason"] = reason
                    valid_leads.append(lead)
                    console.print(f"  [green]\u2705 VALID[/green]   [dim]{short_name(company)}[/dim]")
                elif status == "Invalid":
                    invalid_count += 1
                    console.print(f"  [red]\u274c INVALID[/red] [dim]{short_name(company)}[/dim]")
                else:
                    unknown_count += 1
                    console.print(f"  [yellow]\u26a0\ufe0f UNKNOWN[/yellow] [dim]{short_name(company)}[/dim]")
                
                progress.update(task, advance=1)
        
        console.print()
        console.print("=" * 55)
        console.print(f"[bold]\U0001f389 WhatsApp Filtering Complete[/bold]")
        console.print(f"[green]\u2705 Valid   : {len(valid_leads)}[/green]")
        console.print(f"[red]\u274c Invalid : {invalid_count}[/red]")
        console.print(f"[yellow]\u26a0\ufe0f Unknown : {unknown_count}[/yellow]")
        console.print("=" * 55)
        
        await context.close()
    
    return valid_leads
