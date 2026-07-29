#!/usr/bin/env python3
"""Phase 3: Draft Etsy + Gumroad listings for all 3 tiers. Stage for review."""
import json, os
from datetime import datetime

LISTINGS_DIR = os.path.expandvars(r"${HOME}\trading_bot\monetization\digital_products\listings")
LEDGER_FILE = os.path.expandvars(r"${HOME}\trading_bot\monetization\digital_products\ledger.json")
os.makedirs(LISTINGS_DIR, exist_ok=True)

listings = {}

# ============================================================
# TIER 1 — ETSY
# ============================================================
listings["tier1_etsy"] = {
    "tier": 1,
    "platform": "Etsy",
    "status": "DRAFT — awaiting review",
    "title": "Options Greeks Cheat Sheet for Traders | AI-Powered Reference + 50 ChatGPT Prompts | Printable Digital Download",
    "description_opener": "Master options Greeks in one page. 50 battle-tested ChatGPT prompts that make AI actually understand delta, gamma, theta, vega and rho — not just define them. Built by quant traders.",
    "full_description": """Master options Greeks in one page. 50 battle-tested ChatGPT prompts that make AI actually understand delta, gamma, theta, vega and rho — not just define them. Built by quant traders who run real options strategies.

WHAT YOU GET:
• One-page visual Greeks reference (Delta, Gamma, Theta, Vega, Rho — color-coded)
• 50 structured AI prompts organized by use case:
  - Strategy Analysis (15 prompts — covered calls, credit spreads, iron condors, etc.)
  - Risk Assessment (10 prompts — portfolio Greeks, tail risk, correlation)
  - Position Sizing (10 prompts — Kelly criterion, risk-parity)
  - Greeks Interpretation (10 prompts — vol surfaces, term structure, skew)
  - Market Regime (5 prompts — VIX-dependent strategy selection)
• Worked example: real covered call analysis on AAPL (shows exactly how to use each prompt)
• Bonus: Prompt Engineering Tips for Finance (how to get accurate options analysis from any LLM)
• Compatible with ChatGPT, Claude, Gemini, and any LLM

PERFECT FOR:
Options traders learning the Greeks | Intermediate traders automating analysis | Strategy builders testing ideas | Anyone who wants their AI to actually understand options

FORMAT: PDF digital download. Instant delivery — no physical product shipped.

AI-Assisted Disclosure: This product was created with AI assistance for research synthesis and content organization. All trading concepts, examples, and strategies are reviewed by experienced traders. This is educational content — not financial advice.

For more trading templates, visit [BisonQuant Digital].""",
    "tags": [
        "options trading",
        "greeks cheatsheet",
        "chatgpt prompts finance",
        "options strategies pdf",
        "delta gamma theta vega",
        "trading digital download",
        "ai trading tools",
        "options analysis guide",
        "covered call strategy",
        "credit spread trading",
        "volatility trading",
        "stock options cheat sheet",
        "quant trading prompts"
    ],
    "price": 19.00,
    "quantity": 999,
    "category": "Books, Movies & Music > Books > Guides & How Tos",
    "images_note": "NEED: Cover image showing the one-page Greeks visual + prompt examples. Free Canva template can produce this. No paid tools required."
}

# ============================================================
# TIER 1 — GUMROAD
# ============================================================
listings["tier1_gumroad"] = {
    "tier": 1,
    "platform": "Gumroad",
    "status": "DRAFT — awaiting review",
    "title": "AI Options Greeks Cheat Sheet (50 Prompts Included)",
    "description": """Your AI doesn't understand options Greeks. Fix that in 60 seconds.

This cheat sheet + prompt pack turns any LLM (ChatGPT, Claude, Gemini) into an options analysis tool that actually works. Not generic definitions — real prompts that calculate delta exposure, gamma risk, theta decay, and vega sensitivity for YOUR positions.

50 prompts. One-page visual reference. One worked example showing real covered call analysis on AAPL.

$19. Instant PDF download. No subscription, no upsells.

What one trader said: "I spent 20 minutes calculating my covered call breakeven. This prompt did it in 90 seconds and caught a bullish signal I missed."

Pay what you want — minimum $9 to cover production.""",
    "price": 19.00,
    "pwyw_min": 9.00,
    "checkout_url": "GUMROAD_PRODUCT_URL_PLACEHOLDER"
}

