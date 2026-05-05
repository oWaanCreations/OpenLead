"""
OpenLead Web Interface — Modern web UI for OpenLead
Run: python web_app.py
Then open http://localhost:8080 in your browser
"""

import asyncio
import json
import os
import sys
from pathlib import Path
from typing import Optional
from datetime import datetime
import threading
import queue

# Add src to path
sys.path.insert(0, str(Path(__file__).parent))

from fastapi import FastAPI, WebSocket, WebSocketDisconnect, HTTPException, BackgroundTasks
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse
from pydantic import BaseModel
import uvicorn

# Import OpenLead core modules
from src.config.targets import CITIES, NICHES
from src.core.maps_scraper import scrape_google_maps
from src.core.whatsapp_filter import filter_whatsapp_leads
from src.core.html_report import generate_html_report
from rich.console import Console

app = FastAPI(title="OpenLead Web", version="1.0")

# Global state
scraping_state = {
    "is_running": False,
    "progress": 0,
    "total": 0,
    "current_lead": "",
    "leads": [],
    "phase": "idle",  # idle, scraping, filtering, complete
    "message": "",
    "logs": []
}

state_lock = threading.Lock()

class ScrapingConfig(BaseModel):
    max_leads: int = 100
    selected_cities: Optional[list] = None
    selected_niches: Optional[list] = None
    skip_whatsapp_filter: bool = False

def add_log(message: str):
    """Add a log message to the state."""
    with state_lock:
        timestamp = datetime.now().strftime("%H:%M:%S")
        scraping_state["logs"].append(f"[{timestamp}] {message}")
        if len(scraping_state["logs"]) > 100:
            scraping_state["logs"] = scraping_state["logs"][-100:]

def update_state(**kwargs):
    """Thread-safe state update."""
    with state_lock:
        scraping_state.update(kwargs)

async def progress_callback(current: int, total: int, lead_info: str = ""):
    """Callback for scraping progress."""
    update_state(
        progress=current,
        total=total,
        current_lead=lead_info,
        message=f"Lead #{current}: {lead_info}" if lead_info else f"Progress: {current}/{total}"
    )

class WebConsole(Console):
    """Web-compatible console that also logs to the web UI."""
    def __init__(self):
        super().__init__()
    
    def print(self, *args, **kwargs):
        message = " ".join(str(a) for a in args)
        add_log(message)
        super().print(*args, **kwargs)
    
    def rule(self, title: str, **kwargs):
        add_log(f"--- {title} ---")
        super().rule(title, **kwargs)
    
    def input(self, prompt: str, **kwargs) -> str:
        # For web, we use default values (bundled Chromium = choice 1)
        return ""

async def run_whatsapp_filtering_task(leads: list, console):
    """Run WhatsApp filtering using the original filter_whatsapp_leads function."""
    from src.core.whatsapp_filter import filter_whatsapp_leads
    
    add_log("=" * 55)
    add_log("Phase 2: WhatsApp Filtering")
    add_log("=" * 55)
    add_log("Opening WhatsApp Web in browser...")
    add_log("Please scan QR code if prompted (one-time only)")
    
    try:
        # Call the original filter function from the repo
        valid_leads = await filter_whatsapp_leads(leads, console)
        
        add_log("")
        add_log("=" * 55)
        add_log(f"WhatsApp Filtering Complete - {len(valid_leads)} valid leads")
        add_log("=" * 55)
        
        return valid_leads if valid_leads else leads
        
    except Exception as e:
        add_log(f"❌ WhatsApp filtering error: {str(e)}")
        return leads  # Return original leads if filtering fails

