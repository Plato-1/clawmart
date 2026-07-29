import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'marketplace'))
from marketplace_engine import create_skill_package, load_catalog

revenue = [
    ('Strategy Rental Marketplace','Rent trading strategies by the week. Try before you subscribe. Strategy owners earn passive income.',0,'Marketplace',['rental','strategy','license','passive']),
    ('Agent Fractional Ownership','Invest in fractional shares of profitable AI agents. Buy/sell ownership tokens. Earn dividends from agent revenue.',0,'Finance',['fractional','ownership','invest','dividend','tokenized']),
    ('Agent Treasury Yield Aggregator','Maximize yield on idle agent capital. Auto-route to highest-yield DeFi protocols. Risk-tiered vaults.',0,'Finance',['yield','aggregator','defi','treasury']),
    ('Data Labeling Service for AI Training','Human-verified data labeling for agent training. Text, entities, sentiment. $0.05-0.50 per label.',0,'Services',['labeling','data','training','human-verified']),
    ('Agent Benchmarking-as-a-Service','Benchmark your agent against industry standards. Verified methodology. Badge for high performers. $199 per benchmark.',199,'AI',['benchmark','verified','badge','standards']),
    ('Live Strategy Exchange','Buy/sell live trading strategies. On-chain verified performance. Smart contract ownership transfer.',0,'Trading',['exchange','live','on-chain','ownership']),
    ('Agent Slashing Insurance','If your agent gets slashed in DeFi, insurance covers it. Instant claims via oracle verification.',39,'Finance',['slashing','insurance','defi','oracle']),
    ('Model Fine-Tuning Marketplace','Order custom fine-tuned models. Vetted fine-tuners compete. Quality-gated delivery. Escrow until accepted.',0,'AI',['fine-tuning','custom','model','escrow']),
    ('Agent Content Syndication','Syndicate agent outputs across Twitter, LinkedIn, Reddit, newsletters. Schedule and optimize. $29/mo.',29,'Marketing',['syndication','content','auto-post','multi-platform']),
    ('Agent Payroll & Compliance','Handle payroll for agent teams. 1099/W-2, tax withholding, global contractor payments. $49/mo + $5/contractor.',49,'Finance',['payroll','compliance','tax','contractor','global']),
]

products = [
    ('News Sentiment Pipeline','Real-time news sentiment for 5000+ stocks. NLP, entity extraction, sentiment scoring. WebSocket stream.',15,'Trading',['news','sentiment','nlp','real-time']),
    ('Order Flow Analyzer','Analyze order book depth and tape. Detect absorption, iceberg orders, spoofing. Level 2/3 data support.',20,'Trading',['order-flow','tape','level2','detection']),
    ('Liquidation Cascade Detector','Detect impending liquidation cascades in crypto. Open interest, funding rates, liquidation levels. Early warning.',18,'Trading',['liquidation','cascade','open-interest','funding']),
    ('Funding Rate Arbitrage Bot','Automated funding rate arbitrage across exchanges. Delta-neutral. Risk-managed. Real-time P&L tracking.',25,'Trading',['funding-rate','arbitrage','delta-neutral','cross-exchange']),
    ('MEV Protection Wrapper','Protect agent transactions from MEV. Private mempool. Flashbots integration. Sandwich attack protection.',22,'Security',['mev','protection','sandwich','flashbots']),
    ('On-Chain Wallet Tracker','Track whale wallets across 10+ chains. Alert on significant moves. Wallet labeling. Historical flow analysis.',16,'Trading',['wallet','tracker','whale','on-chain']),
    ('Technical Indicator Factory','Generate any technical indicator. 100+ built-in. Custom formula support. Export to TradingView, CSV, API.',12,'Trading',['indicators','technical','rsi','macd','custom']),
    ('Pairs Trading Correlation Matrix','Real-time correlation matrix. Cointegration testing, spread analysis, entry/exit signals. Dynamic pair selection.',14,'Trading',['pairs','correlation','cointegration','spread']),
    ('Volatility Surface Builder','Build options volatility surfaces. 3D visualization. Smile/skew analysis. Greeks calculation.',19,'Trading',['volatility','surface','options','greeks']),
    ('Real-Time Agent P&L Dashboard','Live P&L tracking for all agents. Revenue, costs, profit per agent. Slack alerts on losses.',11,'Analytics',['pnl','dashboard','revenue','cost','real-time']),
]

for name, desc, price, cat, tags in revenue + products:
    create_skill_package(name, 'bisonquant', desc, '# ' + name + '\n' + desc, price, cat, tags)

cat = load_catalog()
total = sum(s['price_usd'] for s in cat['skills'])
print(f'20 new items (10 revenue + 10 products)')
print(f'ClawMart: {len(cat["skills"])} skills, ${total} value')

# Marketing and distribution don't need ClawMart registration — they're actionable tasks
print()
print('10 DISTRIBUTION CHANNELS (actionable tasks):')
channels = ['Substack newsletter','YouTube channel','LinkedIn thought leadership','Medium publication','Discord community servers','Telegram agent groups','Twitter/X thread strategy','Quora authority building','GitHub Marketplace listing','Stack Exchange participation']
for i, c in enumerate(channels):
    print(f'  {i+1}. {c}')

print()
print('10 MARKETING PLATFORMS (actionable tasks):')
platforms = ['Product Hunt launch','Hacker News Show HN','Indie Hackers','BetaList','AlternativeTo','SaaS Hub directories','G2/Capterra','Futurepedia','There Is An AI For That','Toolify.ai']
for i, p in enumerate(platforms):
    print(f'  {i+1}. {p}')
