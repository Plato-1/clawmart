#!/usr/bin/env python3
"""BisonQuant Strategy Analytics MCP Server.

Real quant tools over a 2,875-symphony Composer registry + 417 tracked live strategies.

FREE tools (no key):    search_strategies, get_strategy_stats, top_performers
PREMIUM tools ($5/mo):  correlation_matrix, optimize_weights, pareto_frontier
                        Buy a key: https://paypal.me/BisonQuant/5  (email bisonquant@agentmail.to after payment)

Run (stdio): python server.py
Env: BISONQUANT_LICENSE_KEY=<key> unlocks premium tools.
"""
import hashlib
import hmac
import json
import math
import os
import statistics
import sys
from pathlib import Path

try:
    from mcp.server.fastmcp import FastMCP
except ImportError:
    sys.exit("pip install 'mcp[cli]' first")

DATA = Path(__file__).parent / "data"
_SECRET = b"bq-mcp-2026-v1"  # key derivation salt (server-side only)

mcp = FastMCP("bisonquant-strategy-analytics")

_stats = None
_pool = None


def stats():
    global _stats
    if _stats is None:
        _stats = json.load(open(DATA / "stats.json"))
    return _stats


def pool():
    global _pool
    if _pool is None:
        _pool = json.load(open(DATA / "equity_pool.json"))
    return _pool


def _licensed() -> bool:
    key = os.getenv("BISONQUANT_LICENSE_KEY", "")
    if not key or "-" not in key:
        return False
    email, sig = key.rsplit("-", 1)
    want = hmac.new(_SECRET, email.encode(), hashlib.sha256).hexdigest()[:16]
    return hmac.compare_digest(sig, want)


PAYWALL = (
    "PREMIUM TOOL — requires license key ($5/month).\n"
    "1) Pay: https://paypal.me/BisonQuant/5 (any card) or ETH/USDC to "
    "0xA2cCD22EEbd76e1BFFc51b0B3C31a120Ee36d22d\n"
    "2) Email your payment receipt to bisonquant@agentmail.to — key delivered within 24h.\n"
    "3) Set BISONQUANT_LICENSE_KEY=<key> in this server's env and restart."
)


def _returns(series):
    dates = sorted(int(k) for k in series)
    out = {}
    for i in range(1, len(dates)):
        v0, v1 = series[str(dates[i - 1])], series[str(dates[i])]
        if isinstance(series, dict) and v0 and v0 > 0:
            out[dates[i]] = v1 / v0 - 1.0
    return out


def _series_of(sid):
    p = pool()
    if sid not in p:
        return None
    return p[sid]["series"]


# ---------- FREE TOOLS ----------

@mcp.tool()
def search_strategies(query: str = "", min_ann_return: float = 0.0, max_drawdown: float = 1.0, limit: int = 10) -> str:
    """Search 417 tracked Composer strategies by name/ticker with return & drawdown filters.
    min_ann_return: e.g. 0.5 = 50% annualized. max_drawdown: e.g. 0.3 = max -30% DD. FREE."""
    q = query.lower()
    rows = []
    for sid, s in stats().items():
        if s["ann"] is None or s["dd"] is None:
            continue
        if s["ann"] < min_ann_return or abs(s["dd"]) > max_drawdown:
            continue
        if q and q not in s["name"].lower() and not any(q in t.lower() for t in s["tickers"]):
            continue
        rows.append((sid, s))
    rows.sort(key=lambda x: -(x[1]["ann"] or 0))
    out = [f"{len(rows)} matches (showing {min(limit, len(rows))}):"]
    for sid, s in rows[:limit]:
        out.append(f"- {sid} | ann={s['ann']*100:.1f}% dd={s['dd']*100:.1f}% sharpe={s['sharpe']} | {s['name'][:70]}")
    return "\n".join(out)


@mcp.tool()
def get_strategy_stats(strategy_id: str) -> str:
    """Full stats for one strategy by ID: annualized return, max drawdown, Sharpe, tickers. FREE."""
    s = stats().get(strategy_id)
    if not s:
        return f"Unknown strategy id: {strategy_id}"
    return json.dumps(s, indent=1)


@mcp.tool()
def top_performers(n: int = 10, max_dd: float = 0.5) -> str:
    """Top N strategies by annualized return under a drawdown cap. FREE."""
    rows = [(sid, s) for sid, s in stats().items()
            if s["ann"] is not None and s["dd"] is not None and abs(s["dd"]) <= max_dd]
    rows.sort(key=lambda x: -x[1]["ann"])
    out = [f"Top {min(n, len(rows))} (max DD {max_dd*100:.0f}%):"]
    for sid, s in rows[:n]:
        out.append(f"- {sid} | ann={s['ann']*100:.1f}% dd={s['dd']*100:.1f}% | {s['name'][:70]}")
    out.append("\nWant correlation + optimal weights across these? Premium tools: correlation_matrix, optimize_weights ($5/mo).")
    return "\n".join(out)


# ---------- PREMIUM TOOLS ----------