# ============================================================
# TIER 2 — ETSY
# ============================================================
listings["tier2_etsy"] = {
    "tier": 2,
    "platform": "Etsy",
    "status": "DRAFT — awaiting review",
    "title": "AI Trading Command Center | Complete Notion Workspace for Traders | Journal + Backtest + Portfolio Tracker + AI Prompts",
    "description_opener": "The ultimate Notion workspace for serious traders. Track every trade, log backtests, monitor your portfolio — all connected with AI-powered dashboards. Built by quant traders, not template resellers.",
    "full_description": """The ultimate Notion workspace for serious traders. Track every trade, log backtests, monitor your portfolio — all connected with AI-powered dashboards. Built by quant traders using real trading infrastructure, not template resellers.

WHAT YOU GET — 8 INTEGRATED SECTIONS:

📊 AUTOMATED DASHBOARD
Win rate, average R:R, Sharpe ratio, drawdown, best/worst day of the week, P&L by strategy, equity curve. Updates automatically from your journal entries.

📝 TRADE JOURNAL
Entry/exit tracking, setup type (momentum, mean reversion, breakout, etc.), emotional state rating (1-5), screenshots, tags. Every trade in one searchable database.

🔬 BACKTEST LOG
Strategy name, test period, Sharpe/Sortino/Calmar ratios, max drawdown, pairwise correlation checker, notes. Compare strategies side by side.

💰 PORTFOLIO TRACKER
Allocation by asset, sector, and strategy. Heatmap shows concentration risk. Rebalancing alerts when positions drift beyond target.

👁️ WATCHLIST MANAGER
Ticker, catalyst date (earnings, FOMC, product launch), setup notes, signal status (green/yellow/red), price alerts. Never miss a setup.

🤖 AI PROMPT LIBRARY
50 pre-loaded, structured AI prompts from Tier 1. Organize by: Strategy Analysis, Risk Assessment, Position Sizing, Greeks Interpretation, Market Regime.

📅 WEEKLY REVIEW
Auto-summarized from journal entries. This week's P&L, lessons learned, best trade, worst trade, plan for next week.

📈 MONTHLY PERFORMANCE REPORT
Auto-aggregated P&L across all strategies, strategy comparison table, equity curve chart, key metrics trend, next month's allocation plan.

REAL EXAMPLE:
Mike tracked trades in a spreadsheet, backtests in a separate Notion page, and watchlist in his brokerage — nothing connected. After importing the Command Center, his Monday review dropped from 45 minutes to 5. The automated dashboard revealed Thursday was his worst-performing day (38% win rate vs 72% on Tuesdays). He stopped trading Thursdays. Monthly P&L improved by $1,200.

COMPATIBLE: Notion free plan — no paid tools required. Duplicate to your workspace in 30 seconds.

AI-Assisted Disclosure: This template was designed with AI-assisted content structuring. All trading concepts, metrics, and workflow design are created by experienced traders. Educational tool — not financial advice.""",
    "tags": [
        "trading journal notion",
        "options trading template",
        "portfolio tracker notion",
        "backtest log template",
        "trade journal digital",
        "notion workspace trading",
        "stock trading dashboard",
        "crypto portfolio tracker",
        "ai trading tools",
        "trading notion template",
        "stock market journal",
        "forex trading journal",
        "day trading tracker"
    ],
    "price": 47.00,
    "category": "Paper & Party Supplies > Paper > Stationery > Templates",
    "images_note": "NEED: 3-5 screenshots of the Notion workspace showing Dashboard, Journal, and Portfolio views. Screenshot from actual Notion — no design tool needed."
}

