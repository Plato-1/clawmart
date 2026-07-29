# AI Options Greeks Cheat Sheet + 50 ChatGPT Prompts

## THE ONE-PAGE GREEKS REFERENCE

### DELTA (Δ) — Directional Exposure
- Range: 0 to 1.0 (calls) / -1.0 to 0 (puts)
- ATM options: ~0.50 delta
- Deep ITM: approaches ±1.0
- Deep OTM: approaches 0
- **What it means:** For every $1 the stock moves, the option price moves by Δ dollars
- **Trader's use:** Delta = approximate probability of expiring ITM (e.g., 0.30 delta ≈ 30% chance)

### GAMMA (Γ) — Delta's Rate of Change
- Highest at-the-money, near expiration
- **What it means:** How fast delta changes when the stock moves
- **Trader's use:** High gamma = position needs frequent rebalancing. Gamma risk kills short-gamma traders during fast moves.

### THETA (Θ) — Time Decay
- Always negative for long options (time is your enemy)
- Accelerates in final 30 days (non-linear decay)
- Highest for ATM options
- **What it means:** Dollar amount lost per day from time decay
- **Trader's use:** Theta sellers (covered calls, iron condors) earn this. Theta buyers (long calls/puts) pay this daily.

### VEGA (ν) — Volatility Sensitivity
- Highest for ATM, longer-dated options
- **What it means:** Dollar change for every 1% move in implied volatility
- **Trader's use:** Long vega = you want vol to spike. Short vega = you profit as vol crushes.

### RHO (ρ) — Interest Rate Sensitivity
- Most relevant for long-dated, deep ITM options
- **What it means:** Dollar change for every 1% move in risk-free rate
- **Trader's use:** Minor impact for most retail traders. Matters for LEAPS and portfolio margin.

---

## 50 AI PROMPTS FOR OPTIONS TRADERS

### SECTION 1: STRATEGY ANALYSIS (15 prompts)

**Prompt 1 — Covered Call Analysis**
"Analyze this covered call position: Long [X] shares of [TICKER] at $[PRICE], short [X] [STRIKE] calls for $[PREMIUM] expiring [DATE]. Calculate: max profit, max loss, breakeven, probability of assignment, and annualized return if called away. Compare to buy-and-hold return."

**Prompt 2 — Cash-Secured Put Analysis**
"I want to sell a cash-secured put on [TICKER] at the $[STRIKE] strike expiring [DATE] for $[PREMIUM]. The stock is at $[PRICE]. Calculate my annualized return if the put expires worthless. Also calculate my effective purchase price and breakeven if assigned."

**Prompt 3 — Iron Condor Risk/Reward**
"Analyze this iron condor on [TICKER] with [DATE] expiration: Short $[LOWER_PUT]/Long $[LOWER_PUT_PROTECTION] puts, Short $[UPPER_CALL]/Long $[UPPER_CALL_PROTECTION] calls. Premium collected: $[CREDIT]. Calculate: max profit, max loss, probability of profit, breakevens, and the strike width to premium ratio."

**Prompt 4 — Credit Spread Comparison**
"Compare two credit spreads on [TICKER]: (A) [STRIKE_A] put spread for $[CREDIT_A] with [WIDTH_A]-wide strikes, and (B) [STRIKE_B] put spread for $[CREDIT_B] with [WIDTH_B]-wide strikes. Which has better risk/reward? Calculate expected value assuming [DELTA_PROB]% probability of max profit."

**Prompt 5 — Butterfly Spread Setup**
"Design a butterfly spread on [TICKER] centered at $[STRIKE] for [DATE] expiration. I want to spend no more than $[MAX_DEBIT] and target a profit zone of ±[WIDTH]%. What strikes should I use?"

**Prompt 6 — Calendar Spread Analysis**
"Analyze a calendar spread: Long [STRIKE] call expiring [DATE_LONG] vs Short [STRIKE] call expiring [DATE_SHORT] on [TICKER] at $[PRICE]. Debit paid: $[COST]. What implied volatility shift benefits this position? What is my profit at expiration of the short leg assuming unchanged IV?"

**Prompt 7 — Straddle Earnings Play**
"[TICKER] reports earnings on [DATE]. The at-the-money straddle expiring the next day costs $[PREMIUM]. The average post-earnings move over the last 8 quarters is ±[MOVE]%. Does the straddle premium overprice or underprice the expected move? Is this a buy or sell?"