@mcp.tool()
def correlation_matrix(strategy_ids: list[str]) -> str:
    """Pairwise daily-return correlation matrix for 2-6 strategies (finds diversifiers). PREMIUM $5/mo."""
    if not _licensed():
        return PAYWALL
    ids = strategy_ids[:6]
    rets = {}
    for i in ids:
        s = _series_of(i)
        if s is None:
            return f"No equity series for {i}"
        rets[i] = _returns(s)
    lines = ["|" + "|".join([""] + ids) + "|"]
    for a in ids:
        row = [a]
        for b in ids:
            if a == b:
                row.append("1.000")
                continue
            common = sorted(set(rets[a]) & set(rets[b]))
            xa = [rets[a][d] for d in common]
            xb = [rets[b][d] for d in common]
            ma, mb = statistics.mean(xa), statistics.mean(xb)
            cov = sum((x - ma) * (y - mb) for x, y in zip(xa, xb)) / len(common)
            sa, sb = statistics.pstdev(xa), statistics.pstdev(xb)
            row.append(f"{cov/(sa*sb):.3f}" if sa and sb else "n/a")
        lines.append("|" + "|".join(row) + "|")
    return "\n".join(lines)


@mcp.tool()
def optimize_weights(strategy_ids: list[str], objective: str = "sharpe") -> str:
    """Grid-search optimal portfolio weights for 2-4 strategies. objective: sharpe|return|drawdown. PREMIUM $5/mo."""
    if not _licensed():
        return PAYWALL
    ids = strategy_ids[:4]
    k = len(ids)
    if k < 2:
        return "Need at least 2 strategy ids"
    rets = {}
    for i in ids:
        s = _series_of(i)
        if s is None:
            return f"No equity series for {i}"
        rets[i] = _returns(s)
    common = sorted(set.intersection(*[set(r) for r in rets.values()]))
    n = len(common)
    if n < 60:
        return f"Only {n} overlapping days — need 60+"
    yrs = n / 252.0
    R = [[rets[i][d] for i in ids] for d in common]

    def calc(w):
        eq, peak, mdd, dr = 1.0, 1.0, 0.0, []
        for row in R:
            r = sum(row[j] * w[j] for j in range(k))
            eq *= 1 + r
            dr.append(r)
            peak = max(peak, eq)
            mdd = max(mdd, (peak - eq) / peak)
        ann = eq ** (1 / yrs) - 1
        sd = statistics.pstdev(dr) * math.sqrt(252)
        sh = (statistics.mean(dr) * 252 / sd) if sd else 0
        return ann, mdd, sh

    step = 0.02 if k <= 3 else 0.05
    ticks = int(round(1 / step))
    best, results = None, []

    def rec(idx, rem, w):
        nonlocal best
        if idx == k - 1:
            w2 = w + [rem * step]
            ann, mdd, sh = calc(w2)
            score = sh if objective == "sharpe" else (ann if objective == "return" else -mdd)
            results.append((score, ann, mdd, sh, w2))
            return
        for t in range(rem + 1):
            rec(idx + 1, rem - t, w + [t * step])

    rec(0, ticks, [])
    results.sort(key=lambda x: -x[0])
    eq_ann, eq_mdd, eq_sh = calc([1 / k] * k)
    _, ann, mdd, sh, w = results[0]
    lines = [
        f"Overlap: {n}d ({yrs:.2f}yr) | objective: {objective}",
        f"Equal weight: ann={eq_ann*100:.1f}% dd={eq_mdd*100:.1f}% sharpe={eq_sh:.3f}",
        f"OPTIMAL:      ann={ann*100:.1f}% dd={mdd*100:.1f}% sharpe={sh:.3f}",
        "Weights: " + ", ".join(f"{ids[i]}={w[i]*100:.0f}%" for i in range(k)),
        "(in-sample; not investment advice)",
    ]
    return "\n".join(lines)


@mcp.tool()
def pareto_frontier(strategy_ids: list[str]) -> str:
    """Best achievable drawdown at each return tier across all weight combos (2-4 strategies). PREMIUM $5/mo."""
    if not _licensed():
        return PAYWALL
    ids = strategy_ids[:4]
    k = len(ids)
    if k < 2:
        return "Need at least 2 strategy ids"
    rets = {}
    for i in ids:
        s = _series_of(i)
        if s is None:
            return f"No equity series for {i}"
        rets[i] = _returns(s)
    common = sorted(set.intersection(*[set(r) for r in rets.values()]))
    if len(common) < 60:
        return f"Only {len(common)} overlapping days — need 60+"
    yrs = len(common) / 252.0
    R = [[rets[i][d] for i in ids] for d in common]

    def calc(w):
        eq, peak, mdd = 1.0, 1.0, 0.0
        for row in R:
            r = sum(row[j] * w[j] for j in range(k))
            eq *= 1 + r
            peak = max(peak, eq)
            mdd = max(mdd, (peak - eq) / peak)
        return eq ** (1 / yrs) - 1, mdd

    step = 0.02 if k <= 3 else 0.05
    ticks = int(round(1 / step))
    results = []

    def rec(idx, rem, w):
        if idx == k - 1:
            w2 = w + [rem * step]
            ann, mdd = calc(w2)
            results.append((ann, mdd, w2))
            return
        for t in range(rem + 1):
            rec(idx + 1, rem - t, w + [t * step])

    rec(0, ticks, [])
    lo = min(r[0] for r in results)
    hi = max(r[0] for r in results)
    lines = ["|return tier|min DD|" + "|".join(ids) + "|"]
    tier = math.floor(lo * 5) / 5
    while tier < hi:
        cands = [r for r in results if tier <= r[0] < tier + 0.2]
        if cands:
            ann, mdd, w = min(cands, key=lambda x: x[1])
            lines.append(f"|>={tier*100:.0f}%|{mdd*100:.1f}%|" + "|".join(f"{x*100:.0f}%" for x in w) + "|")
        tier += 0.2
    return "\n".join(lines)


if __name__ == "__main__":
    mcp.run()