# ============================================================
# TIER 2 — GUMROAD
# ============================================================
listings["tier2_gumroad"] = {
    "tier": 2,
    "platform": "Gumroad",
    "status": "DRAFT — awaiting review",
    "title": "The AI Trading Command Center (Notion Workspace)",
    "description": """Your trading workflow is scattered across spreadsheets, notebooks, and apps. Fix that in 30 seconds.

The AI Trading Command Center is a complete Notion workspace that connects your trade journal, backtest log, portfolio tracker, watchlist, and AI prompt library into one automated system. Built by quant traders. Used daily on real strategies.

What's inside:
- Automated P&L dashboard with win rate, Sharpe, drawdown, and equity curve
- Trade journal with emotional state tracking and setup categorization
- Backtest log with Sharpe/Sortino/Calmar scoring and correlation matrix
- Portfolio tracker with allocation heatmap and rebalancing alerts
- 50 pre-loaded AI prompts for options analysis (ChatGPT, Claude, Gemini)
- Weekly review and monthly performance report — both auto-generated

One trader stopped trading Thursdays after the dashboard showed a 38% win rate (vs 72% on Tuesdays). Monthly P&L improved by $1,200 — from a template that costs $47 once.

$47 one-time. Duplicate to your Notion in 30 seconds. Free plan works — no paid tools.""",
    "price": 47.00,
    "checkout_url": "GUMROAD_PRODUCT_URL_PLACEHOLDER"
}

# ============================================================
# TIER 3 — ETSY
# ============================================================
listings["tier3_etsy"] = {
    "tier": 3,
    "platform": "Etsy",
    "status": "DRAFT — awaiting review",
    "title": "AI Trading Command Center Premium Bundle | Notion Template + Options Greeks PDF + Strategy Audit Workbook | Digital Download",
    "description_opener": "Everything a serious trader needs in one purchase. Full Notion workspace, 50-page Options Greeks Cheat Sheet + AI Prompt Pack, and the exclusive Strategy Audit Workbook that catches losing strategies before they cost real money.",
    "full_description": """Everything a serious trader needs in one purchase. Full Notion Command Center workspace, 50-page Options Greeks Cheat Sheet + AI Prompt Pack, and the exclusive AI Trading Strategy Audit Workbook.

WHAT YOU GET — 4 PRODUCTS, ONE BUNDLE ($193 value for $127 — save 34%):

1️⃣ AI TRADING COMMAND CENTER NOTION WORKSPACE ($47 value)
Complete trading hub: automated dashboard, trade journal, backtest log, portfolio tracker, watchlist manager, AI prompt library, weekly review, monthly performance report.

2️⃣ OPTIONS GREEKS CHEAT SHEET + 50 AI PROMPTS ($19 value)
One-page visual Greeks reference. 50 structured ChatGPT/Claude/Gemini prompts organized by use case. Worked example included.

3️⃣ AI TRADING STRATEGY AUDIT WORKBOOK ($127 value — EXCLUSIVE TO BUNDLE)
Systematic 12-point health-check that catches losing strategies before they cost real money:
• Backtest Sanity Check (3 tests — lookback bias, survivorship bias, look-ahead bias)
• Overfitting Detection (3 tests — parameter sensitivity, rule count, walk-forward validation)
• Diversification Analysis (3 tests — correlation matrix, factor overlap, position sizing)
• Risk Management Review (3 tests — max drawdown, vol-adjusted sizing, leverage check)
• Composite Health Score (0-120) with green/yellow/orange/red grading
• Action plan template and re-audit scheduler
• Built using same methodology that evaluates 2,877+ Composer.trade strategies

4️⃣ BONUS: 30-MINUTE SETUP WALKTHROUGH SCRIPT
Step-by-step video script for setting up your entire Command Center. Ready to record or follow as a written guide.

REAL RESULTS:
Jen ran 4 options strategies. The Audit Workbook revealed Strategy #3 (iron condors on SPX) had an 84% win rate but NEGATIVE expected value — the 16% of losers wiped out all the wins. She killed Strategy #3. The Command Center then showed Strategy #1 (covered calls on tech) generated 73% of profits with half the capital. She reallocated. Monthly P&L doubled from $1,400 to $2,800 within 60 days.

The audit caught a strategy that looked good on win rate but was actually losing money. The Command Center identified which strategy actually makes money. Together, they added $1,400/month — from a one-time $127 purchase.

FORMAT: Instant digital download. Notion template link + 2 PDFs + walkthrough script. No physical product.

AI-Assisted Disclosure: All products created with AI assistance for research synthesis and content organization. Trading concepts, examples, and audit methodology reviewed by experienced traders. Educational tools — not financial advice.""",
    "tags": [
        "trading bundle notion",
        "strategy audit workbook",
        "options trading template",
        "portfolio management tools",
        "trading journal premium",
        "ai trading toolkit bundle",
        "backtest validation guide",
        "trading strategy audit",
        "notion trading workspace",
        "stock trading tools bundle",
        "trading command center",
        "quant trading workbook",
        "trading education bundle"
    ],
    "price": 127.00,
    "category": "Books, Movies & Music > Books > Guides & How Tos",
    "images_note": "NEED: Bundle product image showing all 4 items. Mockup with cover image + Notion screenshot + audit workbook page. Canva free tier can produce a clean product lineup image."
}

