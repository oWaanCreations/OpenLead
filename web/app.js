// OpenLead Web — Frontend Application

const API_BASE = '';
let ws = null;
let currentResults = [];
let allCities = [];
let allNiches = [];

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    initNavigation();
    loadConfig();
    connectWebSocket();
    refreshStatus();
});

// Navigation
function initNavigation() {
    const navItems = document.querySelectorAll('.nav-item');
    const sections = document.querySelectorAll('.section');
    
    navItems.forEach(item => {
        item.addEventListener('click', (e) => {
            e.preventDefault();
            const sectionId = item.dataset.section;
            
            navItems.forEach(n => n.classList.remove('active'));
            sections.forEach(s => s.classList.remove('active'));
            
            item.classList.add('active');
            document.getElementById(sectionId).classList.add('active');
        });
    });
}

// WebSocket Connection
function connectWebSocket() {
    const protocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:';
    ws = new WebSocket(`${protocol}//${window.location.host}/ws`);
    
    ws.onopen = () => {
        console.log('WebSocket connected');
        updateConnectionStatus(true);
    };
    
    ws.onmessage = (event) => {
        const state = JSON.parse(event.data);
        updateUI(state);
    };
    
    ws.onclose = () => {
        console.log('WebSocket disconnected');
        updateConnectionStatus(false);
        setTimeout(connectWebSocket, 3000);
    };
    
    ws.onerror = (err) => {
        console.error('WebSocket error:', err);
    };
}

function updateConnectionStatus(connected) {
    const status = document.getElementById('connectionStatus');
    if (status) {
        status.innerHTML = `
            <span class="status-dot" style="background: ${connected ? 'var(--success)' : 'var(--danger)'}"></span>
            <span class="nav-label">${connected ? 'Connected' : 'Offline'}</span>
        `;
    }
}

// Load Configuration
async function loadConfig() {
    try {
        const response = await fetch(`${API_BASE}/api/config`);
        const config = await response.json();
        
        allCities = config.cities || [];
        allNiches = config.niches || [];
        
        document.getElementById('totalCities').textContent = config.total_cities || allCities.length;
        document.getElementById('totalNiches').textContent = config.total_niches || allNiches.length;
        
        populateCitiesList(allCities);
        populateNichesList(allNiches);
        
        // Select first 10 cities and 5 niches by default
        selectFirstDefaults();
    } catch (err) {
        console.error('Failed to load config:', err);
        addLog('error', 'Failed to load configuration');
    }
}

function populateCitiesList(cities) {
    const container = document.getElementById('citiesList');
    container.innerHTML = cities.map((city, idx) => `
        <label class="checkbox-item" title="${city}">
            <input type="checkbox" name="city" value="${city}" id="city-${idx}">
            <span>${city}</span>
        </label>
    `).join('');
    
    // Add change listeners
    container.querySelectorAll('input[type="checkbox"]').forEach(cb => {
        cb.addEventListener('change', updateCityCount);
    });
}

function populateNichesList(niches) {
    const container = document.getElementById('nichesList');
    container.innerHTML = niches.map((niche, idx) => `
        <label class="checkbox-item">
            <input type="checkbox" name="niche" value="${niche}" id="niche-${idx}">
            <span>${niche}</span>
        </label>
    `).join('');
    
    container.querySelectorAll('input[type="checkbox"]').forEach(cb => {
        cb.addEventListener('change', updateNicheCount);
    });
}

function selectFirstDefaults() {
    // Select first 10 cities
    document.querySelectorAll('#citiesList input[type="checkbox"]').forEach((cb, idx) => {
        if (idx < 10) cb.checked = true;
    });
    
    // Select first 5 niches
    document.querySelectorAll('#nichesList input[type="checkbox"]').forEach((cb, idx) => {
        if (idx < 5) cb.checked = true;
    });
    
    updateCityCount();
    updateNicheCount();
}

function updateCityCount() {
    const count = document.querySelectorAll('#citiesList input[type="checkbox"]:checked').length;
    document.getElementById('selectedCitiesCount').textContent = `${count} selected`;
}

function updateNicheCount() {
    const count = document.querySelectorAll('#nichesList input[type="checkbox"]:checked').length;
    document.getElementById('selectedNichesCount').textContent = `${count} selected`;
}

// Selection Helpers
function selectAllCities() {
    document.querySelectorAll('#citiesList input[type="checkbox"]').forEach(cb => cb.checked = true);
    updateCityCount();
}

function deselectAllCities() {
    document.querySelectorAll('#citiesList input[type="checkbox"]').forEach(cb => cb.checked = false);
    updateCityCount();
}

function selectEurope() {
    const europeanCountries = ['Germany', 'France', 'Italy', 'Spain', 'Netherlands', 'Belgium', 
        'Switzerland', 'Austria', 'Sweden', 'Norway', 'Denmark', 'Finland', 'Ireland', 
        'Portugal', 'Greece', 'Poland', 'Czech Republic', 'Hungary', 'Romania', 'Bulgaria',
        'Croatia', 'Serbia', 'Slovenia', 'Slovakia', 'UK'];
    
    document.querySelectorAll('#citiesList input[type="checkbox"]').forEach(cb => {
        const isEurope = europeanCountries.some(country => cb.value.includes(country));
        cb.checked = isEurope;
    });
    updateCityCount();
}

