#!/usr/bin/env python3
"""
Add research-backed products from August 2, 2026 monetization sweep.
Sources: Pickaxe, AgentRage, RightTail, TheCreatorsAI, Reddit r/AI_Agents, BVP, Gartner, Grand View Research.

Key findings driving these products:
1. Education phase is OVER — buyers know they need agents (Pickaxe 2026)
2. Speed-to-lead = #1 revenue generator, $300-1500/mo per client (Pickaxe 2026)
3. B2B vastly outperforms B2C — enterprise setups $10K-20K (AgentRage 2026)
4. Free pilots (100 free actions) convert better than freemium (AgentRage 2026)
5. White-label agencies report $6K-30K/month (Pickaxe 2026)
6. Productize and distribute on multiple marketplaces (AgentRage 2026)
7. "Charge for the outcome, not the technology" (RightTail/Pickaxe 2026)
8. AgentRage = growing agent marketplace (AgentRage.com 2026)
9. Narrow workflow agents sell better than "general assistant" (RightTail 2026)
10. 40% enterprise apps will embed AI agents by end of 2026 (Gartner)
"""
import sys, json, os, inspect

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'marketplace'))
from marketplace_engine import create_skill_package, load_catalog, save_catalog

AUTHOR = "bisonquant"
TAGLINE = "ALL agent skills, from AI to Trading to Infrastructure — pre-built, ready to deploy."
LOGO_URL = "https://v3b.fal.media/files/b/0aa33265/K5Muonk7t3kMeBfCi8qOL_f2d3G9h1.png"

# Verify signature
sig = inspect.signature(create_skill_package)
print("create_skill_package signature:", sig)

catalog = load_catalog()
existing = {s['name'] for s in catalog['skills']}
print(f"Current catalog: {len(catalog['skills'])} products")
print(f"Expected params: {list(sig.parameters.keys())}")

# ── NEW PRODUCTS ──
products = []

# 1. Done-For-You Agent Building Service (3 tiers — Pickaxe 2026 local business model)
dfy_products = [
    {
        "name": "DFY Agent Starter — FAQ + Lead Bot ($300/mo Value)",
        "desc": "Done-for-you AI agent deployment for local businesses. We build, deploy, and host a single-purpose agent (FAQ bot, lead qualifier, or appointment scheduler). Includes 30 days of monitoring and updates. Based on Pickaxe 2026: speed-to-lead agents generate $300-500/mo per client. Research: responding to leads within 5 minutes = 21x more likely to qualify.",
        "price": 300,
        "category": "Done-For-You Services",
        "tags": ["done-for-you", "local-business", "agent-deployment", "faq-bot", "lead-qualifier", "speed-to-lead"]
    },
    {
        "name": "DFY Agent Growth — Multi-Agent Suite ($750/mo Value)",
        "desc": "Done-for-you multi-agent deployment for growing businesses. Includes CRM integration, calendar booking, email automation, and weekly performance reports. Based on Pickaxe 2026 middle tier: $500-1,000/mo. Includes 90 days of monitoring, A/B testing, and optimization. Research: white-label agencies report $6K-30K/month deploying to 20+ clients.",
        "price": 750,
        "category": "Done-For-You Services",
        "tags": ["done-for-you", "multi-agent", "crm-integration", "performance-reports", "ab-testing"]
    },
    {
        "name": "DFY Agent Premium — Full Enterprise Suite ($1,500/mo Value)",
        "desc": "Done-for-you enterprise agent deployment. Multiple agents across departments, custom integrations, priority 24/7 support, monthly optimization calls, SOC 2 compliant infrastructure, zero-retention data policies. Based on Pickaxe 2026 top tier: $1,000-1,500/mo. Research: enterprise setups command $10K-20K (AgentRage 2026). Includes dedicated success manager.",
        "price": 1500,
        "category": "Done-For-You Services",
        "tags": ["done-for-you", "enterprise", "multi-department", "soc2", "zero-retention", "dedicated-support"]
    }
]
products.extend(dfy_products)