async def run_scraping_task(config: ScrapingConfig):
    """Run the scraping task in background with WhatsApp filtering."""
    global scraping_state
    
    try:
        update_state(
            is_running=True,
            phase="scraping",
            progress=0,
            total=config.max_leads,
            message="Starting Google Maps scraping...",
            leads=[],
            logs=[]
        )
        
        # Create a web-compatible console
        web_console = WebConsole()
        
        # Override stop check
        def stop_check():
            return not scraping_state["is_running"]
        
        # Phase 1: Scraping
        add_log("=" * 55)
        add_log("Phase 1: Google Maps Scraping")
        add_log("=" * 55)
        add_log(f"Starting scrape for max {config.max_leads} leads")
        
        leads = await scrape_google_maps_with_progress(
            config.max_leads, 
            web_console, 
            stop_check,
            progress_callback
        )
        
        if not leads:
            update_state(is_running=False, phase="idle", message="No leads found")
            add_log("❌ No leads found. Try again later.")
            return
        
        add_log(f"✅ Scraping complete! {len(leads)} leads found.")
        
        # Save raw leads
        os.makedirs("outputs", exist_ok=True)
        raw_path = "outputs/raw_leads.json"
        with open(raw_path, "w", encoding="utf-8") as f:
            json.dump(leads, f, indent=2, ensure_ascii=False)
        add_log(f"Raw leads saved to {raw_path}")
        
        # Phase 2: WhatsApp Filtering (if enabled and enough leads)
        valid_leads = leads
        
        if not config.skip_whatsapp_filter and len(leads) > 0:
            update_state(
                phase="filtering",
                progress=0,
                total=len(leads),
                message="Starting WhatsApp filtering..."
            )
            
            valid_leads = await run_whatsapp_filtering_task(leads, web_console)
            
            if not valid_leads:
                add_log("❌ No valid WhatsApp leads found.")
                update_state(is_running=False, phase="idle", message="No valid WhatsApp leads")
                return
            
            add_log(f"✅ WhatsApp filtering complete! {len(valid_leads)} valid leads.")
        else:
            add_log("⚠️ Skipping WhatsApp filtering (disabled or no leads)")
        
        # Phase 3: Generate Report
        add_log("")
        add_log("=" * 55)
        add_log("Phase 3: Generating HTML Report")
        add_log("=" * 55)
        
        update_state(phase="generating", message="Generating HTML report...")
        html_path = "outputs/whatsapp_leads.html"
        generate_html_report(valid_leads, html_path)
        add_log(f"✅ Report generated: {html_path}")
        
        # Final Summary
        add_log("")
        add_log("=" * 55)
        add_log("MISSION COMPLETE")
        add_log("=" * 55)
        add_log(f"📊 Total Scraped:   {len(leads)}")
        add_log(f"📱 WhatsApp Valid: {len(valid_leads)}")
        add_log(f"🗑️ Filtered Out:   {len(leads) - len(valid_leads)}")
        add_log(f"📁 Output File:    {html_path}")
        add_log("=" * 55)
        add_log("")
        add_log("Open the HTML file in your browser to see the results!")
        add_log("Tip: Click any phone number to open WhatsApp chat directly.")
        
        update_state(
            is_running=False,
            phase="complete",
            progress=len(valid_leads),
            total=len(valid_leads),
            leads=valid_leads,
            message=f"Complete! {len(valid_leads)} leads generated."
        )
        
    except Exception as e:
        add_log(f"❌ Error: {str(e)}")
        update_state(is_running=False, phase="error", message=f"Error: {str(e)}")
        raise

async def scrape_google_maps_with_progress(max_leads: int, console, stop_check, progress_cb):
    """Wrapper to inject progress callback into scraper."""
    from playwright.async_api import async_playwright
    import re
    from src.config.targets import CITIES, NICHES
    
    leads = []
    processed_phones = set()
    
    selected_cities = scraping_state.get("selected_cities") or CITIES[:50]  # Limit for web
    selected_niches = scraping_state.get("selected_niches") or NICHES[:10]
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = await context.new_page()
        
        # Block resources for speed
        async def block_resources(route):
            if route.request.resource_type in ["image", "media", "font"]:
                await route.abort()
            else:
                await route.continue_()
        
        await page.route("**/*", block_resources)
        
        for city in selected_cities:
            if stop_check() or len(leads) >= max_leads:
                break
            
            for niche in selected_niches:
                if stop_check() or len(leads) >= max_leads:
                    break
                
                search_query = f"{niche} in {city}"
                add_log(f"Searching: {search_query}")
                
                try:
                    url = f"https://www.google.com/maps/search/{search_query.replace(' ', '+')}/"
                    await page.goto(url, timeout=60000, wait_until="domcontentloaded")
                    await page.wait_for_selector('a[href*="https://www.google.com/maps/place/"]', timeout=8000)
                    
                    # Scroll to load more
                    try:
                        sidebar = page.locator('div[role="feed"]')
                        if await sidebar.count() > 0:
                            for _ in range(3):
                                await sidebar.first.evaluate("el => el.scrollBy(0, 5000)")
                                await asyncio.sleep(0.3)
                    except:
                        pass
                    
                    # Extract cards
                    cards = await page.locator('div.Nv2PK').all()
                    if not cards:
                        cards = await page.locator('div[role="article"]').all()
                    
                    for card in cards:
                        if stop_check() or len(leads) >= max_leads:
                            break
                        
                        try:
                            text = await card.evaluate("el => el.innerText")
                            if not text or "Website" in text:
                                continue
                            
                            lines = [line.strip() for line in text.split('\n') if line.strip()]
                            if len(lines) < 2:
                                continue
                            
                            name = lines[0]
                            rating = "N/A"
                            phone = ""
                            
                            for line in lines[1:]:
                                if re.match(r'^\d(\.\d)?$', line) and len(line) <= 3:
                                    rating = line
                                else:
                                    match = re.search(r'(\+\d[\d\s\-\(\)]{7,25})', line)
                                    if match:
                                        phone = match.group(1).strip()
                            
                            if not phone:
                                continue
                            
                            clean_phone = re.sub(r'[\s\-\(\)]', '', phone)
                            if clean_phone in processed_phones:
                                continue
                            processed_phones.add(clean_phone)
                            
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
                            await progress_cb(len(leads), max_leads, f"{name[:30]}... | {clean_phone}")
                            
                        except Exception as e:
                            continue
                            
                except Exception as e:
                    add_log(f"Error searching {search_query}: {str(e)[:50]}")
                    continue
        
        await browser.close()
    
    return leads

