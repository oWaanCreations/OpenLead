"""
HTML Report Generator — Creates a professional dark-themed searchable dashboard.
Part of OpenLead 1.0 — Google Maps Lead Extractor with WhatsApp Filter.
"""

import os
import re
import html as html_module

def generate_html_report(leads, output_path):
    """
    Generate a professional HTML report from filtered leads.
    
    Args:
        leads: List of lead dicts (must have whatsapp_status = "Valid")
        output_path: Path to write the HTML file
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Build table rows
    rows_html = []
    for idx, lead in enumerate(leads, 1):
        name = html_module.escape(lead.get("company_name", "Unknown"))
        city = html_module.escape(lead.get("city", ""))
        country = html_module.escape(lead.get("country", ""))
        rating = html_module.escape(lead.get("rating", "N/A"))
        phone = html_module.escape(lead.get("phone", ""))
        biz_type = html_module.escape(lead.get("business_type", ""))
        
        # WhatsApp link
        wa_link = f"https://wa.me/{re.sub(r'[^0-9]', '', phone)}" if phone else "#"
        
        rows_html.append(f"""
                        <tr>
                            <td>{idx}</td>
                            <td><div class="company-name">{name}</div></td>
                            <td><div class="city">{city}, {country}</div></td>
                            <td><span class="rating">⭐ {rating}</span></td>
                            <td><a href="{wa_link}" class="phone-link" target="_blank" title="Click to chat on WhatsApp">💬 {phone}</a></td>
                            <td style="color: var(--text-dim); font-size: 0.9rem;">{biz_type}</td>
                            <td><span class="badge badge-whatsapp">WhatsApp</span></td>
                        </tr>
        """)
    
    total_leads = len(leads)
    
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>OpenLead 1.0 | WhatsApp Leads Dashboard</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg: #0a0a0c;
            --card-bg: #16161a;
            --accent: #3d5afe;
            --accent-hover: #5b73ff;
            --text-main: #ffffff;
            --text-dim: #94a3b8;
            --success: #10b981;
            --danger: #ef4444;
            --warning: #f59e0b;
            --border: #2d2d35;
            --whatsapp: #25d366;
        }}
        
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        
        body {{
            font-family: 'Outfit', sans-serif;
            background-color: var(--bg);
            color: var(--text-main);
            padding: 40px 20px;
            line-height: 1.6;
            overflow-x: hidden;
        }}
        
        .container {{ max-width: 1400px; margin: 0 auto; }}
        
        header {{
            display: flex;
            justify-content: space-between;
            align-items: flex-end;
            margin-bottom: 40px;
            border-bottom: 1px solid var(--border);
            padding-bottom: 20px;
            flex-wrap: wrap;
            gap: 20px;
        }}
        
        header .title-area {{ border-left: 4px solid var(--accent); padding-left: 20px; }}
        header h1 {{ font-size: 2.2rem; font-weight: 600; letter-spacing: -1px; }}
        header p {{ color: var(--text-dim); font-size: 1rem; margin-top: 5px; }}
        
        .search-area {{ position: relative; width: 400px; max-width: 100%; }}
        
        #searchInput {{
            width: 100%;
            background: var(--card-bg);
            border: 1px solid var(--border);
            color: white;
            padding: 14px 24px;
            border-radius: 14px;
            outline: none;
            font-family: inherit;
            font-size: 0.95rem;
            transition: border 0.3s, box-shadow 0.3s;
        }}
        
        #searchInput:focus {{
            border-color: var(--accent);
            box-shadow: 0 0 20px rgba(61, 90, 254, 0.2);
        }}
        
        #searchInput::placeholder {{ color: #5a5a66; }}
        
        .stats {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }}
        
        .stat-card {{
            background: var(--card-bg);
            padding: 24px 20px;
            border-radius: 16px;
            border: 1px solid var(--border);
            transition: transform 0.2s, border-color 0.2s;
        }}
        
        .stat-card:hover {{ transform: translateY(-2px); border-color: var(--accent); }}
        .stat-card h3 {{ font-size: 0.75rem; color: var(--text-dim); text-transform: uppercase; letter-spacing: 1.5px; margin-bottom: 8px; }}
        .stat-card p {{ font-size: 2rem; font-weight: 700; color: var(--accent); }}
        .stat-card p.whatsapp {{ color: var(--whatsapp); }}
        
        .table-container {{
            overflow-x: auto;
            border-radius: 16px;
            border: 1px solid var(--border);
        }}
        
        table {{ width: 100%; border-collapse: separate; border-spacing: 0 8px; }}
        
        th {{
            text-align: left;
            padding: 18px 20px;
            color: var(--text-dim);
            font-weight: 500;
            font-size: 0.8rem;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            background: var(--card-bg);
            position: sticky;
            top: 0;
            z-index: 10;
        }}
        
        tbody tr {{
            background: var(--card-bg);
            transition: transform 0.2s, background 0.2s;
            cursor: pointer;
        }}
        
        tbody tr:hover {{ transform: scale(1.005); background: #1e1e24; }}
        
        td {{ padding: 18px 20px; border-top: 1px solid transparent; border-bottom: 1px solid transparent; }}
        td:first-child {{ border-top-left-radius: 12px; border-bottom-left-radius: 12px; color: var(--text-dim); width: 60px; text-align: center; font-weight: 600; }}
        td:last-child {{ border-top-right-radius: 12px; border-bottom-right-radius: 12px; }}
        
        .company-name {{ font-weight: 600; font-size: 1.05rem; color: #fff; }}
        .city {{ color: var(--text-dim); font-size: 0.9rem; }}
        
        .phone-link {{
            color: var(--whatsapp);
            text-decoration: none;
            font-weight: 600;
            background: rgba(37, 211, 102, 0.08);
            padding: 8px 16px;
            border-radius: 10px;
            font-size: 0.9rem;
            border: 1px solid rgba(37, 211, 102, 0.15);
            display: inline-block;
            transition: background 0.2s, transform 0.1s;
        }}
        
        .phone-link:hover {{ background: rgba(37, 211, 102, 0.15); transform: scale(1.02); }}
        
        .badge {{
            display: inline-block;
            padding: 6px 14px;
            border-radius: 8px;
            font-size: 0.7rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}
        
        .badge-whatsapp {{ background: rgba(37, 211, 102, 0.1); color: var(--whatsapp); border: 1px solid rgba(37, 211, 102, 0.2); }}
        .badge-noweb {{ background: rgba(239, 68, 68, 0.1); color: var(--danger); border: 1px solid rgba(239, 68, 68, 0.2); }}
        .rating {{ color: #fbbf24; font-weight: 600; font-size: 0.9rem; }}
        
        @keyframes fadeIn {{ from {{ opacity: 0; transform: translateY(10px); }} to {{ opacity: 1; transform: translateY(0); }} }}
        tbody tr {{ animation: fadeIn 0.4s ease forwards; }}
        
        .no-results {{
            text-align: center;
            padding: 60px 20px;
            color: var(--text-dim);
        }}
        
        .no-results h2 {{ font-size: 1.5rem; margin-bottom: 10px; }}
        
        @media (max-width: 768px) {{
            header {{ flex-direction: column; align-items: flex-start; }}
            .search-area {{ width: 100%; }}
            th, td {{ padding: 12px 10px; font-size: 0.85rem; }}
            .company-name {{ font-size: 0.95rem; }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <div class="title-area">
                <h1>WhatsApp Leads Dashboard</h1>
                <p>Businesses without websites — ready for cold outreach</p>
            </div>
            <div class="search-area">
                <input type="text" id="searchInput" onkeyup="filterTable()" placeholder="Search company, city, category or phone...">
            </div>
        </header>

        <div class="stats">
            <div class="stat-card">
                <h3>Total Leads</h3>
                <p>{total_leads}</p>
            </div>
            <div class="stat-card">
                <h3>WhatsApp Ready</h3>
                <p class="whatsapp">{total_leads}</p>
            </div>
            <div class="stat-card">
                <h3>Countries</h3>
                <p>{len(set(l.get('country', '') for l in leads))}</p>
            </div>
            <div class="stat-card">
                <h3>Categories</h3>
                <p>{len(set(l.get('business_type', '') for l in leads))}</p>
            </div>
        </div>

        <div class="table-container">
            <table id="leadsTable">
                <thead>
                    <tr>
                        <th>#</th>
                        <th>Company</th>
                        <th>Location</th>
                        <th>Rating</th>
                        <th>WhatsApp / Contact</th>
                        <th>Category</th>
                        <th>Status</th>
                    </tr>
                </thead>
                <tbody>
                    {''.join(rows_html) if rows_html else '<tr><td colspan="7"><div class="no-results"><h2>No leads yet</h2><p>Run the scraper to populate this dashboard.</p></div></td></tr>'}
                </tbody>
            </table>
        </div>
    </div>

    <script>
        function filterTable() {{
            var input = document.getElementById("searchInput");
            var filter = input.value.toUpperCase();
            var table = document.getElementById("leadsTable");
            var tr = table.getElementsByTagName("tr");

            for (var i = 1; i < tr.length; i++) {{
                var tds = tr[i].getElementsByTagName("td");
                var found = false;
                for (var j = 0; j < tds.length; j++) {{
                    if (tds[j]) {{
                        var txt = tds[j].textContent || tds[j].innerText;
                        if (txt.toUpperCase().indexOf(filter) > -1) {{
                            found = true;
                            break;
                        }}
                    }}
                }}
                tr[i].style.display = found ? "" : "none";
            }}
        }}
    </script>
</body>
</html>
"""
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
