#!/usr/bin/env python3
"""ClawMart v2 — NFTs + MCP Skills Marketplace with dedicated MCP section."""
import json, os, http.server, socketserver, webbrowser
from urllib.parse import urlparse

NFT_FILE = os.path.expandvars(r"${HOME}\trading_bot\monetization\marketplace\nfts\drop1\catalog.json")
SKILLS_FILE = os.path.expandvars(r"${HOME}\trading_bot\monetization\marketplace\catalog.json")
PORT = 8888

def load_nfts():
    with open(NFT_FILE) as f: return json.load(f)
def load_skills():
    if os.path.exists(SKILLS_FILE):
        with open(SKILLS_FILE) as f: return json.load(f).get("skills", [])
    return []
def load_catalog():
    return json.load(open(SKILLS_FILE))

HTML = r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>ClawMart — AI Agent Skills Marketplace</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{background:#0a0a0a;color:#e0e0e0;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Arial,sans-serif}
.header{background:linear-gradient(135deg,#dc2626,#7f1d1d);padding:30px 20px;text-align:center;position:sticky;top:0;z-index:100}
.header h1{color:#f59e0b;font-size:2.2em;margin:0}
.header p{color:#fca5a5;font-size:1.1em;margin:8px 0 0}
.nav{display:flex;gap:10px;padding:15px 20px;background:#111;border-bottom:2px solid #dc2626;overflow-x:auto;flex-wrap:wrap;justify-content:center}
.nav button{background:#1a1a1a;color:#ccc;border:1px solid #333;padding:8px 16px;border-radius:20px;cursor:pointer;font-size:.9em;transition:all .2s;white-space:nowrap}
.nav button:hover,.nav button.active{background:#dc2626;color:#fff;border-color:#dc2626}
.nav .mcp-tab{background:#1a1a1a;border:2px solid #f59e0b}
.nav .mcp-tab:hover,.nav .mcp-tab.active{background:#f59e0b;color:#000}
.search-bar{padding:15px 20px;display:flex;gap:10px;max-width:900px;margin:0 auto}
.search-bar input{flex:1;padding:12px 16px;border-radius:25px;border:1px solid #333;background:#1a1a1a;color:#fff;font-size:1em}
.search-bar input::placeholder{color:#666}
.search-bar select{padding:12px;border-radius:25px;border:1px solid #333;background:#1a1a1a;color:#fff;font-size:.9em}
.stats{display:flex;gap:15px;padding:0 20px 15px;max-width:900px;margin:0 auto;flex-wrap:wrap}
.stats .stat{background:#111;border:1px solid #222;border-radius:12px;padding:15px 20px;text-align:center;flex:1;min-width:100px}
.stats .stat .num{font-size:1.8em;font-weight:bold;color:#f59e0b}
.stats .stat .label{font-size:.75em;color:#888;text-transform:uppercase;letter-spacing:1px}
.mcp-hero{max-width:900px;margin:15px auto;background:linear-gradient(135deg,#1a1a1a,#0a0a0a);border:2px solid #f59e0b;border-radius:16px;padding:25px;text-align:center}
.mcp-hero img{max-width:400px;height:auto;margin-bottom:15px}
.mcp-hero h2{color:#f59e0b;font-size:1.8em;margin-bottom:8px}
.mcp-hero .price-tag{font-size:2.5em;font-weight:bold;color:#10b981;margin:10px 0}
.mcp-hero .save{color:#888;font-size:.9em}
.mcp-hero .cta{display:inline-block;margin-top:15px;padding:14px 40px;background:#dc2626;color:#fff;border:none;border-radius:10px;font-size:1.1em;font-weight:bold;cursor:pointer;text-decoration:none}
.mcp-hero .cta:hover{background:#b91c1c}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:15px;padding:20px;max-width:1400px;margin:0 auto}
.card{background:#111;border:2px solid #1a1a1a;border-radius:16px;padding:16px;transition:all .3s;cursor:pointer}
.card:hover{transform:translateY(-4px);box-shadow:0 8px 25px rgba(220,38,38,.3);border-color:#dc2626}
.card.mcp{border-left:3px solid #f59e0b}
.card h3{font-size:1em;color:#fff;margin-bottom:6px}
.card .cat{font-size:.8em;color:#888;margin-bottom:6px}
.card .price{font-size:1.3em;font-weight:bold;color:#f59e0b}
.card .desc{font-size:.8em;color:#999;margin:8px 0;line-height:1.4}
.card .tags{display:flex;flex-wrap:wrap;gap:4px;margin-top:8px}
.card .tag{font-size:.65em;padding:3px 8px;border-radius:10px;background:#1a1a1a;color:#888}
.mint-modal{display:none;position:fixed;top:0;left:0;right:0;bottom:0;background:rgba(0,0,0,.85);z-index:200;align-items:center;justify-content:center}
.mint-modal.active{display:flex}
.modal-content{background:#111;border:2px solid #dc2626;border-radius:20px;padding:30px;max-width:450px;width:90%}
.modal-content h2{color:#f59e0b;margin-bottom:10px}
.modal-content .info{color:#ccc;margin-bottom:8px;line-height:1.6}
.modal-content .eth-address{background:#000;border:1px solid #333;padding:12px;border-radius:8px;font-family:monospace;color:#f59e0b;word-break:break-all;margin:15px 0;font-size:.85em}
.modal-content .close-btn{display:block;width:100%;padding:12px;background:#333;color:#fff;border:none;border-radius:8px;cursor:pointer;margin-top:10px}
.footer{text-align:center;padding:30px;color:#444;font-size:.8em;border-top:1px solid #1a1a1a;margin-top:30px}
</style>
</head>
<body>
<div class="header"><h1>🦞 ClawMart</h1><p>AI Agent Skills Marketplace — NFTs + MCP Integrations</p></div>
<div class="nav" id="nav">
<button class="active" data-section="nfts">🏠 NFT Drop #1</button>
<button class="mcp-tab" data-section="mcp">⚡ MCP Integrations</button>
<button data-section="all-skills">🛠 All Skills (169)</button>
</div>
<div class="search-bar">
<input type="text" id="search" placeholder="Search..." oninput="render()">
<select id="sort" onchange="render()">
<option value="default">Sort: Default</option>
<option value="price_asc">Price Low→High</option>
<option value="price_desc">Price High→Low</option>
</select>
</div>
<div class="mcp-hero" id="mcpHero" style="display:none">
<img src="https://v3b.fal.media/files/b/0aa333cd/vfsNXURdPLWCmXE5YJ3JB7_Ma6SdLki.png" alt="Claw4All" style="max-width:350px">
<h2>Claw4All — 52 MCP Integrations</h2>
<p style="color:#ccc">One Subscription. Every Integration.</p>
<div class="price-tag">$25/month</div>
<div class="save">vs $260 individually — Save 90%</div>
<a class="cta" onclick="showMint('Claw4All Bundle','legendary',25,'ALL','All MCP Categories')">🛒 Subscribe Now</a>
</div>
<div class="stats" id="stats"></div>
<div class="grid" id="grid"></div>
<div class="footer">ClawMart · 0xA2cCD22EEbd76e1BFFc51b0B3C31a120Ee36d22d · DM bisonquant on Moltbook<br>All NFTs are collectible parodies. Not financial advice.</div>
<div class="mint-modal" id="mintModal" onclick="closeModal(event)"><div class="modal-content" onclick="event.stopPropagation()"><h2 id="modalTitle"></h2><div class="info" id="modalInfo"></div><div class="eth-address">0xA2cCD22EEbd76e1BFFc51b0B3C31a120Ee36d22d</div><p style="color:#888;font-size:.85em">Send ETH/USDT/USDC. DM bisonquant with tx hash to receive your product.</p><button class="close-btn" onclick="closeModal()">Close</button></div></div>
<script>
let allNfts=[],allSkills=[],currentSection="nfts",search="",sortBy="default";
async function load(){try{let r=await fetch("/api/nfts");allNfts=await r.json();r=await fetch("/api/skills");allSkills=await r.json();buildNav();render()}catch(e){console.error(e)}}
function buildNav(){document.querySelectorAll(".nav button").forEach(b=>{b.classList.remove("active");if(b.dataset.section===currentSection)b.classList.add("active")});document.getElementById("mcpHero").style.display=currentSection==="mcp"?"block":"none"}
function switchSection(section){currentSection=section;buildNav();render()}
document.querySelectorAll(".nav button").forEach(b=>{b.addEventListener("click",()=>switchSection(b.dataset.section))});
function render(){
search=document.getElementById("search").value.toLowerCase();sortBy=document.getElementById("sort").value;
let items=[];
if(currentSection==="nfts"){
items=allNfts;
if(search)items=items.filter(i=>i.name.toLowerCase().includes(search)||i.rarity.toLowerCase().includes(search));
if(sortBy==="price_asc")items.sort((a,b)=>a.price_eth-b.price_eth);
if(sortBy==="price_desc")items.sort((a,b)=>b.price_eth-a.price_eth);
document.getElementById("stats").innerHTML='<div class="stat"><div class="num">'+items.length+'</div><div class="label">NFTs</div></div><div class="stat"><div class="num">'+items.filter(i=>!i.minted).length+'</div><div class="label">Available</div></div>';
let h="";
items.forEach(i=>{
h+='<div class="card '+i.rarity+'" onclick="showMint(\''+i.name+'\',\''+i.rarity+'\','+i.price_eth+',\''+i.edition_number+'\',\''+(i.category_name||"")+'\')"><h3>#'+i.edition_number+' — '+i.name+'</h3><div class="cat">'+i.category_name+'</div><div class="price">'+i.price_eth.toFixed(2)+' ETH</div><button class="cta" style="width:100%;margin-top:10px">🛒 Buy</button></div>';
});
document.getElementById("grid").innerHTML=h||'<div style="text-align:center;padding:60px;color:#666"><h2>No NFTs found</h2></div>';
}else{
items=allSkills;
if(currentSection==="mcp")items=items.filter(i=>i.category==="Bundle"||(i.tags||[]).some(t=>t==="mcp"));
if(search)items=items.filter(i=>i.name.toLowerCase().includes(search)||i.description.toLowerCase().includes(search)||(i.tags||[]).some(t=>t.toLowerCase().includes(search)));
if(sortBy==="price_asc")items.sort((a,b)=>a.price_usd-b.price_usd);
if(sortBy==="price_desc")items.sort((a,b)=>b.price_usd-a.price_usd);
let total=items.reduce((s,i)=>s+i.price_usd,0);
let mcpCount=items.filter(i=>i.category!=="Bundle").length;
document.getElementById("stats").innerHTML='<div class="stat"><div class="num">'+items.length+'</div><div class="label">Products</div><div class="stat"><div class="num">'+mcpCount+'</div><div class="label">MCP</div><div class="stat"><div class="num">$'+total+'</div><div class="label">Value</div>';
let h="";
items.forEach(i=>{
let isMcp=(i.tags||[]).some(t=>t==="mcp");
let isBundle=i.category==="Bundle";
h+='<div class="card'+(isMcp?" mcp":"")+'" onclick="showMint(\''+i.name.replace(/'/g,"\\'")+'\',\''+(isBundle?"MYTHIC":"common")+'\','+i.price_usd+',\''+(i.author||"bisonquant")+'\',\''+i.category+'\')"><h3>'+i.name+'</h3><div class="cat">'+i.category+'</div><div class="desc">'+(i.description||"").substring(0,100)+'...</div><div class="price">$'+i.price_usd+'/mo</div><div class="tags">'+(i.tags||[]).slice(0,4).map(t=>'<span class="tag">'+t+'</span>').join("")+'</div><button class="cta" style="width:100%;margin-top:10px">🛒 Subscribe</button></div>';
});
document.getElementById("grid").innerHTML=h||'<div style="text-align:center;padding:60px;color:#666"><h2>No products found</h2></div>';
}}
function showMint(name,rarity,price,edition,cat){
document.getElementById("modalTitle").textContent=name;
document.getElementById("modalInfo").innerHTML='<b>Rarity:</b> '+rarity.toUpperCase()+'<br><b>Price:</b> $'+price+(currentSection==="nfts"?' ETH':'/mo')+'<br><b>Category:</b> '+cat;
document.getElementById("mintModal").classList.add("active")}
function closeModal(e){if(!e||e.target===document.getElementById("mintModal"))document.getElementById("mintModal").classList.remove("active")}
load();
</script>
</body>
</html>'''

class ClawMartServer(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path == '/':
            self._serve_html(HTML)
        elif parsed.path == '/api/nfts':
            self._serve_json(load_nfts())
        elif parsed.path == '/api/skills':
            self._serve_json(load_skills())
        elif parsed.path == '/api/catalog':
            self._serve_json(load_catalog())
        else:
            super().do_GET()

    def _serve_html(self, html):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(html.encode())

    def _serve_json(self, data):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def log_message(self, format, *args):
        pass

if __name__ == '__main__':
    n = len(load_skills())
    print(f'🦞 ClawMart v2 — {n} skills + 1000 NFTs')
    print(f'   MCP Section: {sum(1 for s in load_skills() if "mcp" in (s.get("tags") or []))} integrations + Claw4All bundle')
    print(f'   Opening: http://localhost:{PORT}')
    with socketserver.TCPServer(("", PORT), ClawMartServer) as httpd:
        webbrowser.open(f'http://localhost:{PORT}')
        httpd.serve_forever()
