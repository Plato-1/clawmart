#!/usr/bin/env python3
"""Generate a Composer symphony backtest report for a customer."""
import sys, json, os, urllib.request, time, re
from datetime import date, timedelta

REG_DIR = os.path.expandvars(r"${HOME}\composer-mcp-server\strategy_registry")
OUTPUT_DIR = os.path.expandvars(r"${HOME}\trading_bot\monetization\orders")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load env for Composer API
BASE_URL = os.environ.get("COMPOSER_BASE_URL", "https://api.composer.trade")
KEY_ID = os.environ.get("COMPOSER_KEY_ID", "")
SECRET = os.environ.get("COMPOSER_SECRET", "")
EPOCH = date(1970, 1, 1)

def backtest(sid):
    """Pull backtest from Composer API."""
    req = urllib.request.Request(
        BASE_URL.rstrip("/") + f"/api/v0.1/symphonies/{sid}/backtest",
        data=json.dumps({"capital": 10000, "start_date": "2021-07-01", "end_date": date.today().isoformat(),
                         "slippage_percent": 0.0005, "apply_reg_fee": True, "apply_taf_fee": True, "apply_cat_fee": True}).encode(),
        method="POST",
        headers={"x-api-key-id": KEY_ID, "authorization": f"Bearer {SECRET}", "accept": "application/json", "content-type": "application/json"}
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read().decode("utf-8"))

def load_registry_data(sid):
    """Load correlation and ranking data from registry."""
    idx = json.load(open(os.path.join(REG_DIR, "symphony_index.json")))
    ann = {x["id"]: x for x in json.load(open(os.path.join(REG_DIR, "ann_return_ranked_2yr.json")))}
    corr_cache = json.load(open(os.path.join(REG_DIR, "_pair_corr_cache.json")))
    return idx.get(sid, {}), ann.get(sid, {}), corr_cache

def generate(order_id, symphony_id):
    name = symphony_id
    try:
        bt = backtest(symphony_id)
        stats = bt["stats"]
        first_day = bt["first_day"]
        n_days = stats["size"]
        first_date = EPOCH + timedelta(days=first_day)
        years = n_days / 252.0
    except Exception as e:
        stats = {"error": str(e), "size": 0}
        years = 0
        n_days = 0
        first_date = "API_ERROR"
    
    # Registry data
    entry, ann_data, corr_cache = load_registry_data(symphony_id)
    
    report = {
        "order_id": order_id,
        "symphony_id": symphony_id,
        "symphony_name": entry.get("name", "Unknown"),
        "generated": date.today().isoformat(),
        "backtest": {
            "annualized_return_pct": round(stats.get("annualized_rate_of_return", 0) * 100, 1),
            "cumulative_return_pct": round(stats.get("cumulative_return", 0) * 100, 1),
            "max_drawdown_pct": round(stats.get("max_drawdown", 0) * 100, 1),
            "sharpe_ratio": round(stats.get("sharpe_ratio", 0), 2),
            "sortino_ratio": round(stats.get("sortino_ratio", 0), 2),
            "calmar_ratio": round(stats.get("calmar_ratio", 0), 2),
            "win_rate_pct": round(stats.get("win_rate", 0) * 100, 1),
            "data_window": f"{years:.1f} years ({n_days} trading days from {first_date})",
            "herfindahl_concentration": round(stats.get("herfindahl_index", 0), 3),
            "annualized_turnover": round(stats.get("annualized_turnover", 0), 1),
        },
        "overfitting_flags": [],
        "disclaimer": "Not financial advice. Backtest only. Past performance != future results."
    }
    
    # Overfitting checks
    if years < 2:
        report["overfitting_flags"].append(f"SHORT_HISTORY: Only {years:.1f} years of backtest data — treat returns as unreliable")
    if stats.get("herfindahl_index", 0) > 0.5:
        report["overfitting_flags"].append("HIGH_CONCENTRATION: Portfolio concentrated in few positions, not truly diversified")
    if stats.get("annualized_rate_of_return", 0) > 5:
        report["overfitting_flags"].append("EXTREME_RETURNS: >500% annualized — likely overfit to recent regime")
    
    path = os.path.join(OUTPUT_DIR, f"backtest_{order_id}.json")
    json.dump(report, open(path, "w"), indent=2)
    print(json.dumps({"order_id": order_id, "report": path, "symphony": entry.get("name", "Unknown")}))
    return report

if __name__ == "__main__":
    order_id = sys.argv[1] if len(sys.argv) > 1 else "demo"
    symphony_id = sys.argv[2] if len(sys.argv) > 2 else "W8hpiheymHgbJ1iQjutP"
    generate(order_id, symphony_id)