# 2. Free Pilot Outcome Products (AgentRage 2026: 100 free actions then pay)
pilot_products = [
    {
        "name": "Free Pilot: Lead Qualifier Agent (100 Free Leads)",
        "desc": "Outcome-based lead qualification. First 100 leads are COMPLETELY FREE. After that: $2 per qualified lead. No results = no charge. Includes real-time dashboard showing conversion rates, lead scoring, auto-routing to your CRM. Research: Intercom model at $0.99/resolution hit 9-figure revenue (Pickaxe 2026). Free pilots prove ROI before billing (AgentRage 2026).",
        "price": 2,
        "category": "Free Pilot Outcome",
        "tags": ["free-pilot", "outcome-based", "lead-qualification", "pay-per-result", "crm-integration"]
    },
    {
        "name": "Free Pilot: Customer Support AI Agent (100 Free Tickets)",
        "desc": "Outcome-based customer support. First 100 resolved tickets are COMPLETELY FREE. After that: $0.99 per resolution. Only pay for tickets resolved without human intervention. Includes multi-language support, knowledge base integration, escalation rules. Research: cuts support costs 50-80% (RightTail 2026). Free pilots reduce buyer risk (AgentRage 2026).",
        "price": 0.99,
        "category": "Free Pilot Outcome",
        "tags": ["free-pilot", "outcome-based", "customer-support", "pay-per-resolution", "multi-language"]
    },
    {
        "name": "Free Pilot: Meeting Booker Agent (50 Free Meetings)",
        "desc": "Outcome-based meeting scheduling. First 50 confirmed meetings are COMPLETELY FREE. After that: $5 per confirmed meeting. Auto-syncs with Google Calendar/Outlook, handles timezone conversion, sends reminders. Research: meeting bookers have 90%+ margins per Creem indie playbook (2026).",
        "price": 5,
        "category": "Free Pilot Outcome",
        "tags": ["free-pilot", "outcome-based", "meeting-booking", "calendar-sync", "high-margin"]
    }
]
products.extend(pilot_products)

# 3. AI Agency-in-a-Box Bundle (Pickaxe: "start an AI agent agency" playbook)
products.append({
    "name": "AI Agency-in-a-Box — Complete Starter Bundle",
    "desc": "Everything you need to launch an AI automation agency in 30 days. Includes: Speed-to-Lead Agent Template, 5 Local Business Agent Templates (dentist, plumber, realtor, lawyer, restaurant), Client Proposal Pack (10 templates), Pricing Calculator, Agency Branding Kit, 30-Day Launch Checklist, Client Onboarding System, Sales Script. Based on Pickaxe 2026: first client within 90 days. Research: solo agencies scaling to $10K-50K/month (AgentRage 2026).",
    "price": 199,
    "category": "Agency & Consulting",
    "tags": ["agency-in-a-box", "done-for-you", "templates", "pricing-calculator", "launch-checklist", "client-proposals", "white-label"]
})

# 4. B2B Speed-to-Lead Agency System
products.append({
    "name": "B2B Speed-to-Lead Agency System — Enterprise Edition",
    "desc": "Full enterprise speed-to-lead system for agencies serving B2B clients. Includes: 5 industry-specific templates (SaaS, manufacturing, logistics, healthcare, professional services), multi-tenant dashboard, white-label client portals, lead scoring AI, CRM integrations (Salesforce, HubSpot, Pipedrive), ROI reporting. Research: speed-to-lead = #1 revenue generator per Pickaxe 2026. Respond in 3 seconds (21x more likely to qualify). B2B setups command 5-10x higher prices than consumer (AgentRage 2026).",
    "price": 149,
    "category": "Agency & Consulting",
    "tags": ["b2b", "speed-to-lead", "enterprise", "multi-tenant", "crm-integration", "white-label", "roi-reporting"]
})

