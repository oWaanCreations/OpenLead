# OpenLead — Find WhatsApp Leads from Google Maps

**Stop wasting time on cold calling. Get a list of businesses that actually use WhatsApp.**

OpenLead finds businesses from Google Maps, checks which ones have WhatsApp, and gives you a clean list with one-click WhatsApp chat links.

---

## What You Get

1. **Scrape Google Maps** — Find businesses in any city, any niche
2. **WhatsApp Check** — Automatically verify which numbers have WhatsApp
3. **Clean HTML Report** — Sort, search, and click to chat instantly

No coding. No manual work. Just results.

---

## Quick Start (3 Steps)

### Step 1: Install Python
Download Python 3.10+ from [python.org](https://python.org)  
**Windows users:** Check "Add Python to PATH" during installation.

### Step 2: Download This Tool
```bash
git clone https://github.com/YOUR_USERNAME/OpenLead.git
cd OpenLead
```

Or download the ZIP and extract it.

### Step 3: Run It
```bash
pip install -r requirements.txt
python run.py
```

That's it. Follow the prompts.

---

## How It Works

### Phase 1: Google Maps Scraping
The tool searches Google Maps for businesses in your chosen cities and niches. It skips businesses that already have websites (usually harder to sell to).

### Phase 2: WhatsApp Verification
Opens WhatsApp Web in your browser. You'll scan a QR code once. Then it automatically checks every phone number to see if it has WhatsApp.

### Phase 3: Get Your Report
A beautiful HTML file opens in your browser. Sort by city, search by business name, click any number to start a WhatsApp chat instantly.

---

## Example Output

**Input:** "Find web designers in New York, max 100 leads"  
**Output:** 42 businesses with verified WhatsApp numbers, ready to message.

**The HTML report includes:**
- Search bar (find any business instantly)
- Sort by city/niche/rating
- One-click WhatsApp buttons
- Export to CSV/Excel

---

## Requirements

- Python 3.10 or newer
- Windows, Mac, or Linux
- WhatsApp on your phone (for QR scan)

---

## Tips for Best Results

**Start small** — Test with 50-100 leads first  
**Use specific niches** — "Web designers" works better than "marketing"  
**Check smaller cities** — Less competition, higher response rates  

---

## Common Issues

**"WhatsApp Web not opening"** — Make sure you have Chrome/Edge/Opera installed  
**"No leads found"** — Try a broader niche or larger city  
**"Slow scraping"** — Rare but Normal. Google Maps has rate limits. Let it run.

---

## Support

Found a bug? Have a feature idea?  
Open an issue on GitHub.

---

## License

MIT — Use it, modify it, sell with it. Just keep the credit.

---

**Ready to find your next client? Run `python run.py` and start scraping.**
