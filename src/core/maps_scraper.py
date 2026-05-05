"""
Google Maps Scraper — Extracts businesses WITHOUT websites worldwide.
Part of OpenLead 1.0 — Google Maps Lead Extractor with WhatsApp Filter.
"""

import asyncio
import re
import os
from playwright.async_api import async_playwright

async def block_resources(route):
    """Block images/media to speed up scraping."""
    if route.request.resource_type in ["image", "media", "font"]:
        await route.abort()
    else:
        await route.continue_()

async def scrape_google_maps(max_leads: int, console, stop_check):
    """
    Scrape Google Maps for businesses without websites.

    Args:
        max_leads: Maximum number of leads to collect
        console: Rich Console instance for output
        stop_check: Callable that returns True if user pressed BACKSPACE

    Returns:
        List of lead dicts
    """
    from src.config.targets import CITIES, NICHES
    from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn, TimeElapsedColumn

    leads = []
    processed_phones = set()
    total_searches = len(CITIES) * len(NICHES)

    progress = Progress(
        SpinnerColumn(style="white"),
        TextColumn("[bold bright_white]{task.description}"),
        BarColumn(bar_width=40, complete_style="white"),
        TaskProgressColumn(),
        TimeElapsedColumn(),
        console=console,
    )

    with progress:
        task = progress.add_task(
            f"[bright_white]Scraping Google Maps...[/bright_white]",
            total=max_leads,
        )

        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            )
            page = await context.new_page()
            await page.route("**/*", block_resources)

            search_count = 0

            for city in CITIES:
                if stop_check():
                    console.print("[dim]⏹ Stopping as requested...[/dim]")
                    break

                for niche in NICHES:
                    if stop_check():
                        break

                    if len(leads) >= max_leads:
                        break

                    search_count += 1
                    search_query = f"{niche} in {city}"

                    progress.update(task, description=f"[bright_white]Searching: {niche} in {city}[/bright_white]")

                    try:
                        url = f"https://www.google.com/maps/search/{search_query.replace(' ', '+')}/"
                        # Dynamic wait - navigate and wait for network idle (faster than fixed timeout)
                        await page.goto(url, timeout=30000, wait_until="networkidle")
                    except Exception:
                        continue

                    # Wait for results - dynamic with shorter timeout
                    try:
                        # Wait for either results or "no results" message
                        await page.wait_for_selector(
                            'a[href*="https://www.google.com/maps/place/"], div[role="main"]',
                            timeout=5000
                        )
                    except Exception:
                        continue

                    # Scroll to load more - dynamic wait based on content changes
                    try:
                        sidebar = page.locator('div[role="feed"]')
                        if await sidebar.count() > 0:
                            previous_count = 0
                            same_count_times = 0
                            max_scrolls = 5
                            scroll_count = 0
                            
                            while scroll_count < max_scrolls and not stop_check():
                                try:
                                    await sidebar.first.evaluate("el => el.scrollBy(0, 3000)")
                                except:
                                    pass
                                
                                # Dynamic wait - wait for new items or timeout quickly
                                try:
                                    await page.wait_for_timeout(300)  # Short wait for lazy load
                                    current_count = await page.locator('a[href*="https://www.google.com/maps/place/"]').count()
                                    
                                    if current_count > previous_count:
                                        previous_count = current_count
                                        same_count_times = 0
                                    else:
                                        same_count_times += 1
                                        # Stop if no new items after 2 attempts
                                        if same_count_times >= 2:
                                            break
                                except:
                                    break
                                
                                scroll_count += 1
                    except Exception:
                        pass

                    # Extract cards
                    cards = await page.locator('div.Nv2PK').all()
                    if not cards:
                        cards = await page.locator('div[role="article"]').all()

                    found_this_query = 0

                    for card in cards:
                        if stop_check() or len(leads) >= max_leads:
                            break

                        try:
                            text = await card.evaluate("el => el.innerText")
                            if not text:
                                continue

                            # SKIP if website exists
                            if "Website" in text or "website" in text.lower():
                                continue

                            lines = [line.strip() for line in text.split('\n') if line.strip()]
                            if len(lines) < 2:
                                continue

                            name = lines[0]
                            rating = "N/A"
                            phone = ""

                            for line in lines[1:]:
                                # Rating: digits with optional decimal, 1-3 chars
                                if re.match(r'^\d(\.\d)?$', line) and len(line) <= 3:
                                    rating = line
                                else:
                                    # Phone: starts with + and has 8+ digits
                                    match = re.search(r'(\+\d[\d\s\-\(\)]{7,25})', line)
                                    if match:
                                        phone = match.group(1).strip()

                            if not phone:
                                continue

                            # Clean phone
                            clean_phone = re.sub(r'[\s\-\(\)]', '', phone)
                            if clean_phone in processed_phones:
                                continue
                            processed_phones.add(clean_phone)

                            # Parse city/country
                            city_name = city.split(',')[0].strip()
                            country = city.split(',')[1].strip() if ',' in city else ""

                            lead = {
                                "company_name": name,
                                "country": country,
                                "city": city_name,
                                "rating": rating,
                                "phone": clean_phone,
                                "business_type": niche,
                                "website_status": "No Website",
                                "search_query": search_query,
                            }

                            leads.append(lead)
                            found_this_query += 1

                            progress.update(task, advance=1, description=f"[white]Lead #{len(leads):04d}[/white] | [bright_white]{name[:30]}...[/bright_white] | [dim]{clean_phone}[/dim]")

                        except Exception:
                            continue

                    if found_this_query > 0:
                        console.print(f"[dim]   📍 {city_name}: {found_this_query} leads[/dim]")

                    if len(leads) >= max_leads:
                        break

                if len(leads) >= max_leads:
                    break

            await browser.close()

    return leads