@app.get("/", response_class=HTMLResponse)
async def root():
    """Serve the main web interface."""
    return FileResponse("web/index.html")

@app.get("/api/status")
async def get_status():
    """Get current scraping status."""
    with state_lock:
        return JSONResponse(content=scraping_state)

@app.get("/api/config")
async def get_config():
    """Get available configuration options."""
    return JSONResponse(content={
        "cities": CITIES,
        "niches": NICHES,
        "total_cities": len(CITIES),
        "total_niches": len(NICHES)
    })

@app.post("/api/start")
async def start_scraping(config: ScrapingConfig, background_tasks: BackgroundTasks):
    """Start a new scraping job."""
    with state_lock:
        if scraping_state["is_running"]:
            raise HTTPException(status_code=400, detail="Scraping already in progress")
        scraping_state["selected_cities"] = config.selected_cities
        scraping_state["selected_niches"] = config.selected_niches
    
    # Run in background
    asyncio.create_task(run_scraping_task(config))
    
    return {"message": "Scraping started", "config": config.model_dump()}

@app.post("/api/stop")
async def stop_scraping():
    """Stop the current scraping job."""
    with state_lock:
        scraping_state["is_running"] = False
    return {"message": "Stop requested"}

@app.get("/api/results")
async def get_results():
    """Get current leads/results."""
    with state_lock:
        return JSONResponse(content={
            "leads": scraping_state["leads"],
            "count": len(scraping_state["leads"])
        })

@app.get("/api/download/{format}")
async def download_results(format: str):
    """Download results in various formats."""
    with state_lock:
        leads = scraping_state["leads"]
    
    if not leads:
        raise HTTPException(status_code=404, detail="No results available")
    
    if format == "json":
        return JSONResponse(content=leads)
    elif format == "csv":
        import csv
        import io
        output = io.StringIO()
        writer = csv.DictWriter(output, fieldnames=leads[0].keys())
        writer.writeheader()
        writer.writerows(leads)
        return HTMLResponse(
            content=output.getvalue(),
            headers={"Content-Disposition": "attachment; filename=openlead_results.csv"}
        )
    elif format == "html":
        if os.path.exists("outputs/whatsapp_leads.html"):
            return FileResponse("outputs/whatsapp_leads.html", filename="openlead_results.html")
        raise HTTPException(status_code=404, detail="HTML report not generated yet")
    else:
        raise HTTPException(status_code=400, detail="Invalid format. Use: json, csv, html")

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """WebSocket for real-time updates."""
    await websocket.accept()
    try:
        while True:
            with state_lock:
                await websocket.send_json(scraping_state)
            await asyncio.sleep(0.5)
    except WebSocketDisconnect:
        pass

# Mount static files
if os.path.exists("web"):
    app.mount("/static", StaticFiles(directory="web"), name="static")

if __name__ == "__main__":
    print("=" * 60)
    print("  OpenLead Web Interface")
    print("  Modern web UI for OpenLead")
    print("=" * 60)
    print()
    print("  Starting server...")
    print("  Open http://localhost:8080 in your browser")
    print()
    print("  Press Ctrl+C to stop")
    print("=" * 60)
    print()
    
    uvicorn.run(app, host="0.0.0.0", port=8080)
