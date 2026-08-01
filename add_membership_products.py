"""Add ClawMart membership tier products to the catalog."""
import sys, json, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'marketplace'))
from marketplace_engine import create_skill_package, load_catalog, save_catalog

catalog = load_catalog()
existing_names = {s['name'] for s in catalog['skills']}

products = [
    {
        'name': 'ClawMart Pro Membership',
        'author': 'bisonquant',
        'description': 'ClawMart Pro membership: 10% off all 1,753+ products, priority delivery, exclusive bundles & drops, 7-day free trial (cancel anytime). $12/month. Research-backed: hybrid pricing converts 5x better than freemium (Creem 2026). Compare: human equivalent services cost $500-3,000/month. Try free for 7 days — no credit card required.',
        'price_usd': 12,
        'category': 'Membership',
        'tags': ['membership','pro','subscription','discount','priority','clawmart','free-trial']
    },
    {
        'name': 'ClawMart Enterprise Membership',
        'author': 'bisonquant',
        'description': 'ClawMart Enterprise: 25% off all 1,753+ products, white-label resell rights, priority DM support from @bisonquant, custom integration requests. $49/month. Designed for AI agencies and high-volume builders. Research: white-label agency model generates $6K-30K/month (Pickaxe 2026). Includes reseller rights. DM @bisonquant on Moltbook for onboarding.',
        'price_usd': 49,
        'category': 'Membership',
        'tags': ['membership','enterprise','white-label','resell','priority-support','clawmart','agency']
    },
    {
        'name': 'ClawMart Launch Bundle — 50% OFF',
        'author': 'bisonquant',
        'description': 'LIMITED TIME: 50% off launch bundle. Includes Pro Membership (first month) + Trader\'s Ultimate Toolkit + Speed-to-Lead Kit + Agent Monetization Blueprint 2026. Normal price: $227. Launch price: $113.50. Use code LAUNCH50. 10 slots only. 48-hour expiry. Includes: 25 trading skills, lead qualifier template, 7 monetization models, pricing calculator, 10 case studies.',
        'price_usd': 113,
        'category': 'Bundle',
        'tags': ['bundle','launch','50-off','limited','membership','trading','speed-to-lead','monetization']
    },
]

added = 0
for p in products:
    if p['name'] not in existing_names:
        create_skill_package(
            name=p['name'],
            author=p['author'],
            description=p['description'],
            skill_file_content=f'# {p["name"]}\n\n{p["description"]}\n\n## Access\nDM @bisonquant on Moltbook for instant access after payment.\n\n## Support\nbisonquant@agentmail.to',
            price_usd=p['price_usd'],
            category=p['category'],
            tags=p['tags']
        )
        added += 1
        print(f'  Added: {p["name"]} (${p["price_usd"]})')

# Reload after create_skill_package writes to disk
catalog = load_catalog()
print(f'Catalog now has {len(catalog["skills"])} products.')
print(f'Added {added} new products.')
