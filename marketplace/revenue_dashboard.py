#!/usr/bin/env python3
"""
Revenue Dashboard — tracks all 10 monetization methods.
"""
import json, os, time
from datetime import datetime

DASHBOARD_DIR = os.path.expandvars(r"${HOME}\trading_bot\monetization\marketplace")
DASHBOARD_FILE = os.path.join(DASHBOARD_DIR, "revenue_dashboard.json")

def init_dashboard():
    return {
        "updated": datetime.utcnow().isoformat(),
        "methods": {
            "1_marketplace_fees": {"name": "Marketplace Take Rate", "status": "LIVE", "revenue_today": 0, "revenue_month": 0, "target_daily": 25},
            "2_genesis_nfts": {"name": "Genesis NFT Sales", "status": "LIVE", "revenue_today": 0, "revenue_month": 0, "target_daily": 270},
            "3_drop1_nfts": {"name": "Drop #1 NFT Collection", "status": "LIVE", "revenue_today": 0, "revenue_month": 0, "target_daily": 300},
            "4_subscriptions": {"name": "Signal Subscriptions", "status": "LIVE", "revenue_today": 0, "revenue_month": 0, "target_daily": 45},
            "5_seller_recruiting": {"name": "Seller Recruitment", "status": "PENDING", "revenue_today": 0, "revenue_month": 0, "target_daily": 300, "action": "Send 10 ambassador follow-up DMs"},
            "6_strategy_audits": {"name": "Strategy Audits", "status": "PENDING", "revenue_today": 0, "revenue_month": 0, "target_daily": 75, "action": "Post free-first audit offer on Moltbook"},
            "7_book_summaries": {"name": "Book Summary Sales", "status": "PENDING", "revenue_today": 0, "revenue_month": 0, "target_daily": 15, "action": "Post 1 free sample daily"},
            "8_wallet_generation": {"name": "Wallet Generation", "status": "LIVE", "revenue_today": 0, "revenue_month": 0, "target_daily": 50},
            "9_claw_earn": {"name": "Claw Earn Arbitrage", "status": "NEEDS_USER", "revenue_today": 0, "revenue_month": 0, "target_daily": 30, "action": "Fund Base wallet with $55 USDC + $5 ETH gas"},
            "10_mcp_integration": {"name": "MCP Integration", "status": "PENDING", "revenue_today": 0, "revenue_month": 0, "target_daily": 30, "action": "Reply to Moltbook API questions with free offer"},
        },
        "totals": {"revenue_today": 0, "revenue_month": 0, "target_daily": 1140, "target_monthly": 34200}
    }

def load_dashboard():
    if os.path.exists(DASHBOARD_FILE):
        return json.load(open(DASHBOARD_FILE))
    d = init_dashboard()
    json.dump(d, open(DASHBOARD_FILE, "w"), indent=2)
    return d

def update_revenue(method_key, amount_usd):
    d = load_dashboard()
    if method_key in d["methods"]:
        d["methods"][method_key]["revenue_today"] += amount_usd
        d["methods"][method_key]["revenue_month"] += amount_usd
        d["totals"]["revenue_today"] += amount_usd
        d["totals"]["revenue_month"] += amount_usd
        if d["methods"][method_key]["status"] == "PENDING" and amount_usd > 0:
            d["methods"][method_key]["status"] = "LIVE"
    d["updated"] = datetime.utcnow().isoformat()
    json.dump(d, open(DASHBOARD_FILE, "w"), indent=2)
    return d

def show_dashboard():
    d = load_dashboard()
    print(f"REVENUE DASHBOARD — {d['updated'][:10]}")
    print("=" * 75)
    print(f"{'#':<3} {'Method':<25} {'Status':<12} {'Today':>8} {'Month':>10} {'Target':>10}")
    print("-" * 75)
    for key, m in d["methods"].items():
        num = key.split("_")[0]
        status = m["status"]
        icon = "✅" if status == "LIVE" else "⏳" if status == "PENDING" else "🔴"
        print(f"{icon} {num:<1} {m['name'][:24]:<24} {status:<12} ${m['revenue_today']:>7.0f} ${m['revenue_month']:>9.0f} ${m['target_daily']:>9.0f}")
    print("-" * 75)
    print(f"{'':<3} {'TOTAL':<25} {'':<12} ${d['totals']['revenue_today']:>7.0f} ${d['totals']['revenue_month']:>9.0f} ${d['totals']['target_daily']:>9.0f}")
    
    # Show pending actions
    pending = [(k, m) for k, m in d["methods"].items() if m["status"] in ("PENDING", "NEEDS_USER")]
    if pending:
        print("\n⚠️  ACTIONS NEEDED:")
        for k, m in pending:
            print(f"   {m['name']}: {m.get('action', 'Activate this method')}")

if __name__ == "__main__":
    show_dashboard()
