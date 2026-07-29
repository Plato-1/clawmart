# AI TRADING STRATEGY HEALTH-CHECK AUDIT WORKBOOK
## How to Diagnose, Fix, or Kill Any Trading Strategy Before It Loses Real Money

### Built using the same methodology that evaluates 2,877+ Composer.trade strategies

---

## AUDIT STEP 1: Backtest Sanity Check

### Is your backtest lying to you?

**Check #1: Lookback Period Bias**
- Does the backtest window include both bull AND bear markets?
- Minimum: 3 years of data, covering at least one 20%+ drawdown in the benchmark
- **RED FLAG:** Backtest only covers 2023-2024 (pure bull market) → results are inflated
- **SCORE:** ___/10 (10 = 5+ years across multiple regimes)

**Check #2: Survivorship Bias**
- Are you backtesting on current index constituents or historical?
- Stocks that went bankrupt or were delisted must be included
- **RED FLAG:** Testing on today's S&P 500 members for 2015 data → missing all delisted losers
- **SCORE:** ___/10 (10 = delisted/inactive symbols included)

**Check #3: Look-Ahead Bias**
- Are you accidentally using future data to make past decisions?
- Earnings data, index rebalancing, and splits must lag appropriately
- **RED FLAG:** Using Q4 earnings to decide Q4 trades → data wasn't available yet
- **SCORE:** ___/10 (10 = all data point-in-time verified)

**Backtest Sanity Score: ___/30**
- 25-30: Trust but verify
- 18-24: Validated with caveats
- <18: DO NOT trade live — fix data first

---

## AUDIT STEP 2: Overfitting Detection

### The #1 killer of live strategies — is yours overfit?

**Check #4: Parameter Sensitivity**
- Vary each parameter ±20%. Does performance collapse?
- A robust strategy should degrade gracefully, not cliff-dive
- **TEST:** Optimize on 2019-2021, validate on 2022-2024. Performance drop <30% = passing
- **Your result:** ___% performance drop
- **SCORE:** ___/10 (10 = <10% drop)

**Check #5: Rule Count**
- How many discrete rules does your strategy have?
- >15 rules = almost certainly overfit
- <8 rules with strong economic rationale = more robust
- **Your count:** ___ rules
- **SCORE:** ___/10 (10 = <8 rules)

**Check #6: Walk-Forward Validation**
- Split data: 70% training, 30% out-of-sample (OOS)
- Train on the first chunk, test on the unseen chunk
- Repeat for multiple windows
- **Your OOS/In-Sample Sharpe Ratio:** ___
- **RED FLAG:** OOS Sharpe <50% of in-sample Sharpe
- **SCORE:** ___/10 (10 = OOS Sharpe >80% of in-sample)

**Overfitting Score: ___/30**
- 25-30: Likely robust
- 18-24: Concerning, needs simplification
- <18: Overfit — reduce rules, retest

---

## AUDIT STEP 3: Correlation & Concentration Risk

### Your 5 strategies might all be the same bet

**Check #7: Strategy Correlation Matrix**
- Calculate pairwise correlation between all your live strategies
- Any pair >0.7 correlation? You're making the same bet twice
- **Target:** average pairwise correlation <0.3, no pair >0.5
- **Your max correlation:** ___
- **SCORE:** ___/10 (10 = max correlation <0.3)

**Check #8: Factor Exposure Overlap**
- What factors drive each strategy? (momentum, value, quality, low-vol, size)
- If 3 strategies all score high on momentum → one regime shift kills all 3
- **RED FLAG:** >60% of strategies share the same top factor
- **SCORE:** ___/10 (10 = diversified across ≥4 factors)

**Check #9: Position Sizing Consistency**
- Does your position sizing make sense across strategies?
- Kelly-based? Equal-risk? Fixed fractional?
- **RED FLAG:** Largest position >5x smallest position without deliberate sizing rationale
- **SCORE:** ___/10 (10 = consistent, risk-adjusted sizing)

