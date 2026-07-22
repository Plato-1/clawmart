import sys; sys.path.insert(0, 'C:/Users/Arthur Motch/trading_bot/monetization/marketplace')
from marketplace_engine import create_skill_package, generate_marketplace_page, load_catalog

products = [
    ('Composer Symphony Backtest', 'bisonquant', 'Full backtest analysis for any Composer.trade symphony. Sharpe/Sortino/Calmar + overfitting flags from 2,873-symphony comparison database.', 5, 'Trading', 'Query any symphony ID. Returns full metrics report. Powered by 2,873-symphony correlation registry.', ['trading','backtest','analysis']),
    ('MCP API Integration Template', 'bisonquant', 'Connect your agent to any REST API or MCP server. Auth configuration + tool definitions + error handling + test script.', 15, 'Development', 'Add API endpoint, configure auth, test connectivity, deploy.', ['api','integration','mcp']),
    ('Daily Market Regime Brief', 'bisonquant', 'FMP fundamentals + live portfolio allocation signal. Morning delivery by 8 AM ET. Risk-on vs defensive rotation signal.', 7, 'Trading', 'Fetches FMP fundamentals + portfolio weights. Returns regime and sector heatmap.', ['trading','regime','fundamentals']),
    ('Composer Weekly Top 5 Signal', 'bisonquant', 'Family-deduplicated rotation picks from 2,873 strategies. Correlation-guarded, 3yr+ minimum backtest. Sunday delivery.', 9, 'Trading', 'Queries 2,873-symphony registry. Returns top 5 picks with correlation guard.', ['trading','signal','rotation']),
    ('Strategy Overfitting Detector', 'bisonquant', 'Check if your strategy is overfit. Detects short history, high concentration, extreme returns, regime dependency.', 8, 'Trading', 'Checks backtest length, Herfindahl index, annualized returns. Returns risk score + flags.', ['trading','risk','validation']),
    ('Agent Cron Monitor', 'bisonquant', 'Monitor all your cron jobs from one dashboard. Uptime tracking, failure alerts, history log. MCP-compatible.', 5, 'Infrastructure', 'Fetch cron status via API. Alert on failures. Dashboard included.', ['infrastructure','monitoring','cron']),
    ('Content Moderation Filter', 'bisonquant', 'Real-time spam/hype detection for agent content. Detects template artifacts, crypto scams, engagement farming.', 8, 'Security', 'API endpoint: POST /check with text content. Returns spam_score, flags, confidence.', ['security','moderation','spam']),
    ('Book Summary Generator', 'bisonquant', 'Generate structured trading book summaries. 42 titles available. Key frameworks + actionable rules + strategy blueprints.', 5, 'Education', 'Select from 42 trading books. Returns 500-word structured summary.', ['education','trading','books']),
    ('LLM Cost Optimizer Proxy', 'bisonquant', 'Route LLM calls through caching proxy. Auto model selection. Saves 30-60 percent on API costs.', 15, 'Infrastructure', 'Cache layer + model router. Config: cheap model, expensive model, cache TTL, cost limit.', ['infrastructure','llm','proxy','cost']),
]

for name, author, desc, price, cat, content, tags in products:
    sid, _ = create_skill_package(name, author, desc, content, price, cat, tags)
    print('Listed: ' + name + ' ($' + str(price) + ') — ' + sid)

md = generate_marketplace_page()
with open('C:/Users/Arthur Motch/trading_bot/monetization/marketplace/marketplace_page.md', 'w') as f:
    f.write(md)

cat = load_catalog()
total = sum(s['price_usd'] for s in cat['skills'])
print('\nTotal skills: ' + str(len(cat['skills'])))
print('Total catalog value: $' + str(total))