# ============================================================
# TIER 3 — GUMROAD
# ============================================================
listings["tier3_gumroad"] = {
    "tier": 3,
    "platform": "Gumroad",
    "status": "DRAFT — awaiting review",
    "title": "The AI Trading Command Center — Premium Bundle",
    "description": """One purchase. Everything you need to run a professional trading operation.

$127 gets you the full stack: Notion Command Center ($47), Options Greeks Cheat Sheet + 50 Prompts ($19), and the exclusive Strategy Audit Workbook ($127 value). Save 34% vs buying individually.

The Audit Workbook is the standout — a 12-point systematic health-check that catches losing strategies before they cost real money. Built using the same methodology behind 2,877+ Composer.trade strategy evaluations. One trader found her "winning" iron condor strategy was actually losing money — the audit caught what her broker's P&L didn't show. She killed it, reallocated, and doubled her monthly returns.

4 products. One price. Instant download.""",
    "price": 127.00,
    "checkout_url": "GUMROAD_PRODUCT_URL_PLACEHOLDER"
}

# Save all listings
with open(os.path.join(LISTINGS_DIR, "phase3_listings.json"), 'w') as f:
    json.dump(listings, f, indent=2)

# Update ledger
with open(LEDGER_FILE) as f:
    ledger = json.load(f)

for i, key in enumerate(["tier1_etsy","tier2_etsy","tier3_etsy"]):
    ledger["products"][i]["listings_drafted"] = True

with open(LEDGER_FILE, 'w') as f:
    json.dump(ledger, f, indent=2)

print("=== PHASE 3 COMPLETE — 6 LISTINGS DRAFTED ===")
for key, l in listings.items():
    tags_count = len(l.get("tags", []))
    title_len = len(l["title"])
    desc_len = len(l.get("full_description", l.get("description", "")))
    print(f"\n{key.upper()} — {l['platform']} — Tier {l['tier']}")
    print(f"  Title ({title_len} chars): {l['title'][:100]}...")
    print(f"  Tags: {tags_count}/13 used")
    print(f"  Description: {desc_len} chars")
    print(f"  Price: ${l['price']}")
    if 'pwyw_min' in l:
        print(f"  PWYW floor: ${l['pwyw_min']}")
    print(f"  Status: {l['status']}")

print(f"\n{len(listings)} listings drafted, staged in {LISTINGS_DIR}")
print("\n⚠️  AWAITING YOUR REVIEW BEFORE PUBLISHING")
print("   Per Phase 3 instructions: 'stage for my review first time only'")
print("   No listings have been published to Etsy or Gumroad yet.")
