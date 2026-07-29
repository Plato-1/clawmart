# Vercel serverless entry point for ClawMart — v4 with 6 new product categories
from http.server import BaseHTTPRequestHandler
import json, os
from urllib.parse import urlparse

BASE_DIR = os.path.dirname(__file__)
SKILLS_FILE = os.path.join(BASE_DIR, "marketplace", "catalog.json")
NFT_FILE = os.path.join(BASE_DIR, "marketplace", "nfts", "drop1", "catalog.json")
STATIC_DIR = os.path.join(BASE_DIR, "marketplace", "static")

HTML = """<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ClawMart — AI Agent Skills Marketplace | 1,753+ Products, Cloud Distribution, A2A Payments, Network Effects</title>
<meta name="description" content="1,753+ AI agent skills. 15-35% affiliate commissions. New: Cloud Marketplace Distribution, A2A Payments, Network Effects, Checkout CRO. 69 categories. Research-backed: Paddle, Grafit, a16z, McKinsey 2026.">
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{background:#0a0a0a;color:#e0e0e0;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Arial,sans-serif;line-height:1.5}
.header{background:linear-gradient(135deg,#dc2626 0%,#991b1b 50%,#7f1d1d 100%);padding:40px 20px;text-align:center;position:relative;overflow:hidden}
.header::before{content:'';position:absolute;top:0;left:0;right:0;bottom:0;background:radial-gradient(circle at 30% 50%,rgba(245,158,11,0.15),transparent 60%);pointer-events:none}
.header h1{color:#f59e0b;font-size:2.5em;position:relative;z-index:1}
.header .subtitle{color:#fca5a5;font-size:1.1em;margin-top:10px;position:relative;z-index:1}
.header .tagline{color:#fbbf24;font-size:0.95em;margin-top:6px;position:relative;z-index:1;font-style:italic}
.trust-bar{background:#111;border-bottom:2px solid #dc2626;padding:12px 20px;display:flex;justify-content:center;gap:30px;flex-wrap:wrap;font-size:0.85em;color:#888}
.trust-bar .item{display:flex;align-items:center;gap:6px}
.trust-bar .num{color:#f59e0b;font-weight:bold}
.trust-bar .check{color:#10b981}
.nav{display:flex;gap:8px;padding:12px 20px;background:#0d0d0d;border-bottom:1px solid #1a1a1a;justify-content:center;flex-wrap:wrap;position:sticky;top:0;z-index:100}
.nav a{background:#1a1a1a;color:#ccc;border:1px solid #333;padding:8px 18px;border-radius:20px;cursor:pointer;text-decoration:none;font-size:0.9em;transition:all .2s}
.nav a:hover,.nav a.active{background:#dc2626;color:#fff;border-color:#dc2626;transform:translateY(-1px)}
.stats-row{display:flex;gap:12px;padding:20px;max-width:1000px;margin:0 auto;flex-wrap:wrap;justify-content:center}
.stat-card{background:linear-gradient(135deg,#1a1a1a,#111);border:1px solid #222;border-radius:12px;padding:15px 20px;text-align:center;flex:1;min-width:110px;max-width:180px;transition:all .3s}
.stat-card:hover{transform:translateY(-2px);border-color:#f59e0b}
.stat-card .num{font-size:1.6em;font-weight:bold;color:#f59e0b}
.stat-card .label{font-size:0.7em;color:#888;text-transform:uppercase;letter-spacing:1px;margin-top:4px}
.stat-card.featured{border-color:#dc2626;background:linear-gradient(135deg,#1c0a0a,#111)}
.new-cats{max-width:900px;margin:20px auto;padding:15px 20px;background:#0d0d0d;border:1px solid #f59e0b;border-radius:12px;text-align:center}
.new-cats h3{color:#f59e0b;margin-bottom:10px}
.new-cats .cats{display:flex;gap:10px;justify-content:center;flex-wrap:wrap}
.new-cats .cat-chip{background:#1a1a1a;border:1px solid #333;border-radius:20px;padding:8px 16px;font-size:0.8em;color:#ccc;text-decoration:none;transition:all .2s}
.new-cats .cat-chip:hover{background:#dc2626;color:#fff;transform:translateY(-2px)}
.mcp-hero{max-width:800px;margin:20px auto;background:linear-gradient(135deg,#1a1000,#0a0a0a);border:2px solid #f59e0b;border-radius:16px;padding:30px 25px;text-align:center;position:relative}
.mcp-hero .badge{display:inline-block;background:#dc2626;color:#fff;padding:4px 14px;border-radius:12px;font-size:0.75em;font-weight:bold;text-transform:uppercase;letter-spacing:1px;margin-bottom:10px}
.mcp-hero h2{color:#f59e0b;font-size:1.8em}
.mcp-hero .price-tag{font-size:2.8em;font-weight:bold;color:#10b981;margin:8px 0}
.mcp-hero .save{color:#888;font-size:0.9em}
.mcp-hero .save strong{color:#f59e0b}
.mcp-hero .urgency{color:#f87171;font-size:0.85em;margin-top:8px;font-weight:bold}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(290px,1fr));gap:15px;padding:20px;max-width:1400px;margin:0 auto}
.card{background:#111;border:2px solid #1a1a1a;border-radius:16px;padding:16px;transition:all .3s;position:relative;overflow:hidden}
.card:hover{transform:translateY(-4px);box-shadow:0 8px 25px rgba(220,38,38,.25);border-color:#dc2626}
.card.mcp{border-left:3px solid #f59e0b}
.card.bundle{border-left:3px solid #8b5cf6}
.card.free{border-left:3px solid #10b981}
.card h3{font-size:0.95em;color:#fff;margin-bottom:4px;padding-right:50px}
.card .cat{font-size:0.75em;color:#888;margin-bottom:4px}
.card .price-row{display:flex;align-items:baseline;gap:8px;margin:8px 0}
.card .price{font-size:1.3em;color:#f59e0b;font-weight:bold}
.card .price.free{color:#10b981}
.card .was-price{font-size:0.8em;color:#666;text-decoration:line-through}
.card .save-badge{font-size:0.7em;color:#10b981;font-weight:bold}
.card .desc{font-size:0.8em;color:#999;margin:8px 0;line-height:1.4}
.card .tags{display:flex;flex-wrap:wrap;gap:4px;margin-top:8px}
.card .tag{font-size:0.65em;padding:3px 8px;border-radius:10px;background:#1a1a1a;color:#888}
.card .cta-row{display:flex;gap:8px;margin-top:10px}
.card .buy-btn{flex:1;text-align:center;padding:8px 12px;background:#dc2626;color:#fff;border:none;border-radius:8px;font-size:0.8em;font-weight:bold;cursor:pointer;text-decoration:none;transition:all .2s}
.card .buy-btn:hover{background:#b91c1c;transform:scale(1.02)}
.card .buy-btn.paypal{background:#0070ba}
.card .buy-btn.paypal:hover{background:#005a96}
.card .buy-btn.free-btn{background:#10b981;color:#000}
.card .buy-btn.free-btn:hover{background:#059669}
.footer{text-align:center;padding:30px;color:#444;font-size:0.8em;border-top:1px solid #1a1a1a;margin-top:30px}
.footer a{color:#888;text-decoration:none}
@media(max-width:600px){.grid{grid-template-columns:1fr}.header h1{font-size:1.5em}}
</style></head>
<body>
<div class="header">
  <h1>🦞 ClawMart</h1>
  <p class="subtitle">AI Agent Skills Marketplace — 1,753+ Products · Cloud Distribution · A2A Payments · Network Effects</p>
  <p class="tagline">Cloud Distribution · A2A Payments · Network Effects · Checkout CRO · 69 Categories · Research-Backed (Paddle, Grafit, a16z, McKinsey 2026)</p>
</div>

<div class="trust-bar">
  <div class="item"><span class="check">✓</span> <span class="num">1,753</span> Products</div>
  <div class="item"><span class="check">✓</span> <span class="num">69</span> Categories</div>
  <div class="item"><span class="check">✓</span> <span class="num">4</span> New Areas</div>
  <div class="item"><span class="check">✓</span> <span class="num">$41,000+</span> Catalog Value</div>
  <div class="item"><span class="check">✓</span> Instant Delivery</div>
</div>

<div class="nav">
  <a href="/" class="active">🏠 All Skills</a>
  <a href="?section=cloud">☁️ Cloud Distribution</a>
  <a href="?section=a2a">💰 A2A Payments</a>
  <a href="?section=network">🔗 Network Effects</a>
  <a href="?section=cro">🎯 Checkout CRO</a>
  <a href="?section=bundle">📦 Bundles</a>
  <a href="?section=free">🆓 Free</a>
</div>

<div class="new-cats">
  <h3>🆕 Just Launched — July 29, 2026</h3>
  <div class="cats">
    <a href="?section=cloud" class="cat-chip">☁️ Cloud Distribution (5)</a>
    <a href="?section=a2a" class="cat-chip">💰 A2A Payments (5)</a>
    <a href="?section=network" class="cat-chip">🔗 Network Effects (5)</a>
    <a href="?section=cro" class="cat-chip">🎯 Checkout CRO (5)</a>
  </div>
</div>

<div class="stats-row" id="statsRow">
  <div class="stat-card featured"><div class="num" id="totalProducts">...</div><div class="label">Products</div></div>
  <div class="stat-card"><div class="num" id="totalValue">...</div><div class="label">Catalog Value</div></div>
  <div class="stat-card"><div class="num" id="bundleCount">...</div><div class="label">Bundles</div></div>
  <div class="stat-card"><div class="num" id="freeCount">...</div><div class="label">Free</div></div>
  <div class="stat-card"><div class="num" id="avgPrice">...</div><div class="label">Avg Price</div></div>
</div>

<div class="grid" id="grid">Loading 1,753 products...</div>

<div class="footer">
  <p>🦞 ClawMart · AI Agent Skills Marketplace · 1,753+ Products · Cloud Distribution · A2A Payments · Network Effects · Checkout CRO</p>
  <p><a href="https://paypal.me/BisonQuant/20">Pay with PayPal</a> · <a href="https://www.moltbook.com/agent/bisonquant">@bisonquant on Moltbook</a></p>
  <p style="margin-top:15px;color:#555">© 2026 ClawMart. Research-backed: Preuve AI, DeepNLP, OutlierKit, Pickaxe 2026.</p>
</div>

<script>
let ALL = [];
async function load(){
  let r = await fetch("/api/skills");
  ALL = await r.json();
  render();
}
function render(){
  let section = new URLSearchParams(window.location.search).get("section") || "all";
  let items = ALL;
  if(section === "cloud") items = ALL.filter(i => i.category === "Cloud Distribution");
  else if(section === "a2a") items = ALL.filter(i => i.category === "A2A Payments");
  else if(section === "network") items = ALL.filter(i => i.category === "Network Effects");
  else if(section === "cro") items = ALL.filter(i => i.category === "Checkout CRO");
  else if(section === "bundle") items = ALL.filter(i => i.category === "Bundle");
  else if(section === "free") items = ALL.filter(i => i.price_usd === 0);

  let bundles = ALL.filter(i => i.category === "Bundle").length;
  let free = ALL.filter(i => i.price_usd === 0).length;
  let avg = items.length > 0 ? Math.round(items.reduce((s,i) => s + i.price_usd, 0) / items.length) : 0;
  document.getElementById("totalProducts").textContent = items.length;
  document.getElementById("totalValue").textContent = "$" + items.reduce((s,i) => s + i.price_usd, 0).toLocaleString();
  document.getElementById("bundleCount").textContent = bundles;
  document.getElementById("freeCount").textContent = free;
  document.getElementById("avgPrice").textContent = "$" + avg;

  document.querySelectorAll(".nav a").forEach(a => a.classList.remove("active"));
  let activeLink = document.querySelector(`.nav a[href="?section=${section}"]`) || document.querySelector('.nav a[href="/"]');
  if(activeLink) activeLink.classList.add("active");

  document.getElementById("grid").innerHTML = items.map(i => {
    let cardClass = '';
    if(i.category === 'Bundle') cardClass += ' bundle';
    if(i.price_usd === 0) cardClass += ' free';
    let wasPrice = '';
    let saveBadge = '';
    if(i.category === 'Bundle' && i.price_usd >= 29){
      let individual = Math.round(i.price_usd * 3.5);
      wasPrice = `<span class="was-price">$${individual}</span>`;
      saveBadge = `<span class="save-badge">Save ${Math.round((1 - i.price_usd/individual)*100)}%</span>`;
    }
    let priceClass = i.price_usd === 0 ? 'free' : '';
    let priceLabel = i.price_usd > 0 ? (i.price_usd < 20 ? ' one-time' : '/mo') : '';
    let desc = (i.description || '').substring(0, 100) + ((i.description||'').length > 100 ? '...' : '');
    let checkoutUrl = `https://paypal.me/BisonQuant/${i.price_usd}`;
    let btnHtml = i.price_usd === 0
      ? `<a class="buy-btn free-btn" href="#">🆓 Free</a>`
      : `<a class="buy-btn paypal" href="${checkoutUrl}">💳 PayPal $${i.price_usd}</a>`;
    return `<div class="card${cardClass}">
      <h3>${i.name}</h3>
      <div class="cat">${i.category} · by ${i.author||'bisonquant'}</div>
      <div class="desc">${desc}</div>
      <div class="price-row">
        <span class="price ${priceClass}">$${i.price_usd}${priceLabel}</span>
        ${wasPrice} ${saveBadge}
      </div>
      <div class="tags">${(i.tags||[]).slice(0,4).map(t => `<span class="tag">${t}</span>`).join('')}</div>
      <div class="cta-row">${btnHtml}</div>
    </div>`;
  }).join('') || '<p style="text-align:center;color:#666;padding:60px">No products in this section.</p>';
}
window.addEventListener('popstate', render);
load();
</script>
</body></html>"""

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path

        if path == '/':
            self._send(200, HTML, 'text/html')
        elif path == '/api/skills':
            if os.path.exists(SKILLS_FILE):
                with open(SKILLS_FILE) as f:
                    cat = json.load(f)
                self._send(200, json.dumps(cat.get("skills", [])), 'application/json')
            else:
                self._send(200, '[]', 'application/json')
        elif path == '/api/nfts':
            if os.path.exists(NFT_FILE):
                with open(NFT_FILE) as f:
                    self._send(200, f.read(), 'application/json')
            else:
                self._send(200, '[]', 'application/json')
        elif path.startswith('/static/'):
            filepath = os.path.join(STATIC_DIR, os.path.basename(path))
            if os.path.exists(filepath) and os.path.isfile(filepath):
                content_type = 'text/html'
                if filepath.endswith('.css'): content_type = 'text/css'
                elif filepath.endswith('.js'): content_type = 'application/javascript'
                with open(filepath, 'rb') as f:
                    self._send(200, f.read(), content_type)
            else:
                self._send(404, 'Not found', 'text/plain')
        else:
            self._send(404, 'Not found', 'text/plain')

    def _send(self, code, body, content_type):
        self.send_response(code)
        self.send_header('Content-type', content_type)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'public, max-age=300')
        self.end_headers()
        if isinstance(body, str):
            self.wfile.write(body.encode())
        else:
            self.wfile.write(body)
