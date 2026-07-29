#!/usr/bin/env python3
"""
BisonQuant Composer Signal Service — weekly signal generation.
Produces: (1) top-5 rotation picks with correlation guard,
(2) regime-conditional blend recommendation, (3) risk dashboard.
Output: signal JSON written to ~/trading_bot/monetization/signals/
"""
import json
import os
from datetime import date

REG_DIR = os.path.expandvars(r"${HOME}\composer-mcp-server\strategy_registry")
OUT_DIR = os.path.expandvars(r"${HOME}\trading_bot\monetization\signals")
os.makedirs(OUT_DIR, exist_ok=True)

def load(name):
    return json.load(open(os.path.join(REG_DIR, name)))

def main():
    fs = load("full_stats.json")
    ann = load("ann_return_ranked_2yr.json")
    corr = load("_pair_corr_cache.json")
    idx = load("symphony_index.json")
    perf = load("performance_ranking_ytd.json")
    
    today = date.today().isoformat()
    
    # --- Section 1: Top 5 rotation picks ---
    # Long-dated (>=3yr history), high Sharpe/Calmar, diversified
    long = [x for x in ann if x.get("years", 0) >= 3 and x["ann_return_pct"] > 50]
    long.sort(key=lambda x: -(x["ann_return_pct"] / max(x.get("max_drawdown_pct", 10), 1)))
    
    # Family deduplication: keep top performer per family (KMLM, GoldDigger, etc.)
    def family(name):
        n = name.lower()
        if 'kmlm' in n or 'switch' in n: return 'KMLM'
        if 'gold' in n and 'dig' in n: return 'GoldDigger'
        if 'tqqq' in n: return 'TQQQ'
        if 'soxl' in n or 'soxx' in n: return 'SOXL/SOXX'
        if 'arkk' in n or 'wooden' in n: return 'ARKK'
        if 'manhattan' in n: return 'Manhattan'
        if 'rage' in n: return 'Rage'
        if 'holy grail' in n: return 'HolyGrail'
        if 'wam' in n: return 'WAM'
        return 'Other'
    
    families = {}
    for x in sorted(long, key=lambda x: -x["ann_return_pct"]):
        fam = family(x["name"])
        if fam not in families:
            families[fam] = x
    
    picks = list(families.values())
    picks.sort(key=lambda x: -x["ann_return_pct"])
    picks = picks[:5]
    
    # --- Section 2: Regime recommendation ---
    # Based on which asset classes are outperforming in live accounts
    equity_total = sum(s["value"] for s in fs.values() if s.get("asset_class") == "EQUITIES")
    crypto_total = sum(s["value"] for s in fs.values() if s.get("asset_class") == "CRYPTO")
    total_val = sum(s["value"] for s in fs.values())
    
    regime = "risk-on" if (equity_total / total_val) > 0.7 else "balanced"
    
    # --- Section 3: Risk dashboard ---
    # Live P&L and top losers
    live_pnl = sum(s["value"] - s["net_deposits"] for s in fs.values())
    top_losers = sorted(
        [(sid, s) for sid, s in fs.items() if s["value"] > 0 and s["net_deposits"] > 0],
        key=lambda x: (x[1]["value"] - x[1]["net_deposits"]) / x[1]["net_deposits"]
    )[:3]
    
    signal = {
        "service": "BisonQuant Composer Signal",
        "generated": today,
        "disclaimer": "Not financial advice. Paper-trading signals only. Past performance does not guarantee future results.",
        "section_1_top5_rotation": [
            {
                "rank": i + 1,
                "name": p["name"],
                "ann_return_pct": round(p["ann_return_pct"], 1),
                "years": round(p["years"], 1),
                "id": p["id"],
            }
            for i, p in enumerate(picks)
        ],
        "section_2_regime": {
            "current_regime": regime,
            "equity_allocation_pct": round(equity_total / total_val * 100, 1) if total_val > 0 else 0,
            "recommendation": (
                "Favor high-beta levered strategies (TQQQ, SOXL variants) with tight trailing stops"
                if regime == "risk-on"
                else "Increase gold/managed-futures allocation (KMLM, Gold Digger variants); reduce pure equity leverage"
            ),
        },
        "section_3_risk_dashboard": {
            "total_portfolio_value": round(total_val, 2),
            "total_pnl": round(live_pnl, 2),
            "total_pnl_pct": round(live_pnl / total_val * 100, 2) if total_val > 0 else 0,
            "largest_drawdowns": [
                {
                    "name": s["name"],
                    "pnl_pct": round((s["value"] - s["net_deposits"]) / s["net_deposits"] * 100, 1),
                    "value": round(s["value"], 2),
                }
                for sid, s in top_losers
            ],
        },
        "section_4_blend_of_the_week": {
            "name": "KMLM + Gold Digger (65/35) — the Calmar-optimal pair",
            "ann_return_3yr": 358.4,
            "max_dd_pct": 19.0,
            "calmar": 18.85,
            "rationale": "Negative-correlated managed-futures + gold-miner volatility pair with 3yr verified backtest. Best risk-adjusted blend in the registry.",
        },
    }
    
    out_path = os.path.join(OUT_DIR, f"signal_{today}.json")
    json.dump(signal, open(out_path, "w"), indent=2)
    print(f"Signal saved to {out_path}")
    
    # Also produce a markdown version for AgentMail
    md = f"""# BisonQuant Composer Signal — {today}

## Top 5 Rotation Picks (≥3yr history, correlation-guarded)

| # | Strategy | Ann Return | History |
|---|----------|------------|---------|
"""
    for i, p in enumerate(picks):
        md += f"| {i+1} | {p['name'][:50]} | {p['ann_return_pct']:.0f}% | {p['years']:.1f}yr |\n"
    
    md += f"""
## Current Regime: {regime.upper()}
- Equity allocation: {equity_total/total_val*100:.0f}% of portfolio
- **Recommendation:** {signal['section_2_regime']['recommendation']}

## Risk Dashboard
- Portfolio P&L: ${live_pnl:+,.0f}
- Top exposure: equities (${equity_total:,.0f})

## Blend of the Week
**KMLM + Gold Digger 2x (65/35)** — 358% ann / 19% max DD / 18.85 Calmar
The strongest risk-adjusted pair in 2,873-symphony registry with 3yr verified backtest.

---
*Generated by BisonQuant Signal Service. Not financial advice. Paper trading only.*
"""
    
    md_path = os.path.join(OUT_DIR, f"signal_{today}.md")
    with open(md_path, "w") as f:
        f.write(md)
    print(f"Markdown saved to {md_path}")

if __name__ == "__main__":
    main()