**Prompt 8 — Strangle Optimization**
"I want to sell a strangle on [TICKER] at strikes with approximately 0.16 delta each. The stock is at $[PRICE], [DATE] expiration. What are the optimal strike prices? Calculate max profit, margin requirement, and breakevens."

**Prompt 9 — Ratio Spread Analysis**
"Analyze a 1x2 ratio call spread on [TICKER]: Buy 1 $[LOWER_STRIKE] call, sell 2 $[HIGHER_STRIKE] calls, [DATE] expiration. Net debit: $[COST]. Under what scenarios is this profitable? What is the risk if the stock rallies through the short strikes?"

**Prompt 10 — Collar Strategy Setup**
"Design a zero-cost collar for [TICKER] at $[PRICE]: Buy a protective put at $[PUT_STRIKE], sell a covered call at $[CALL_STRIKE] to offset the put cost, [DATE] expiration. What strikes achieve a zero or near-zero net cost? What is my max gain and max loss?"

**Prompt 11 — Poor Man's Covered Call (PMCC / Diagonal)**
"Set up a PMCC on [TICKER]: Long [LONG_DATE] $[LONG_STRIKE] call (LEAPS), short [SHORT_DATE] $[SHORT_STRIKE] call. Calculate the net debit, maximum profit scenarios, and breakeven. How does this compare to a traditional covered call?"

**Prompt 12 — Jade Lizard Analysis**
"Analyze a Jade Lizard on [TICKER] with [DATE] expiration: Short $[PUT_STRIKE] put, short $[CALL_STRIKE] call spread (sell call, buy higher call). Net credit: $[CREDIT]. Confirm there is no upside risk. Calculate max profit and downside breakeven."

**Prompt 13 — Put Backspread Setup**
"I am bearish on [TICKER] at $[PRICE] but want defined risk. Design a put backspread: sell 1 $[ATM_PUT], buy 2 $[OTM_PUT], [DATE] expiry. What is my ideal scenario, and at what price does the position become profitable?"

**Prompt 14 — Synthetic Long Stock**
"Show me the synthetic equivalent of buying 100 shares of [TICKER] using options: buy 1 $[STRIKE] call, sell 1 $[STRIKE] put, [DATE] expiration. What is the cost compared to buying stock outright? Account for dividends and interest."

**Prompt 15 — Risk Reversal**
"Analyze a risk reversal on [TICKER]: sell 1 OTM put, buy 1 OTM call, zero cost, [DATE] expiration. At what strikes is this zero-cost? What is my delta exposure and what does this position tell me about the options market's skew?"

### SECTIONS 2-5: (Risk Assessment 10 prompts, Position Sizing 10 prompts, Greeks Interpretation 10 prompts, Market Regime 5 prompts)
[Full 50 prompts available in the complete PDF — this is the draft structure showing the depth and quality]

---

## WORKED EXAMPLE: Real Covered Call Analysis

Sarah runs a covered call strategy on AAPL. Stock is at $195, she wants to sell the $200 call expiring in 30 days for $3.50 premium.

She opens ChatGPT, loads Prompt #1 from this pack, and pastes:
- Long 100 AAPL @ $195
- Short 1 AAPL 200C @ $3.50, 30 DTE

**AI Output:**
- Max Profit: $200 - $195 + $3.50 = $8.50 per share ($850 total)
- Max Loss: $195 - $3.50 = $191.50 per share if AAPL goes to $0
- Breakeven: $191.50 (stock can fall $3.50 before she loses money)
- If Called Away: $200 sale price + $3.50 premium = $203.50 effective exit (4.4% in 30 days, 53% annualized)
- If Not Called: She keeps $350 premium and 100 shares; annualized return on capital at risk = $350/$19,150 × 12 = 21.9%

The AI flags: AAPL's 50-day MA is at $188 — her breakeven of $191.50 is ABOVE the 50-MA, meaning the stock has room to pull back without the trade turning negative. This is a bullish signal she hadn't considered. She adjusts next month's strike to $205 for more upside potential.

**Time saved: 90 seconds vs 20 minutes of manual calculation.**

---

*AI-Assisted Disclosure: This product was created with AI assistance for research synthesis and content organization. All trading concepts, examples, and strategies are reviewed by experienced traders. This is educational content — not financial advice.*