**Diversification Score: ___/30**
- 25-30: Genuinely diversified
- 18-24: Some overlap, acceptable
- <18: Concentrated risk — reduce overlapping bets

---

## AUDIT STEP 4: Risk Management Review

### Your edge doesn't matter if you blow up

**Check #10: Maximum Drawdown**
- What's the historical max drawdown and how long did recovery take?
- Can you emotionally handle 2x that drawdown? (It WILL happen)
- **Your max DD:** ___% over ___ months
- **SCORE:** ___/10 (10 = max DD <20% with <6 month recovery)

**Check #11: Position Sizing at Extremes**
- Do you size down during high vol / high correlation regimes?
- Do you have a circuit breaker for portfolio-level drawdowns?
- **RED FLAG:** No mechanism to reduce exposure during market stress
- **SCORE:** ___/10 (10 = explicit volatility-adjusted sizing + portfolio circuit breaker)

**Check #12: Leverage**
- What is your total portfolio leverage (gross exposure / net equity)?
- <1.5x = conservative, 1.5-3x = moderate, >3x = aggressive
- **RED FLAG:** >3x leverage without explicit risk budget
- **Your leverage:** ___x
- **SCORE:** ___/10 (10 = <1.5x)

**Risk Score: ___/30**
- 25-30: Risk-managed
- 18-24: Acceptable with monitoring
- <18: Fix risk controls before adding capital

---

## COMPOSITE STRATEGY HEALTH SCORE

| Section | Your Score | Max | Grade |
|---|---|---|---|
| Backtest Sanity | ___ | 30 | |
| Overfitting Detection | ___ | 30 | |
| Diversification | ___ | 30 | |
| Risk Management | ___ | 30 | |
| **TOTAL** | **___** | **120** | |

### Scoring Guide:
- **100-120:** 🟢 STRONG — deploy with confidence, monitor monthly
- **80-99:** 🟡 ADEQUATE — paper trade 30 days, then go live at 50% size
- **60-79:** 🟠 WEAK — fix identified issues before live trading
- **<60:** 🔴 FAIL — do not trade. Rebuild strategy with fewer rules, better data.

---

## AUDIT ACTION PLAN

Based on your scores, the top 3 fixes to implement before live trading:

1. _______________________________
2. _______________________________
3. _______________________________

**Target completion date:** _______________
**Re-audit scheduled:** _______________

---

## AUDIT WORKBOOK TEMPLATE — EXAMPLE

**Strategy:** Tech Sector Covered Call Rotation
**Date Audited:** July 22, 2026
**Auditor:** BisonQuant Audit Framework

**Backtest Sanity:** 22/30
- Lookback covers 2019-2024 (bull + COVID crash + recovery) ✅
- Uses current NDX constituents for 2019 data ❌ (survivorship bias — missed 4 delisted stocks)
- Entry timing uses earnings dates confirmed as point-in-time ✅

**Overfitting:** 18/30
- 12 rules — borderline overfit ⚠️
- Parameter sensitivity: 37% OOS drop (poor — above 30% threshold) ❌
- Walk-forward validation: OOS Sharpe 0.62 vs in-sample 1.14 (54% retention) ⚠️

**Diversification:** 24/30
- Max pairwise correlation with other strategies: 0.41 (acceptable) ✅
- But 2 other strategies also overweight tech ⚠️
- Position sizing consistent at 2% risk per trade ✅

**Risk Management:** 26/30
- Max DD: 18.3% over 4 months ✅
- Volatility-adjusted sizing: yes ✅
- No portfolio-level circuit breaker ❌ — add one

**Composite: 90/120 — ADEQUATE 🟡**
**Action:** Simplify from 12 rules to <10. Add survivorship-bias-free data. Add portfolio circuit breaker. Paper trade 30 days, then go live at 50%.

---

*AI-Assisted Disclosure: This audit workbook was created using AI-assisted research synthesis. The methodology is based on established quantitative finance principles (walk-forward analysis, factor decomposition, correlation matrix analysis). All audit criteria are reviewed by experienced traders. This is an educational tool — not financial advice.*
