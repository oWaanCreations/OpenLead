#!/usr/bin/env python3
"""
OpenLead 1.0 — Google Maps Lead Extractor with WhatsApp Filter
One command: Scrape -> Filter -> Beautiful HTML Report
"""

import sys
import os
import subprocess
import asyncio
import json
import time
import threading
import signal

# ─── Auto Setup ──────────────────────────────────────────────────────────────
SETUP_FILE = ".setup_complete"
REQUIRED_PACKAGES = ["playwright", "rich"]

if not os.path.exists(SETUP_FILE):
    print("First run detected. Setting up environment...\n")
    for pkg in REQUIRED_PACKAGES:
        try:
            __import__(pkg)
        except ImportError:
            print(f"  Installing {pkg}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", pkg, "-q"])
    
    # Install Playwright browsers
    try:
        from playwright.async_api import async_playwright
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "playwright", "-q"])
    
    print("  Installing Playwright Chromium...")
    subprocess.check_call([sys.executable, "-m", "playwright", "install", "chromium"])
    
    with open(SETUP_FILE, "w") as f:
        f.write("done")
    print("\nSetup complete! Run the script again to start.\n")
    sys.exit(0)

# ─── Imports ─────────────────────────────────────────────────────────────────
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn
from rich.table import Table
from rich.layout import Layout
from rich.live import Live
from rich.align import Align
from rich import box

from src.config.targets import CITIES, NICHES
from src.core.maps_scraper import scrape_google_maps
from src.core.whatsapp_filter import filter_whatsapp_leads
from src.core.html_report import generate_html_report

console = Console()

# ─── Global Stop Flag ────────────────────────────────────────────────────────
stop_requested = False

def listen_for_stop():
    """Background thread: press BACKSPACE to stop scraping early."""
    global stop_requested
    try:
        import msvcrt
        while not stop_requested:
            if msvcrt.kbhit():
                key = msvcrt.getch()
                if key == b'\x08':  # BACKSPACE
                    stop_requested = True
                    console.print("\n[bold yellow]Stop requested by user. Wrapping up...[/bold yellow]")
                    break
            time.sleep(0.1)
    except Exception:
        pass

# ─── Banner ──────────────────────────────────────────────────────────────────
def show_banner():
    from rich.columns import Columns
    
    # Clean, terminal-width-safe banner using Rich components
    title = Text("OPENLEAD", style="bold bright_white", justify="center")
    subtitle = Text("Lead Generation Tool", style="dim", justify="center")
    tagline = Text("Google Maps  WhatsApp Filter  HTML Report", style="cyan", justify="center")
    
    # Build the banner content
    content = Text()
    content.append("\n")
    content.append("◆ ", style="bright_cyan")
    content.append("OPEN", style="bold bright_white")
    content.append("LEAD", style="bold cyan")
    content.append(" ◆\n", style="bright_cyan")
    content.append("Lead Generation Tool\n", style="dim")
    content.append("Google Maps  WhatsApp Filter  HTML Report", style="bright_black")
    
    console.print(Panel(
        Align.center(content),
        border_style="bright_black",
        box=box.ROUNDED,
        padding=(1, 2)
    ))

# ─── Config Display ──────────────────────────────────────────────────────────
def show_config(max_leads):
    table = Table(box=box.ROUNDED, border_style="dim", title="[bold]Configuration[/bold]")
    table.add_column("Setting", style="bright_white", no_wrap=True)
    table.add_column("Value", style="white")
    
    table.add_row("Target Cities", f"[white]{len(CITIES)}[/white] cities worldwide")
    table.add_row("Business Niches", f"[white]{len(NICHES)}[/white] categories")
    table.add_row("Max Leads", f"[bright_white]{max_leads}[/bright_white]")
    table.add_row("Website Filter", "[dim]Skip businesses WITH website[/dim]")
    table.add_row("WhatsApp Filter", "[white]Keep only WhatsApp contacts[/white]")
    table.add_row("Output", "[bright_white]outputs/whatsapp_leads.html[/bright_white]")
    
    console.print(table)
    console.print()

