#!/usr/bin/env python3
"""Portfolio Weight Optimization — fulfillment script.
Usage: python fulfill_weight_opt.py curves.csv  (columns = strategies, rows = daily equity values, first col optional date)
   or: python fulfill_weight_opt.py ID1 ID2 [ID3...]  (Composer symphony IDs resolved from local registry pool)
Outputs: markdown report to stdout + JSON artifact next to input.
"""
import json, statistics, math, sys, csv, itertools
from pathlib import Path

REG = Path.home() / 'composer-mcp-server' / 'strategy_registry'

def load_from_registry(ids):
    pool = json.load(open(REG / 'combined_equity_pool.json'))
    out = {}
    for i in ids:
        if i not in pool:
            sys.exit(f"ERROR: symphony {i} not in local equity pool")
        s = pool[i]['series']
        out[i] = {int(k): v for k, v in s.items()}
    return out

def load_from_csv(path):
    rows = list(csv.reader(open(path)))
    header = rows[0]
    start = 1 if not _is_num(rows[1][0]) else 0
    names = header[start:]
    out = {n: {} for n in names}
    for t, row in enumerate(rows[1:]):
        for j, n in enumerate(names):
            try:
                out[n][t] = float(row[start + j])
            except (ValueError, IndexError):
                pass
    return out

def _is_num(x):
    try:
        float(x); return True
    except ValueError:
        return False

def daily_returns(s):
    dates = sorted(s.keys())
    rets = {}
    for i in range(1, len(dates)):
        v0, v1 = s[dates[i-1]], s[dates[i]]
        if v0 > 0:
            rets[dates[i]] = v1 / v0 - 1.0
    return rets

def main():
    args = sys.argv[1:]
    if not args:
        sys.exit(__doc__)
    if args[0].endswith('.csv'):
        series = load_from_csv(args[0])
    else:
        series = load_from_registry(args)

    names = list(series.keys())
    k = len(names)
    if k < 2 or k > 6:
        sys.exit(f"ERROR: need 2-6 strategies, got {k}")

    rets = {n: daily_returns(s) for n, s in series.items()}
    common = sorted(set.intersection(*[set(r.keys()) for r in rets.values()]))
    n = len(common)
    yrs = n / 252.0
    if n < 60:
        sys.exit(f"ERROR: only {n} overlapping days — need >= 60")

    R = [[rets[nm][d] for nm in names] for d in common]

    def calc(w):
        eq, dr = 1.0, []
        peak, mdd = 1.0, 0.0
        for row in R:
            r = sum(row[i] * w[i] for i in range(k))
            eq *= (1 + r)
            dr.append(r)
            if eq > peak: peak = eq
            dd = (peak - eq) / peak
            if dd > mdd: mdd = dd
        ann = (eq) ** (1 / yrs) - 1
        mu = statistics.mean(dr) * 252
        sd = statistics.pstdev(dr) * math.sqrt(252)
        return ann, mdd, (mu / sd if sd > 0 else 0.0)

    # correlation matrix
    def corr(a, b):
        xa = [rets[a][d] for d in common]
        xb = [rets[b][d] for d in common]
        ma, mb = statistics.mean(xa), statistics.mean(xb)
        cov = sum((x - ma) * (y - mb) for x, y in zip(xa, xb)) / n
        sa, sb = statistics.pstdev(xa), statistics.pstdev(xb)
        return cov / (sa * sb) if sa > 0 and sb > 0 else 0.0

    print(f"# Portfolio Weight Optimization Report")
    print(f"\nStrategies: {', '.join(names)}")
    print(f"Overlap: {n} trading days ({yrs:.2f} years)\n")
    print("## Correlation Matrix\n")
    print("| |" + "|".join(names) + "|")
    print("|---|" + "---|" * k)
    for a in names:
        print(f"|{a}|" + "|".join(f"{corr(a,b):.3f}" if a != b else "1.000" for b in names) + "|")

    eq_w = [1.0 / k] * k
    eq_ann, eq_mdd, eq_sh = calc(eq_w)
    print(f"\n## Equal Weight Baseline\nann={eq_ann*100:.1f}%  maxDD={eq_mdd*100:.1f}%  sharpe={eq_sh:.3f}\n")

    # grid search (5% for k>=4, 2% for k==3, 1% for k==2)
    step = 0.01 if k == 2 else (0.02 if k == 3 else 0.05)
    ticks = int(round(1 / step))
    results = []
    def rec(idx, remaining, w):
        if idx == k - 1:
            w2 = w + [round(remaining * step, 10)]
            ann, mdd, sh = calc(w2)
            results.append((ann, mdd, sh, w2))
            return
        for t in range(remaining + 1):
            rec(idx + 1, remaining - t, w + [t * step])
    rec(0, ticks, [])

    results.sort(key=lambda x: -x[2])
    both = [r for r in results if r[0] > eq_ann and r[1] < eq_mdd]
    print("## Top 10 by Sharpe (beats equal-weight on BOTH return & drawdown)\n")
    print("|#|ann|maxDD|sharpe|" + "|".join(names) + "|")
    print("|---|---|---|---|" + "---|" * k)
    for i, (ann, mdd, sh, w) in enumerate(both[:10]):
        print(f"|{i+1}|{ann*100:.1f}%|{mdd*100:.1f}%|{sh:.3f}|" + "|".join(f"{x*100:.0f}%" for x in w) + "|")

    print("\n## Pareto Frontier (min drawdown per return tier)\n")
    print("|return tier|min DD|sharpe|" + "|".join(names) + "|")
    print("|---|---|---|" + "---|" * k)
    lo = min(r[0] for r in results); hi = max(r[0] for r in results)
    tier = math.floor(lo * 10) / 10
    while tier < hi:
        cands = [r for r in results if tier <= r[0] < tier + 0.2]
        if cands:
            best = min(cands, key=lambda x: x[1])
            print(f"|>={tier*100:.0f}%|{best[1]*100:.1f}%|{best[2]:.3f}|" + "|".join(f"{x*100:.0f}%" for x in best[3]) + "|")
        tier += 0.2

    rec_w = both[0] if both else results[0]
    print(f"\n## RECOMMENDATION\nWeights: " + ", ".join(f"{names[i]}={rec_w[3][i]*100:.0f}%" for i in range(k)))
    print(f"Expected (in-sample): ann={rec_w[0]*100:.1f}%  maxDD={rec_w[1]*100:.1f}%  sharpe={rec_w[2]:.3f}")
    print(f"vs equal weight:      ann={eq_ann*100:.1f}%  maxDD={eq_mdd*100:.1f}%  sharpe={eq_sh:.3f}")
    print("\nRebalance spec: daily rebalance to target weights; tolerance band ±2%; execute at close.")
    print("\n*In-sample optimization. Past performance does not guarantee future results. Not investment advice.*")

if __name__ == '__main__':
    main()