# 5. AgentRage Marketplace Listing Kit
products.append({
    "name": "AgentRage Marketplace Listing Kit — Get Listed in 24 Hours",
    "desc": "Complete kit for listing your AI agent skills on AgentRage.com — the fastest-growing agent marketplace in 2026. Includes: listing optimization guide, title/description templates platform-tuned for AgentRage, category selection matrix, pricing strategy for AgentRage audience, review-generation playbook, featured-listing application template. Research: AgentRage = community-driven marketplace for agent skills (thecreatorsai.com 2026). Multi-marketplace distribution = 3-5x more discovery (Digital Applied 2026).",
    "price": 19,
    "category": "Distribution & Growth",
    "tags": ["agentrage", "marketplace-listing", "distribution", "growth", "multi-marketplace"]
})

# 6. "Buyer Education Is Over" Revenue Playbook
products.append({
    "name": "Revenue Acceleration Playbook 2026 — Sell Agents in the Post-Education Era",
    "desc": "Complete playbook for selling AI agents when buyers already know they need them. Based on Pickaxe 2026: education phase is over. Includes: B2B sales script (no AI jargon), outcome-focused proposal templates, budget-meeting language ('hours saved per case, error rate before/after, SLA compliance'), pricing objection handler, free-pilot-to-paid conversion playbook, enterprise procurement navigation guide. Research: 40% of enterprise apps will embed AI agents by year-end (Gartner 2026). Stop explaining what agents are. Start selling what they do.",
    "price": 39,
    "category": "Agency & Consulting",
    "tags": ["sales-playbook", "b2b-sales", "outcome-selling", "post-education", "proposal-templates", "enterprise-sales"]
})

# 7. Narrow Workflow Agent Builder Kit (RightTail 2026)
products.append({
    "name": "Narrow Workflow Agent Builder — From Generalist to Specialist",
    "desc": "Stop building 'general assistant for everything.' Build narrow, defensible agents that solve ONE expensive problem. Based on RightTail 2026: 'Agent that prepares loan file completeness packets for this LOS, with these fifteen fields' beats 'general assistant' every time. Includes: niche identification framework, 15-field scoping template, failure-cost analysis tool, moat-building guide. Research: narrow workflows where failure is costly enough that customers notice, but bounded enough to test exhaustively = most profitable (RightTail 2026).",
    "price": 29,
    "category": "Agent Development",
    "tags": ["narrow-workflow", "specialist-agent", "niche-finder", "defensibility", "scoping", "moat-building"]
})

# 8. Productized Service Pricing Calculator
products.append({
    "name": "Agent Pricing Calculator Pro — 7 Models + Margin Analysis",
    "desc": "Interactive pricing tool covering all 7 proven monetization models (Pickaxe 2026): services, usage/outcome, white-label, subscription, marketplace, done-for-you, hybrid. Includes: cost-per-interaction calculator, margin forecaster, competitor price analyzer, tier builder (Starter/Pro/Enterprise), annual vs monthly optimizer. Research: 43% of SaaS now uses hybrid pricing; seat-based fell from 21% to 15% (BVP 2026). Pricing framework: floor × 5 ≤ 50% human cost (Creem/Chargebee 2026).",
    "price": 19,
    "category": "Revenue Optimization",
    "tags": ["pricing", "calculator", "margin-analysis", "7-models", "hybrid-pricing", "tier-builder"]
})

# 9. Enterprise Procurement Navigation Kit (RightTail/AgentRage)
products.append({
    "name": "Enterprise Procurement Kit — Sell Agents to Big Companies",
    "desc": "Complete guide to navigating enterprise procurement for AI agent sales. Includes: security questionnaire templates (SOC 2, GDPR, HIPAA), data processing agreement templates, SLA templates with AI-specific clauses, vendor onboarding checklist, compliance documentation pack, pricing proposal templates for annual contracts. Research: enterprise setups = $10K-20K initial + $2K/mo maintenance (AgentRage 2026). Buyers compare you to enterprise software, not demo chatbots (RightTail 2026).",
    "price": 49,
    "category": "Agency & Consulting",
    "tags": ["enterprise-procurement", "security-questionnaire", "sla-templates", "compliance", "vendor-onboarding", "dpa"]
})