# ─── Main ────────────────────────────────────────────────────────────────────
def main():
    show_banner()
    
    # Ask for lead limit
    try:
        max_input = console.input("[bold bright_white]Maximum leads to collect[/bold bright_white] [dim](default: 1000)[/dim]: ")
        max_leads = int(max_input) if max_input.strip() else 1000
    except ValueError:
        max_leads = 1000
    
    show_config(max_leads)
    
    console.print(Panel(
        "[bold yellow]Press [BACKSPACE] at any time during scraping to stop early and proceed with found leads.[/bold yellow]",
        border_style="yellow",
        box=box.ROUNDED
    ))
    console.print()
    
    # ─── Phase 1: Scrape ─────────────────────────────────────────────────────
    console.rule("[bold magenta]Phase 1: Google Maps Scraping[/bold magenta]", style="magenta")
    
    stop_thread = threading.Thread(target=listen_for_stop, daemon=True)
    stop_thread.start()
    
    leads = asyncio.run(scrape_google_maps(max_leads, console, lambda: stop_requested))
    
    if not leads:
        console.print("\n[bold red]No leads found. Try again later.[/bold red]")
        input("\nPress Enter to exit...")
        return
    
    console.print(f"\n[bold green]Scraping complete! {len(leads)} unique leads found.[/bold green]")
    
    # Save raw leads
    raw_path = "outputs/raw_leads.json"
    os.makedirs("outputs", exist_ok=True)
    with open(raw_path, "w", encoding="utf-8") as f:
        json.dump(leads, f, indent=2, ensure_ascii=False)
    console.print(f"[dim]Raw leads saved to {raw_path}[/dim]\n")
    
    # ─── Phase 2: WhatsApp Filter ────────────────────────────────────────────
    console.rule("[bold magenta]Phase 2: WhatsApp Filtering[/bold magenta]", style="magenta")
    console.print("[dim]Opening WhatsApp Web to validate numbers...[/dim]\n")
    
    valid_leads = asyncio.run(filter_whatsapp_leads(leads, console))
    
    if not valid_leads:
        console.print("\n[bold red]No WhatsApp leads found.[/bold red]")
        input("\nPress Enter to exit...")
        return
    
    console.print(f"\n[bold green]Filtering complete! {len(valid_leads)} WhatsApp leads confirmed.[/bold green]")
    
    # ─── Phase 3: HTML Report ────────────────────────────────────────────────
    console.rule("[bold magenta]Phase 3: Generating HTML Report[/bold magenta]", style="magenta")
    
    html_path = "outputs/whatsapp_leads.html"
    generate_html_report(valid_leads, html_path)
    
    abs_path = os.path.abspath(html_path)
    console.print(f"\n[bold green]Report generated:[/bold green] [cyan]{abs_path}[/cyan]")
    
    # Final summary
    console.print()
    summary = Table(box=box.DOUBLE_EDGE, border_style="bright_cyan", title="[bold]Mission Complete[/bold]")
    summary.add_column("Metric", style="cyan")
    summary.add_column("Count", justify="right", style="green")
    summary.add_row("Total Scraped", str(len(leads)))
    summary.add_row("WhatsApp Valid", str(len(valid_leads)))
    summary.add_row("Filtered Out", str(len(leads) - len(valid_leads)))
    summary.add_row("Output File", html_path)
    console.print(summary)
    
    console.print("\n[bold bright_cyan]Open the HTML file in your browser and start cold calling![/bold bright_cyan]")
    console.print("[dim]Tip: Click any phone number to open WhatsApp chat directly.[/dim]\n")
    
    # Keep terminal open
    input("Press Enter to exit...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[bold red]Interrupted by user. Exiting.[/bold red]")
        input("\nPress Enter to exit...")
        sys.exit(0)
