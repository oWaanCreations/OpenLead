# OpenLead
 
**Professional lead generation tool with a modern web interface. Find WhatsApp-ready businesses from Google Maps — no coding required.**
 
![OpenLead UI](https://img.shields.io/badge/UI-Web%20App-4ec9b0)
![Python](https://img.shields.io/badge/Python-3.10%2B-3776ab)
![FastAPI](https://img.shields.io/badge/API-FastAPI-009688)
 
---
 
## What Is OpenLead?
 
OpenLead is a **browser-based lead generation tool** that:
 
1. **Scrapes Google Maps** for businesses (worldwide coverage)
2. **Filters via WhatsApp Web** to find valid WhatsApp contacts only
3. **Exports clean data** as HTML reports with one-click WhatsApp chat
 
All controlled through a **professional dark-themed web dashboard** — like VSCode, but for lead generation.
 
---
 
## Features
 
### 🗺️ Google Maps Scraping
- 500+ cities worldwide
- 40+ business niches
- Skips businesses with websites (better conversion)
- Smart rate-limiting to avoid bans
 
### 💬 WhatsApp Filtering
- Opens WhatsApp Web automatically
- QR scan once, then auto-checks all numbers
- Keeps only valid WhatsApp contacts
- Shows valid/invalid count in real-time
 
### 🖥️ Web Dashboard
- **VSCode-inspired dark UI** — minimal, professional
- **Real-time progress** — watch scraping live
- **Terminal view** — see exactly what's happening
- **Results table** — search, sort, export
- **One-click WhatsApp** — open chat instantly
 
### 📊 Export Options
- Beautiful HTML report (opens in browser)
- Search and filter within results
- Sort by city, niche, rating
- One-click WhatsApp for every lead
 
---
 
## Quick Start
 
### 1. Install Python
Download Python 3.10+ from [python.org](https://python.org)
 
**Windows:** Check "Add Python to PATH" during install.
 
### 2. Install Dependencies
```bash
pip install -r requirements.txt
```
 
### 3. Start the App
```bash
python web_app.py
```
 
### 4. Open Your Browser
Go to: `http://localhost:8080`
 
---
 
## How to Use
 
### Dashboard View
When you open the app, you'll see:
- **Sidebar** — Navigate between Dashboard, New Scrape, Results, Terminal
- **Status bar** — Shows total leads, cities, niches, current status
- **Activity log** — Recent scraping activity
 
### Starting a New Scrape
 
1. Click **"New Scrape"** in the sidebar
2. Set **Maximum Leads** (50-1000 recommended)
3. Choose options:
   - **Skip businesses with websites** — Recommended for cold calling
   - **Filter WhatsApp contacts** — Validates WhatsApp numbers
4. Click **"Start Scraping"**
 
### During Scraping
 
The **Progress Panel** shows:
- Live progress bar
- Current phase (Scraping / Filtering / Complete)
- Current business being processed
- Logs in real-time
 
**To stop early:** Click **"Stop"** — you'll keep all leads found so far.
 
### WhatsApp Filtering
 
If you enabled WhatsApp filtering:
1. A browser window opens with WhatsApp Web
2. Scan the QR code with your phone (one-time)
3. The tool automatically checks every number
4. Valid WhatsApp contacts are kept, invalid ones removed
 
### Viewing Results
 
Go to **"Results"** in the sidebar:
- Search by company name, city, or phone
- Sort by any column
- Click **"Open WhatsApp"** to start chatting instantly
- Click **"Download Report"** for the HTML file
 
### Terminal View
 
The **"Terminal"** section shows:
- Full activity logs
- Real-time updates during scraping
- Error messages if anything goes wrong
 
---
 
## Project Structure
 
```
OpenLead/
├── web/                    # Frontend (HTML, CSS, JS)
│   ├── index.html         # Main UI
│   ├── styles.css         # Dark theme styling
│   └── app.js             # Frontend logic
├── src/                    # Backend modules
│   ├── core/
│   │   ├── maps_scraper.py      # Google Maps scraping
│   │   ├── whatsapp_filter.py   # WhatsApp validation
│   │   └── html_report.py       # Report generation
│   └── config/
│       └── targets.py           # Cities & niches data
├── web_app.py             # Main web server (FastAPI)
├── requirements.txt       # Python dependencies
├── README.md             # This file
└── .gitignore            # Files to exclude from Git
```
 
---
 
## What Gets Saved
 
All generated files are in the `outputs/` folder:
 
- `whatsapp_leads_*.html` — Beautiful report with search & WhatsApp links
- `whatsapp_leads_*.json` — Raw data for custom processing
 
 
---
 
## Requirements
 
- **Python 3.10+**
- **Windows / Mac / Linux**
- **Chrome, Edge, or Opera** (for WhatsApp Web)
- **WhatsApp on your phone** (for QR scan)
 
---
 
## Troubleshooting
 
### "WhatsApp Web won't open"
- Make sure you have Chrome, Edge, or Opera installed
- The tool uses Playwright Chromium by default
 
### "No leads found"
- Try a broader niche (e.g., "marketing" instead of "SEO agency")
- Try a larger city
- Increase the max leads limit
 
### "Scraping is slow"
- This is normal — Google Maps has rate limits
- The tool waits between requests to avoid being blocked
- Let it run, grab a coffee ☕
 
### "Browser closes immediately"
- Make sure you're logged into WhatsApp Web
- Check the Terminal for error messages
 
---
 
## Tips for Best Results
 
| Tip | Why It Works |
|-----|--------------|
| Start with 50-100 leads | Test your niche/city combo first |
| Target businesses without websites | Easier to sell web services to |
| Use specific niches | "Web designers" > "marketing agencies" |
| Try smaller cities | Less competition, higher response rates |
| Scrape during business hours | Better for immediate WhatsApp follow-up |
 
---
 
## Tech Stack
 
- **Backend:** FastAPI (Python) + WebSocket for real-time updates
- **Frontend:** Vanilla JS + VSCode-inspired dark UI
- **Scraping:** Playwright (Google Maps automation)
- **WhatsApp:** Playwright + clipboard paste method
- **Styling:** CSS variables, JetBrains Mono font
 
 
## Contributing
 
Found a bug? Want a feature?
 
1. Open an issue on GitHub
2. Describe the problem or feature request
3. Be specific — screenshots help
 
---
 
## License
 
MIT License — use it, modify it, sell with it. Just give the credit.
 
---
 
**Ready to find your next 100 clients?**
 
```bash
python web_app.py
```
 
Then open `http://localhost:8080` in your browser.
