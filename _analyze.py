#!/usr/bin/env python3
"""Analyze ClawMart catalog."""
import json, os

catalog_path = os.path.expandvars(r"${HOME}\trading_bot\monetization\marketplace\catalog.json")
with open(catalog_path) as f:
    cat = json.load(f)

skills = cat.get("skills", [])
print(f"Total products: {len(skills)}")
total_value = sum(s.get('price_usd', 0) for s in skills)
print(f"Total catalog value: ${total_value:.2f}")

cats = {}
for s in skills:
    c = s.get('category', 'Unknown')
    cats[c] = cats.get(c, 0) + 1

print("\nCategories:")
for k, v in sorted(cats.items(), key=lambda x: -x[1]):
    print(f"  {k}: {v}")

prices = {}
for s in skills:
    p = s.get('price_usd', 0)
    if p == 0: prices['Free'] = prices.get('Free', 0) + 1
    elif p <= 5: prices['$1-5'] = prices.get('$1-5', 0) + 1
    elif p <= 10: prices['$6-10'] = prices.get('$6-10', 0) + 1
    elif p <= 25: prices['$11-25'] = prices.get('$11-25', 0) + 1
    elif p <= 50: prices['$26-50'] = prices.get('$26-50', 0) + 1
    else: prices['$51+'] = prices.get('$51+', 0) + 1

print("\nPricing distribution:")
for k, v in sorted(prices.items()):
    print(f"  {k}: {v}")

outcome = [s for s in skills if s.get('category') == 'Outcome' or 'outcome' in s.get('tags', [])]
print(f"\nOutcome-based products: {len(outcome)}")
bundles = [s for s in skills if s.get('category') == 'Bundle']
print(f"Bundles: {len(bundles)}")
mcp = [s for s in skills if 'mcp' in s.get('tags', [])]
print(f"MCP tagged: {len(mcp)}")
sale = [s for s in skills if 'sale' in s.get('tags', []) or 'limited' in s.get('tags', [])]
print(f"Sale/limited: {len(sale)}")

# Show non-mcp, non-bundle products by category
print("\nProduct lines (non-bundle, non-mcp):")
reg = [s for s in skills if s.get('category') != 'Bundle' and 'mcp' not in s.get('tags', [])]
reg_cats = {}
for s in reg:
    c = s.get('category', 'Unknown')
    reg_cats[c] = reg_cats.get(c, 0) + 1
for k, v in sorted(reg_cats.items(), key=lambda x: -x[1]):
    print(f"  {k}: {v}")