function selectAllNiches() {
    document.querySelectorAll('#nichesList input[type="checkbox"]').forEach(cb => cb.checked = true);
    updateNicheCount();
}

function deselectAllNiches() {
    document.querySelectorAll('#nichesList input[type="checkbox"]').forEach(cb => cb.checked = false);
    updateNicheCount();
}

// Scraping Control
async function startScraping() {
    const maxLeads = parseInt(document.getElementById('maxLeads').value) || 100;
    const enableWhatsappFilter = document.getElementById('enableWhatsappFilter').checked;
    
    const selectedCities = Array.from(document.querySelectorAll('#citiesList input[type="checkbox"]:checked'))
        .map(cb => cb.value);
    const selectedNiches = Array.from(document.querySelectorAll('#nichesList input[type="checkbox"]:checked'))
        .map(cb => cb.value);
    
    if (selectedCities.length === 0 || selectedNiches.length === 0) {
        alert('Please select at least one city and one niche');
        return;
    }
    
    const config = {
        max_leads: maxLeads,
        selected_cities: selectedCities,
        selected_niches: selectedNiches,
        skip_whatsapp_filter: !enableWhatsappFilter  // If checked, we DON'T skip
    };
    
    try {
        const response = await fetch(`${API_BASE}/api/start`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(config)
        });
        
        if (!response.ok) {
            const err = await response.json();
            throw new Error(err.detail || 'Failed to start scraping');
        }
        
        showProgressCard();
        setButtonState('running');
        addLog('info', `Started scraping: ${maxLeads} max leads, ${selectedCities.length} cities, ${selectedNiches.length} niches`);
        
    } catch (err) {
        console.error('Start error:', err);
        addLog('error', `Failed to start: ${err.message}`);
        alert(err.message);
    }
}

async function stopScraping() {
    try {
        await fetch(`${API_BASE}/api/stop`, { method: 'POST' });
        addLog('warning', 'Stop requested by user');
        setButtonState('idle');
    } catch (err) {
        console.error('Stop error:', err);
    }
}

function showProgressCard() {
    document.getElementById('progressCard').style.display = 'block';
}

function setButtonState(state) {
    const startBtn = document.getElementById('startBtn');
    const stopBtn = document.getElementById('stopBtn');
    
    if (state === 'running') {
        startBtn.disabled = true;
        stopBtn.disabled = false;
    } else {
        startBtn.disabled = false;
        stopBtn.disabled = true;
    }
}

// UI Updates
function updateUI(state) {
    // Update status card
    const statusCard = document.getElementById('statusCard');
    const statusValue = document.getElementById('currentStatus');
    
    statusValue.textContent = state.phase.charAt(0).toUpperCase() + state.phase.slice(1);
    
    statusCard.className = 'status-item';
    if (state.phase === 'scraping' || state.phase === 'filtering' || state.phase === 'generating') {
        statusCard.classList.add('running');
    } else if (state.phase === 'complete') {
        statusCard.classList.add('complete');
    } else if (state.phase === 'error') {
        statusCard.classList.add('error');
    }
    
    // Update stats
    document.getElementById('totalLeads').textContent = state.leads?.length || 0;
    
    // Update progress
    if (state.is_running || state.phase === 'complete') {
        const progressFill = document.getElementById('progressFill');
        const progressText = document.getElementById('progressText');
        const phaseBadge = document.getElementById('phaseBadge');
        const currentLead = document.getElementById('currentLead');
        
        const percentage = state.total > 0 ? (state.progress / state.total * 100) : 0;
        progressFill.style.width = `${percentage}%`;
        progressText.textContent = `${state.progress} / ${state.total}`;
        
        phaseBadge.textContent = state.phase;
        phaseBadge.className = `phase-badge ${state.phase}`;
        
        currentLead.textContent = state.message || state.current_lead || '-';
    }
    
    // Update button state
    if (state.is_running) {
        setButtonState('running');
    } else if (state.phase !== 'idle') {
        setButtonState('idle');
    }
    
    // Update logs
    if (state.logs && state.logs.length > 0) {
        updateLogs(state.logs);
    }
    
    // Update results if complete
    if (state.leads && state.leads.length > 0 && currentResults.length !== state.leads.length) {
        currentResults = state.leads;
        updateResultsTable(state.leads);
    }
}

function stripRichMarkup(text) {
    // Remove Rich console markup like [bold], [/bold], [green], [dim], etc.
    // Pattern: [tag] or [/tag] or [tag=style]
    return text.replace(/\[\/?[a-zA-Z0-9_\-]+(?:=[^\]]+)?\]/g, '');
}

