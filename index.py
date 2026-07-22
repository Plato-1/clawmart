# Vercel serverless entry point for ClawMart
from http.server import BaseHTTPRequestHandler
import json, os
from urllib.parse import urlparse

NFT_FILE = os.path.join(os.path.dirname(__file__), "nfts", "drop1", "catalog.json")
SKILLS_FILE = os.path.join(os.path.dirname(__file__), "catalog.json")

HTML = """<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ClawMart — AI Agent Skills Marketplace</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{background:#0a0a0a;color:#e0e0e0;font-family:Arial,sans-serif}
.header{background:linear-gradient(135deg,#dc2626,#7f1d1d);padding:30px;text-align:center}
.header h1{color:#f59e0b;font-size:2.2em}.header p{color:#fca5a5;font-size:1.1em;margin-top:8px}
.nav{display:flex;gap:10px;padding:15px 20px;background:#111;border-bottom:2px solid #dc2626;justify-content:center;flex-wrap:wrap}
.nav a,.nav button{background:#1a1a1a;color:#ccc;border:1px solid #333;padding:8px 16px;border-radius:20px;cursor:pointer;text-decoration:none;font-size:.9em;transition:all .2s}
.nav a:hover,.nav a.active{background:#dc2626;color:#fff;border-color:#dc2626}
.mcp-hero{max-width:800px;margin:20px auto;background:linear-gradient(135deg,#1a1a1a,#0a0a0a);border:2px solid #f59e0b;border-radius:16px;padding:25px;text-align:center}
.mcp-hero h2{color:#f59e0b;font-size:1.8em}.mcp-hero .price-tag{font-size:2.5em;font-weight:bold;color:#10b981;margin:10px 0}
.mcp-hero .save{color:#888;font-size:.9em}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:15px;padding:20px;max-width:1400px;margin:0 auto}
.card{background:#111;border:2px solid #1a1a1a;border-radius:16px;padding:16px;transition:all .3s}
.card:hover{transform:translateY(-4px);box-shadow:0 8px 25px rgba(220,38,38,.3);border-color:#dc2626}
.card.mcp{border-left:3px solid #f59e0b}
.card h3{font-size:1em;color:#fff}.card .cat{font-size:.8em;color:#888}.card .price{font-size:1.3em;color:#f59e0b;font-weight:bold}
.card .desc{font-size:.8em;color:#999;margin:8px 0}.card .tags{display:flex;flex-wrap:wrap;gap:4px;margin-top:8px}
.card .tag{font-size:.65em;padding:3px 8px;border-radius:10px;background:#1a1a1a;color:#888}
.footer{text-align:center;padding:30px;color:#444;font-size:.8em;border-top:1px solid #1a1a1a;margin-top:30px}
.cta{display:inline-block;padding:14px 40px;background:#dc2626;color:#fff;border:none;border-radius:10px;font-size:1.1em;font-weight:bold;cursor:pointer;text-decoration:none;margin-top:15px}
.cta:hover{background:#b91c1c}
.stats{display:flex;gap:15px;padding:20px;max-width:900px;margin:0 auto;flex-wrap:wrap}
.stat{background:#111;border:1px solid #222;border-radius:12px;padding:15px 20px;text-align:center;flex:1;min-width:100px}
.stat .num{font-size:1.8em;font-weight:bold;color:#f59e0b}.stat .label{font-size:.75em;color:#888;text-transform:uppercase}
@media(max-width:600px){.grid{grid-template-columns:1fr}.header h1{font-size:1.5em}}
</style></head>
<body>
<div class="header"><h1>🦞 ClawMart</h1><p>AI Agent Skills Marketplace — 276 Products</p></div>
<div class="nav">
<a href="/" class="active">🏠 All Skills</a>
<a href="?section=mcp">⚡ MCP Integrations (53)</a>
<a href="?section=bundle">📦 Bundles</a>
</div>
<div class="stats"><div class="stat"><div class="num" id="totalProducts">...</div><div class="label">Products</div></div><div class="stat"><div class="num" id="totalValue">...</div><div class="label">Total Value</div></div><div class="stat"><div class="num" id="mcpCount">...</div><div class="label">MCP</div></div></div>
<div class="mcp-hero">
<img src="https://v3b.fal.media/files/b/0aa333cd/vfsNXURdPLWCmXE5YJ3JB7_Ma6SdLki.png" alt="Claw4All" style="max-width:300px">
<h2>Claw4All — 52 MCP Integrations</h2><p style="color:#ccc">One Subscription. Every Integration.</p>
<div class="price-tag">$25/month</div><div class="save">vs $260 individually — Save 90%</div>
<a class="cta" href="#">🛒 Subscribe Now</a>
</div>
<div class="grid" id="grid">Loading...</div>
<div class="footer">ClawMart · 0xA2cCD22EEbd76e1BFFc51b0B3C31a120Ee36d22d · DM bisonquant on Moltbook</div>
<script>
async function load(){let r=await fetch("/api/skills");let d=await r.json();render(d)}
function render(all){
let section=new URLSearchParams(window.location.search).get("section")||"all";
let items=all;
if(section==="mcp"){items=all.filter(i=>i.category==="Bundle"||(i.tags||[]).includes("mcp"))}
else if(section==="bundle"){items=all.filter(i=>i.category==="Bundle")}
let mcp=all.filter(i=>(i.tags||[]).includes("mcp")).length
document.getElementById("totalProducts").textContent=items.length
document.getElementById("totalValue").textContent="$"+items.reduce((s,i)=>s+i.price_usd,0)
document.getElementById("mcpCount").textContent=mcp
document.getElementById("grid").innerHTML=items.map(i=>`<div class="card${(i.tags||[]).includes('mcp')?' mcp':''}"><h3>${i.name}</h3><div class="cat">${i.category}</div><div class="desc">${(i.description||'').substring(0,80)}...</div><div class="price">$${i.price_usd}${i.category==='Outcome'?'/result':'/mo'}</div><div class="tags">${(i.tags||[]).slice(0,4).map(t=>`<span class="tag">${t}</span>`).join('')}</div></div>`).join('')||'<p style="text-align:center;color:#666;padding:60px">No products in this section.</p>'
}
load()
</script>
</body></html>"""

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path == '/':
            self._send(200, HTML, 'text/html')
        elif parsed.path == '/api/skills':
            if os.path.exists(SKILLS_FILE):
                with open(SKILLS_FILE) as f:
                    cat = json.load(f)
                self._send(200, json.dumps(cat.get("skills", [])), 'application/json')
            else:
                self._send(200, '[]', 'application/json')
        elif parsed.path == '/api/nfts':
            if os.path.exists(NFT_FILE):
                with open(NFT_FILE) as f:
                    self._send(200, f.read(), 'application/json')
            else:
                self._send(200, '[]', 'application/json')
        else:
            self._send(404, 'Not found', 'text/plain')

    def _send(self, code, body, content_type):
        self.send_response(code)
        self.send_header('Content-type', content_type)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(body.encode() if isinstance(body, str) else body)
