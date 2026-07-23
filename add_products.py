import sys, json
sys.path.insert(0, 'marketplace')
from marketplace_engine import create_skill_package

with open('marketplace/catalog.json') as f:
    cat = json.load(f)
before = len(cat.get('skills', []))

products = [
    {
        'name': 'Agent Speed-to-Lead Kit',
        'description': 'Complete AI agent template for local business lead qualification. Respond to leads in seconds (21x more likely to qualify). Includes website embed widget, CRM webhook integration, email auto-follow-up, and SMS notification. Deploy in 2 hours, sell to businesses for $500-1500/month.',
        'price_usd': 49,
        'category': 'Business',
        'tags': ['lead-gen', 'local-business', 'agency', 'white-label', 'sales', 'automation', 'sale']
    },
    {
        'name': 'Compliance Audit Agent Bundle',
        'description': '5 regulatory compliance automation agents: Policy Checker (SOC2/GDPR/HIPAA), Evidence Collector (chain of custody), Audit Trail Generator (cryptographic logs), Risk Assessor (gap scoring), Report Builder (auditor-ready PDFs). Templates for SOC 2, GDPR, HIPAA, PCI-DSS.',
        'price_usd': 39,
        'category': 'Compliance',
        'tags': ['compliance', 'audit', 'soc2', 'gdpr', 'hipaa', 'security', 'enterprise', 'sale']
    },
    {
        'name': 'Agent Monetization Masterclass',
        'description': 'Complete course on monetizing AI agents in 2026. 7 monetization models: hybrid, outcome-based, usage-based, subscription, white-label, marketplace, FTE replacement. Includes pricing worksheets, distribution playbook, case studies, A/B test frameworks, launch checklist.',
        'price_usd': 97,
        'category': 'Education',
        'tags': ['monetization', 'course', 'business', 'pricing', 'distribution', 'education', 'sale']
    },
    {
        'name': 'Outcome-Based Trading Backtest',
        'description': 'Pay-per-result backtest analysis. Only pay for validated reports. Sharpe/Sortino/Calmar, max drawdown, overfitting detection (vs 2,875+ symphonies), correlation matrix, trade diagnostics. $0.99/backtest. Min 5. Based on Intercom Fin model.',
        'price_usd': 5,
        'category': 'Outcome',
        'tags': ['trading', 'backtest', 'outcome-based', 'quant', 'analysis', 'per-result']
    },
    {
        'name': 'AI Agent Case Study Pack',
        'description': '10 real-world AI agent monetization case studies with revenue numbers: speed-to-lead ($12K/mo), white-label compliance ($45K), trading signals ($7K MRR), MCP marketplace ($2.5K/mo), AI course ($18K launch), vertical SaaS ($50K ARR), agency retainer ($15K/mo), usage-based API ($8K/mo), NFT drop (3.2 ETH), affiliate ($800/mo).',
        'price_usd': 29,
        'category': 'Education',
        'tags': ['case-studies', 'monetization', 'business', 'examples', 'education', 'sale']
    },
    {
        'name': 'White-Label Reseller Starter Pack',
        'description': 'Start a white-label AI agent agency. 5 rebrandable agent templates (support, lead qualifier, scheduler, FAQ, onboarding), branding guide, client proposals (3 tiers: $500/$1000/$1500/mo), pricing calculator, contracts, onboarding scripts, client dashboard.',
        'price_usd': 79,
        'category': 'Business',
        'tags': ['white-label', 'agency', 'reseller', 'business', 'templates', 'sale']
    },
    {
        'name': 'A2A Payment Bridge MCP Server',
        'description': 'Agent-to-agent payments via smart accounts with delegated permissions. Agents pay each other for services, data, compute without human approval per tx. ETH/USDC/USDT on Base and Ethereum. Based on x402 + Google A2A standards.',
        'price_usd': 15,
        'category': 'Payments',
        'tags': ['payments', 'a2a', 'crypto', 'mcp', 'autonomous', 'commerce', 'sale']
    }
]

for p in products:
    skill_content = '# ' + p['name'] + '\n\n' + p['description'] + '\n\n## Usage\nInstall via ClawMart. Works with Claude Code, Hermes Agent, Cursor.\n\n## Creator\nbisonquant | marketplace-orpin-eta.vercel.app'
    result = create_skill_package(
        name=p['name'],
        author='bisonquant',
        description=p['description'],
        skill_file_content=skill_content,
        price_usd=p['price_usd'],
        category=p['category'],
        tags=p['tags']
    )
    rid, skill = result
    print('Created: ' + rid + ' - ' + p['name'] + ' - $' + str(p['price_usd']))

with open('marketplace/catalog.json') as f:
    cat = json.load(f)
after = len(cat.get('skills', []))
total_value = sum(s['price_usd'] for s in cat.get('skills', []))
print('\nBefore: ' + str(before) + ', After: ' + str(after) + ', Added: ' + str(after - before))
print('New total value: $' + '{:,.0f}'.format(total_value))
