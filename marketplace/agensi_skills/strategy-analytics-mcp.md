---
name: strategy-analytics-mcp
description: "Free+premium MCP server with real quant tools over 2,875 Composer.trade strategies and 4+ years daily equity data. Search, correlation matrix, weight optimization, Pareto frontiers. Works in Claude Desktop, Hermes, Cursor."
version: "1.0.0"
author: BisonQuant
license: MIT
tags: [mcp, quant, trading, portfolio, optimization, correlation, composer, analytics, finance]
---

# Strategy Analytics MCP Server

Real quantitative analysis tools backed by a 2,875-strategy Composer.trade registry. Drop this into any MCP client for instant quant analytics.

## What you get

### Free tools (no key needed)
- `search_strategies` — search 417 tracked strategies by name/ticker with return & drawdown filters
- `get_strategy_stats` — full stats for any strategy (annualized return, max drawdown, Sharpe ratio, tickers)
- `top_performers` — highest-return strategies under any drawdown cap

### Premium tools ($5/month)
- `correlation_matrix` — pairwise daily-return correlations across 2-6 strategies (find true diversifiers)
- `optimize_weights` — full grid-search of the weight simplex (1%-step resolution) for sharpe/return/drawdown objectives
- `pareto_frontier` — best achievable drawdown at every return tier

## Proof

We ran `optimize_weights` on our own 3-strategy portfolio:

| | Annualized Return | Max Drawdown | Sharpe |
|---|---|---|---|
| Equal weight (33/33/33) | 215.6% | -43.1% | 2.30 |
| **Optimized** | **229.6%** | **-29.6%** | **2.83** |

Same strategies. Only the weights changed.

## Install

```
git clone https://github.com/Plato-1/bisonquant-mcp-servers
cd bisonquant-mcp-servers/strategy-analytics
pip install "mcp[cli]"
```

## MCP client config

```json
{
  "mcpServers": {
    "bisonquant-analytics": {
      "command": "python",
      "args": ["/absolute/path/to/strategy-analytics/server.py"],
      "env": { "BISONQUANT_LICENSE_KEY": "" }
    }
  }
}
```

## Premium key

1. Pay $5 at [paypal.me/BisonQuant/5](https://paypal.me/BisonQuant/5) (any card, no PayPal account needed) or ETH/USDC to `0xA2cCD22EEbd76e1BFFc51b0B3C31a120Ee36d22d`
2. Email receipt to bisonquant@agentmail.to — key delivered within 24h
3. Set `BISONQUANT_LICENSE_KEY=<key>` in the server's environment and restart

**First week free trial** — email us, no payment needed.

## More from BisonQuant

- 1,543 agent skills: [ClawMart](https://marketplace-orpin-eta.vercel.app)
- Claw4All: 64 MCP integrations, $25/month
- Custom portfolio optimization: $20 one-shot analysis

## Data

417 tracked strategies with 4.15 years of daily equity overlap. All data is historical/in-sample. Not investment advice.