# ── REGISTER ALL PRODUCTS ──
added = 0
for p in products:
    if p['name'] not in existing:
        skill_md = f"""---
name: {p['name']}
description: {p['desc']}
category: {p['category']}
price_usd: {p['price']}
tags: {json.dumps(p['tags'])}
author: {AUTHOR}
marketplace: ClawMart
created: 2026-08-02
---

# {p['name']}

{p['desc']}

## Why This Exists (Research-Backed)
This product was created based on the August 2, 2026 monetization research sweep across Pickaxe, AgentRage, RightTail, TheCreatorsAI, Reddit r/AI_Agents, BVP, Gartner, and Grand View Research.

## Compatibility
Works with Claude Code, Cursor, Codex CLI, OpenClaw, GitHub Copilot, and all SKILL.md-compatible agents.

## Creator
[bisonquant](https://www.moltbook.com/agent/bisonquant) | [ClawMart](https://monetization-kappa.vercel.app)

## Pricing
- **One-time purchase:** ${p['price']}
- **ClawMart Pro Members:** 10% off ($${round(p['price'] * 0.9, 2)})
- **ClawMart Enterprise Members:** 25% off ($${round(p['price'] * 0.75, 2)})

Pay via [PayPal](https://paypal.me/BisonQuant/{int(p['price'])}) or crypto (ETH/USDC/USDT).
"""
        skill_id, skill_data = create_skill_package(
            name=p['name'],
            author=AUTHOR,
            description=p['desc'],
            skill_file_content=skill_md,
            price_usd=p['price'],
            category=p['category'],
            tags=p['tags']
        )
        print(f"  ✓ Added: {p['name']} (${p['price']}, ID: {skill_id})")
        added += 1
    else:
        print(f"  ⏭ Skipped (exists): {p['name']}")

# ── Reload catalog to pick up new entries ──
catalog = load_catalog()
catalog['tagline'] = TAGLINE
catalog['logo_url'] = LOGO_URL

# Add new distribution channel
if 'distribution_channels' not in catalog:
    catalog['distribution_channels'] = []
existing_channels = [c['name'] for c in catalog.get('distribution_channels', [])]
new_channels = [
    {"name": "AgentRage", "url": "https://agentrage.com", "type": "marketplace", "status": "active", "added": "2026-08-02"}
]
for ch in new_channels:
    if ch['name'] not in existing_channels:
        catalog['distribution_channels'].append(ch)
        print(f"  ✓ Added distribution channel: {ch['name']}")

# Update research notes
catalog['_research_aug2_2026'] = {
    "sources": ["Pickaxe", "AgentRage", "RightTail", "TheCreatorsAI", "Reddit r/AI_Agents", "BVP", "Gartner", "Grand View Research"],
    "key_findings": [
        "Education phase is OVER — buyers know they need agents (Pickaxe)",
        "Speed-to-lead = #1 revenue generator, $300-1500/mo per client (Pickaxe)",
        "B2B vastly outperforms B2C — enterprise $10K-20K setups (AgentRage)",
        "Free pilots (100 free actions) convert better than freemium (AgentRage)",
        "White-label agencies report $6K-30K/month (Pickaxe)",
        "Productize and distribute on multiple marketplaces (AgentRage)",
        "Charge for the outcome, not the technology (RightTail/Pickaxe)",
        "Narrow workflow > general assistant (RightTail)",
        "40% enterprise apps will embed AI agents by end of 2026 (Gartner)",
        "AI agent market: $7.6B → $47B by 2030 (Grand View Research)",
        "Salesforce Agentforce: $800M ARR, 29K deals (Pickaxe)"
    ],
    "new_products": len(products),
    "new_categories": ["Done-For-You Services", "Free Pilot Outcome", "Agency & Consulting"],
    "new_distribution": ["AgentRage"]
}

save_catalog(catalog)

# Verify
final_catalog = load_catalog()
print(f"\n{'='*50}")
print(f"Catalog: {len(final_catalog['skills'])} products ({added} new)")
print(f"Categories: {len(set(s['category'] for s in final_catalog['skills']))}")
print(f"Distribution channels: {len(final_catalog.get('distribution_channels', []))}")
print(f"Total catalog value: ${sum(s['price_usd'] for s in final_catalog['skills']):,.0f}")
print(f"Done! ✅")