function cleanLogText(log) {
    // Strip Rich markup, then escape HTML
    return escapeHtml(stripRichMarkup(log));
}

function updateLogs(logs) {
    const logsTerminal = document.getElementById('logsTerminal');
    const dashboardLogs = document.getElementById('dashboardLogs');
    
    // Terminal logs
    logsTerminal.innerHTML = logs.map(log => {
        const cleanLog = stripRichMarkup(log);
        const level = cleanLog.includes('Error') ? 'error' : 
                      cleanLog.includes('Started') || cleanLog.includes('Complete') ? 'success' :
                      cleanLog.includes('Stop') ? 'warning' : 'info';
        return `<div class="log-line log-${level}">${escapeHtml(cleanLog)}</div>`;
    }).join('');
    
    // Auto-scroll
    logsTerminal.scrollTop = logsTerminal.scrollHeight;
    
    // Dashboard preview (last 5)
    if (dashboardLogs) {
        const recentLogs = logs.slice(-5);
        dashboardLogs.innerHTML = recentLogs.map(log => 
            `<div class="log-line log-info">${escapeHtml(stripRichMarkup(log))}</div>`
        ).join('');
    }
}

function updateResultsTable(leads) {
    const tbody = document.getElementById('resultsBody');
    const noResults = document.getElementById('noResults');
    
    if (leads.length === 0) {
        tbody.innerHTML = '';
        noResults.style.display = 'block';
        return;
    }
    
    noResults.style.display = 'none';
    
    tbody.innerHTML = leads.map((lead, idx) => `
        <tr data-search="${(lead.company_name + ' ' + lead.city + ' ' + lead.phone + ' ' + lead.business_type).toLowerCase()}">
            <td>${idx + 1}</td>
            <td class="company-cell">${escapeHtml(lead.company_name)}</td>
            <td>${escapeHtml(lead.city)}, ${escapeHtml(lead.country)}</td>
            <td><a href="https://wa.me/${lead.phone.replace(/\D/g, '')}" class="phone-link" target="_blank">${escapeHtml(lead.phone)}</a></td>
            <td>${escapeHtml(lead.business_type)}</td>
            <td><span class="rating">${lead.rating !== 'N/A' ? '★ ' + lead.rating : '-'}</span></td>
            <td>
                <a href="https://wa.me/${lead.phone.replace(/\D/g, '')}" target="_blank" class="btn btn-sm btn-primary">
                    Chat
                </a>
            </td>
        </tr>
    `).join('');
}

function filterResults() {
    const query = document.getElementById('searchResults').value.toLowerCase();
    const rows = document.querySelectorAll('#resultsBody tr');
    
    rows.forEach(row => {
        const searchText = row.dataset.search || '';
        row.style.display = searchText.includes(query) ? '' : 'none';
    });
}

// Downloads
async function downloadResults(format) {
    try {
        const response = await fetch(`${API_BASE}/api/download/${format}`);
        
        if (!response.ok) {
            const err = await response.json();
            throw new Error(err.detail || 'Download failed');
        }
        
        if (format === 'json') {
            const data = await response.json();
            const blob = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' });
            downloadBlob(blob, 'openlead_results.json');
        } else if (format === 'csv') {
            const text = await response.text();
            const blob = new Blob([text], { type: 'text/csv' });
            downloadBlob(blob, 'openlead_results.csv');
        } else if (format === 'html') {
            const blob = await response.blob();
            downloadBlob(blob, 'openlead_results.html');
        }
        
        addLog('success', `Downloaded results as ${format.toUpperCase()}`);
    } catch (err) {
        alert(err.message);
    }
}

function downloadBlob(blob, filename) {
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = filename;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
}

// Utilities
function escapeHtml(text) {
    if (!text) return '';
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

function addLog(level, message) {
    const logsTerminal = document.getElementById('logsTerminal');
    const line = document.createElement('div');
    line.className = `log-line log-${level}`;
    line.textContent = `[${new Date().toLocaleTimeString()}] ${message}`;
    logsTerminal.appendChild(line);
    logsTerminal.scrollTop = logsTerminal.scrollHeight;
}

function clearLogs() {
    document.getElementById('logsTerminal').innerHTML = '<div class="log-line log-info">Logs cleared.</div>';
}

async function refreshLogs() {
    await refreshStatus();
}

async function refreshStatus() {
    try {
        const response = await fetch(`${API_BASE}/api/status`);
        const state = await response.json();
        updateUI(state);
    } catch (err) {
        console.error('Refresh error:', err);
    }
}

async function loadResults() {
    try {
        const response = await fetch(`${API_BASE}/api/results`);
        const data = await response.json();
        if (data.leads) {
            currentResults = data.leads;
            updateResultsTable(data.leads);
        }
    } catch (err) {
        console.error('Load results error:', err);
    }
}

// Periodic refresh for non-WebSocket updates
setInterval(() => {
    if (!ws || ws.readyState !== WebSocket.OPEN) {
        refreshStatus();
    }
}, 5000);

// Initial results load
loadResults();
