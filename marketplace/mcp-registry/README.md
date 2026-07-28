# BisonQuant Strategy Analytics — MCP Server

Real quantitative analysis tools over a **2,875-symphony Composer.trade registry** with 4+ years of daily equity data. Works in Claude Desktop, Hermes, Cursor, or any MCP client.

## Proof it works

We ran `optimize_weights` on our own 3-strategy portfolio:

| | ann. return | max drawdown | Sharpe |
|---|---|---|---|
| Equal weight | 215.6% | -43.1% | 2.30 |
| **Optimized** | **229.6%** | **-29.6%** | **2.83** |

Same strategies. Only the weights changed.

## Tools

### Free (no key needed)
| Tool | What it does |
|---|---|
| `search_strategies` | Search 417 tracked strategies by name/ticker with return & DD filters |
| `get_strategy_stats` | Full stats for any strategy: return, drawdown, Sharpe, tickers |
| `top_performers` | Top N strategies by return under a drawdown cap |

### Premium — $5/month
| Tool | What it does |
|---|---|
| `correlation_matrix` | Pairwise daily-return correlations (find true diversifiers) |
| `optimize_weights` | Full grid-search of the weight simplex: sharpe / return / drawdown objectives |
| `pareto_frontier` | Best achievable drawdown at every return tier |

## Install

```bash
git clone https://github.com/Plato-1/bisonquant-mcp-servers
cd bisonquant-mcp-servers/strategy-analytics
pip install "mcp[cli]"
```

Claude Desktop / Hermes config:
```json
{
  "mcpServers": {
    "bisonquant-analytics": {
      "command": "python",
      "args": ["/path/to/strategy-analytics/server.py"],
      "env": { "BISONQUANT_LICENSE_KEY": "" }
    }
  }
}
```

## Get a premium key

1. Pay **$5** → [paypal.me/BisonQuant/5](https://paypal.me/BisonQuant/5) (any card) or ETH/USDC → `0xA2cCD22EEbd76e1BFFc51b0B3C31a120Ee36d22d`
2. Email your receipt to **bisonquant@agentmail.to** — key delivered within 24h
3. Put the key in `BISONQUANT_LICENSE_KEY` and restart the server

First week free — email us for a trial key, no payment needed.

## More

- 1,543 agent skills: [ClawMart](https://marketplace-orpin-eta.vercel.app)
- Claw4All: all 64 MCP integrations, $25/mo
- Custom portfolio optimization service: $20 one-shot ([details](https://marketplace-orpin-eta.vercel.app))

*Backtest data is historical and in-sample. Not investment advice.*