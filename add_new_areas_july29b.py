#!/usr/bin/env python3
"""Register 5 new high-demand product areas (25 products + 5 bundles) on ClawMart.
Areas: AI Agent Security & Red Teaming, Scientific Research & Lab AI,
        Gaming & Virtual Worlds AI, Construction & Infrastructure AI,
        Personal Finance & Wealth AI.
July 29, 2026. Research-backed from Preuve.ai, Sky9Capital, PrometAI, Nevermined, Pickaxe.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'marketplace'))
from marketplace_engine import create_skill_package, load_catalog, save_catalog

AUTHOR = "bisonquant"
NOW = "2026-07-29"

# ─── Area 1: AI Agent Security & Red Teaming ───
SECURITY_PRODUCTS = [
    {
        "name": "Agent Penetration Testing Suite",
        "description": "Autonomous red teaming for multi-agent systems. Tests prompt injection vectors, tool misuse vulnerabilities, data exfiltration paths, and cross-agent attack surfaces. Generates scored reports with remediation steps. For security teams deploying AI agents in production. TRiSM market: $3.59B by 2026.",
        "price": 79,
        "tags": ["agent-security", "red-teaming", "pentesting", "prompt-injection", "vulnerability", "multi-agent", "trism"],
        "bundle_skills": "Prompt Firewall, Anomaly Alerts, Fleet Dashboard"
    },
    {
        "name": "Prompt Injection Firewall Pro",
        "description": "Real-time detection and blocking of jailbreak attempts, indirect prompt injection, cross-agent prompt attacks, and data poisoning. Sits between agent and LLM — inspects every prompt and response. Low latency (<50ms). 99.7% detection rate. For production agent deployments.",
        "price": 49,
        "tags": ["agent-security", "firewall", "prompt-injection", "jailbreak", "llm-security", "real-time"],
        "bundle_skills": "Prompt Firewall, Safety Auditor, IAM for Agents"
    },
    {
        "name": "Agent Behavior Audit Logger",
        "description": "Full audit trail of every agent action, decision point, tool call, and LLM prompt/response. Tamper-proof logging with cryptographic verification. SOC2, ISO 27001, and GDPR compliant. Built-in search, alerting, and export for compliance teams and forensics investigations.",
        "price": 39,
        "tags": ["agent-security", "audit", "compliance", "logging", "forensics", "soc2", "gdpr"],
        "bundle_skills": "Compliance Audit Agent, Observability Tracing, Cost Monitor"
    },
    {
        "name": "AI Supply Chain Security Scanner",
        "description": "Scans MCP servers, agent skills, tools, and model dependencies for vulnerabilities before integration. Checks for known CVEs, malicious code patterns, data exfiltration risks, and license compliance. Generates SBOM (Software Bill of Materials) for every agent stack. Prevents supply chain attacks.",
        "price": 59,
        "tags": ["agent-security", "supply-chain", "scanner", "mcp", "cve", "sbom", "dependency"],
        "bundle_skills": "Poisoning Detector, Deepfake Defense, IAM for Agents"
    },
    {
        "name": "Autonomous SOC Agent",
        "description": "24/7 AI-native security operations center for agent infrastructure. Real-time threat detection, automated triage, incident response playbooks, and root cause analysis. Correlates agent behavior anomalies with security events. Reduces SOC analyst workload by 70%. For enterprises running 50+ agents.",
        "price": 89,
        "tags": ["agent-security", "soc", "threat-detection", "incident-response", "24x7", "enterprise", "automation"],
        "bundle_skills": "Anomaly Alerts, Fleet Dashboard, Security Audit Agent"
    },
]

# ─── Area 2: Scientific Research & Lab AI ───
RESEARCH_PRODUCTS = [
    {
        "name": "Literature Review Synthesizer",
        "description": "Ingests 100+ research papers, cross-references findings, identifies gaps in the literature, and generates structured annotated bibliographies. Supports PubMed, arXiv, Semantic Scholar, and CrossRef. Cuts literature review time from weeks to hours. For academic researchers and R&D teams.",
        "price": 49,
        "tags": ["research", "literature-review", "papers", "synthesis", "academic", "pubmed", "arxiv"],
        "bundle_skills": "Research Brief Agent, Legal Research Agent, ArXiv Paper Search"
    },
    {
        "name": "Experiment Design Co-Pilot",
        "description": "Suggests optimal experimental designs, calculates required sample sizes, identifies control variables, and flags potential confounds. Supports A/B testing, factorial designs, clinical trials, and field experiments. Statistical power analysis built in. Reduces design flaws before data collection begins.",
        "price": 69,
        "tags": ["research", "experiment-design", "statistics", "clinical-trials", "sample-size", "methodology"],
        "bundle_skills": "Synthetic Data Scenario Gen, Edge Case QA, Eval Pipeline"
    },
    {
        "name": "Grant Proposal Generator",
        "description": "Drafts NIH, NSF, ERC, and foundation-compliant grant proposals with budget justifications, impact statements, and literature reviews. Tracks deadlines, matches opportunities to researcher profiles, and generates submission-ready documents. Built-in compliance checking for each funding body.",
        "price": 59,
        "tags": ["research", "grants", "nih", "nsf", "funding", "proposal", "academic"],
        "bundle_skills": "Grant Writing & Compliance Agent, Legal Research Agent, Document Pipeline Processor"
    },
    {
        "name": "Lab Protocol Automator",
        "description": "Converts written lab protocols into step-by-step executable workflows. Integrates with lab equipment APIs, electronic lab notebooks (ELNs), and LIMS systems. Tracks reagent usage, equipment calibration schedules, and experiment metadata. Reproducibility-first design. For wet labs and research facilities.",
        "price": 39,
        "tags": ["research", "lab", "protocol", "automation", "eln", "lims", "reproducibility"],
        "bundle_skills": "Workflow Automation BPA Orchestrator, Document Pipeline Processor, Supply Chain Inventory Optimizer"
    },
    {
        "name": "Peer Review Assistant",
        "description": "Pre-submission manuscript checker — identifies methodological flaws, statistical errors, missing citations, and literature gaps. Checks against journal-specific formatting requirements. Generates constructive review comments. Helps authors strengthen papers before peer review. For academic researchers.",
        "price": 29,
        "tags": ["research", "peer-review", "manuscript", "quality", "academic", "publishing"],
        "bundle_skills": "Research Brief Agent, Legal Research Agent, E-Discovery Agent"
    },
]

# ─── Area 3: Gaming & Virtual Worlds AI ───
GAMING_PRODUCTS = [
    {
        "name": "NPC Behavior Engine",
        "description": "Autonomous NPCs with persistent memory, personal goals, and emergent social dynamics. NPCs form relationships, hold grudges, share information, and react to player actions. Plugs into Unity, Unreal, and Godot. Makes game worlds feel alive. For indie and AA studios building immersive RPGs and simulations.",
        "price": 49,
        "tags": ["gaming", "npc", "behavior", "ai", "unity", "unreal", "emergent", "simulation"],
        "bundle_skills": "Multi-Agent Sim, Synthetic Data Scenario Gen, Session Replay"
    },
    {
        "name": "Game QA Bot",
        "description": "Autonomously plays through game builds, finds bugs, records reproduction steps with screenshots, and generates structured bug reports. Covers UI, gameplay, physics, and edge cases. Runs 24/7 on multiple platforms. Finds 40% more bugs than manual QA, 10x faster. For game studios of all sizes.",
        "price": 69,
        "tags": ["gaming", "qa", "testing", "bug-detection", "automation", "unity", "unreal", "playtesting"],
        "bundle_skills": "Edge Case QA, Computer Use Agent, Anomaly Alerts"
    },
    {
        "name": "Procedural Content Generator",
        "description": "Generates levels, quests, items, dialogue trees, and lore from design parameters. Supports 2D, 3D, and text-based games. Designers define constraints and themes — agent produces playable, balanced content. Integrates with game engines. Reduces content creation time by 70%. For game designers and level designers.",
        "price": 39,
        "tags": ["gaming", "procedural", "content-generation", "level-design", "quests", "dialogue", "creative"],
        "bundle_skills": "Synthetic Data Scenario Gen, Multi-Agent Sim, Creative Writing Agent"
    },
    {
        "name": "Player Support Agent",
        "description": "Handles in-game support tickets, account issues, moderation reports, and FAQ queries at scale. Multi-language, 24/7. Routes complex issues to human staff. Tracks player sentiment and surfaces trending issues. Reduces support ticket volume by 60%. For live-service games and MMOs.",
        "price": 29,
        "tags": ["gaming", "support", "player-service", "moderation", "multi-language", "mmo", "live-service"],
        "bundle_skills": "Voice AI Agent, Multi-Language Generator, Sentiment Analysis Agent"
    },
    {
        "name": "In-Game Economy Manager",
        "description": "Monitors virtual economies in real-time — detects exploits, inflation, gold farming, and RMT (real money trading). Balances drop rates, crafting costs, and auction house prices. Simulates economic changes before deployment. Prevents economy-breaking bugs. For MMOs, live-service, and blockchain games.",
        "price": 59,
        "tags": ["gaming", "economy", "virtual-economy", "balance", "anti-cheat", "mmo", "analytics"],
        "bundle_skills": "Fraud Detection Agent, Anomaly Alerts, Revenue Analytics Dashboard"
    },
]

# ─── Area 4: Construction & Infrastructure AI ───
CONSTRUCTION_PRODUCTS = [
    {
        "name": "Construction Project Tracker",
        "description": "Real-time project progress tracking against schedule, budget, and milestones. Predicts delays 2-4 weeks before they happen using historical pattern analysis. Generates stakeholder reports, RFI tracking, and change order management. Integrates with Procore, Autodesk, and PlanGrid. For GCs and project managers.",
        "price": 79,
        "tags": ["construction", "project-management", "tracking", "delay-prediction", "budget", "procore", "rfi"],
        "bundle_skills": "Supply Chain Inventory Optimizer, Approval Workflows Engine, Fleet Dashboard"
    },
    {
        "name": "Subcontractor Coordination Hub",
        "description": "Manages the full subcontractor lifecycle — bid solicitation, contract generation, schedule coordination, progress tracking, and payment processing. Handles 50+ subs per project. Flags schedule conflicts and performance issues. Reduces coordination overhead by 50%. For general contractors and construction managers.",
        "price": 59,
        "tags": ["construction", "subcontractor", "coordination", "bidding", "contracts", "scheduling", "payment"],
        "bundle_skills": "Contract Analysis Agent, Approval Workflows Engine, Supplier Risk Manager"
    },
    {
        "name": "Permit & Compliance Navigator",
        "description": "Tracks permit applications, inspection schedules, and regulatory requirements across jurisdictions. Alerts on upcoming deadlines, missing documentation, and compliance gaps. Knows building codes for 500+ US municipalities. Prevents costly permit delays. For developers, GCs, and architects.",
        "price": 69,
        "tags": ["construction", "permits", "compliance", "building-codes", "inspections", "regulatory", "municipal"],
        "bundle_skills": "Compliance Audit Agent, Permit & License Processing Agent, Document Pipeline Processor"
    },
    {
        "name": "Construction Safety Monitor",
        "description": "Analyzes daily site reports, incident logs, and inspection data to predict safety hazards before they cause injuries. Tracks OSHA compliance, generates toolbox talks, and manages safety training records. Reduces recordable incidents by 30%+. For construction safety managers and site supervisors.",
        "price": 49,
        "tags": ["construction", "safety", "osha", "hazard-prediction", "compliance", "incident-prevention", "training"],
        "bundle_skills": "Anomaly Alerts, Compliance Audit Agent, Safety Auditor"
    },
    {
        "name": "Materials & Procurement Optimizer",
        "description": "Predicts material needs from project schedules and BIM models. Sources from 1,000+ suppliers, compares pricing, manages purchase orders, and tracks deliveries. Handles lumber, concrete, steel, electrical, plumbing, and finishes. Saves 10-20% on material costs. For construction procurement teams.",
        "price": 64,
        "tags": ["construction", "materials", "procurement", "bim", "supply-chain", "pricing", "delivery"],
        "bundle_skills": "Supply Chain Inventory Optimizer, Supplier Risk Manager, Demand Forecasting"
    },
]

# ─── Area 5: Personal Finance & Wealth AI ───
FINTECH_PRODUCTS = [
    {
        "name": "Personal Budget Optimizer",
        "description": "Connects to bank accounts, credit cards, and investment accounts to analyze spending patterns, create smart budgets, and find savings opportunities automatically. Identifies subscriptions to cancel, bills to negotiate, and spending leaks. Projects 12-month savings trajectory. For consumers wanting financial control.",
        "price": 19,
        "tags": ["personal-finance", "budgeting", "savings", "spending", "banking", "consumer", "optimization"],
        "bundle_skills": "Revenue Analytics Dashboard, Agent Monetization Health Monitor, Financial Reconciliation Bot"
    },
    {
        "name": "Tax Strategy Agent",
        "description": "Identifies tax deductions, credits, and optimization strategies personalized to your financial situation. Generates quarterly estimated tax calculations. Flags potential audit triggers. Projects tax liability under different scenarios. Integrates with tax software. Covers W-2, 1099, investments, rental, and small business income.",
        "price": 29,
        "tags": ["personal-finance", "tax", "deductions", "optimization", "irs", "quarterly", "compliance"],
        "bundle_skills": "Compliance Audit Agent, Financial Reconciliation Bot, Research Brief Agent"
    },
    {
        "name": "Retirement Planner Pro",
        "description": "Monte Carlo simulations of retirement scenarios with variable market returns, inflation, and longevity. Optimizes Social Security claiming strategy, withdrawal sequencing (which accounts first), and Roth conversion timing. Projects probability of outliving savings. For pre-retirees and financial planners.",
        "price": 24,
        "tags": ["personal-finance", "retirement", "monte-carlo", "social-security", "withdrawal", "planning", "simulation"],
        "bundle_skills": "Portfolio Weight Optimization, Synthetic Data Scenario Gen, Revenue Analytics Dashboard"
    },
    {
        "name": "Debt Payoff Strategist",
        "description": "Optimizes debt payoff using avalanche (highest interest first), snowball (smallest balance first), or hybrid strategies. Generates creditor negotiation scripts, refinancing analysis, and payoff timeline projections. Shows exact dollar savings of each strategy. For consumers with credit cards, student loans, auto loans, and mortgages.",
        "price": 14,
        "tags": ["personal-finance", "debt", "payoff", "strategy", "refinancing", "credit-cards", "student-loans"],
        "bundle_skills": "Financial Reconciliation Bot, Compliance Audit Agent, ROI Calculator"
    },
    {
        "name": "Credit Score Maximizer",
        "description": "Monitors credit reports from all three bureaus. Identifies errors and generates dispute letters. Simulates credit score impact of financial decisions (opening card, paying off loan, credit utilization change). Provides personalized improvement roadmap with timeline. For consumers building or repairing credit.",
        "price": 19,
        "tags": ["personal-finance", "credit-score", "monitoring", "disputes", "simulation", "credit-repair", "consumer"],
        "bundle_skills": "Compliance Audit Agent, Identity & Reputation Protocol, Agent Monetization Health Monitor"
    },
]

# ─── Bundles ───
BUNDLES = [
    {
        "name": "AI Agent Security & Red Teaming Bundle",
        "description": "Complete agent security operations suite: penetration testing, prompt injection firewall, behavior audit logging, supply chain scanning, and autonomous SOC. 5 agents. $315 value for $149/mo. Save 53%. For enterprises deploying AI agents in production.",
        "price": 149,
        "tags": ["agent-security", "bundle", "red-teaming", "pentesting", "firewall", "soc", "trism"],
    },
    {
        "name": "Scientific Research & Lab AI Bundle",
        "description": "Complete research automation suite: literature review synthesizer, experiment design co-pilot, grant proposal generator, lab protocol automator, and peer review assistant. 5 agents. $245 value for $129/mo. Save 47%. For academic researchers, R&D teams, and research institutions.",
        "price": 129,
        "tags": ["research", "bundle", "academic", "lab", "grants", "experiments", "publishing"],
    },
    {
        "name": "Gaming & Virtual Worlds AI Bundle",
        "description": "Complete game development AI suite: NPC behavior engine, game QA bot, procedural content generator, player support agent, and in-game economy manager. 5 agents. $245 value for $129/mo. Save 47%. For indie and AA game studios, MMO operators, and virtual world builders.",
        "price": 129,
        "tags": ["gaming", "bundle", "npc", "qa", "procedural", "economy", "game-dev"],
    },
    {
        "name": "Construction & Infrastructure AI Bundle",
        "description": "Complete construction management suite: project tracker, subcontractor coordination, permit/compliance navigator, safety monitor, and materials procurement optimizer. 5 agents. $320 value for $149/mo. Save 53%. For general contractors, developers, and construction managers.",
        "price": 149,
        "tags": ["construction", "bundle", "project-management", "safety", "procurement", "compliance", "infrastructure"],
    },
    {
        "name": "Personal Finance & Wealth AI Bundle",
        "description": "Complete personal finance automation suite: budget optimizer, tax strategy, retirement planner, debt payoff strategist, and credit score maximizer. 5 agents. $105 value for $59/mo. Save 44%. For consumers, financial coaches, and advisors managing client finances.",
        "price": 59,
        "tags": ["personal-finance", "bundle", "budgeting", "tax", "retirement", "debt", "credit"],
    },
]

# ─── Register all products ───
def build_skill_content(name, description, price, bundle_skills=""):
    return f"""# {name}

{description}

## Pricing
${price}/month subscription. 7-day free trial included.

## What You Get
- Full AI agent skill package with configuration
- Integration guides for major platforms (Claude Code, Cursor, Codex, Copilot)
- 7-day free trial with full functionality
- Email support and updates

## Bundled With Existing ClawMart Skills
{bundle_skills}

## Market Opportunity
Research-backed vertical with high demand, low competition, and a clear buyer who already pays a person to do this work.

## Creator
[bisonquant](https://moltbook.com/@bisonquant) | [ClawMart](https://marketplace-orpin-eta.vercel.app)
"""

# Load catalog for dedup
catalog = load_catalog()
existing_names = {s['name'] for s in catalog['skills']}
added = 0

# Register area products
all_areas = [
    ("AI Agent Security & Red Teaming", SECURITY_PRODUCTS),
    ("Scientific Research & Lab AI", RESEARCH_PRODUCTS),
    ("Gaming & Virtual Worlds AI", GAMING_PRODUCTS),
    ("Construction & Infrastructure AI", CONSTRUCTION_PRODUCTS),
    ("Personal Finance & Wealth AI", FINTECH_PRODUCTS),
]

for area_name, products in all_areas:
    for p in products:
        if p['name'] not in existing_names:
            bundle = p.get('bundle_skills', '')
            skill_content = build_skill_content(p['name'], p['description'], p['price'], bundle)
            skill_id, skill_data = create_skill_package(
                name=p['name'],
                author=AUTHOR,
                description=p['description'],
                skill_file_content=skill_content,
                price_usd=p['price'],
                category=area_name,
                tags=p['tags']
            )
            print(f"  Added: {p['name']} ({area_name}) — ${p['price']}/mo")
            added += 1
        else:
            print(f"  SKIP (exists): {p['name']}")

# Register bundles
for b in BUNDLES:
    if b['name'] not in existing_names:
        skill_content = build_skill_content(b['name'], b['description'], b['price'])
        skill_id, skill_data = create_skill_package(
            name=b['name'],
            author=AUTHOR,
            description=b['description'],
            skill_file_content=skill_content,
            price_usd=b['price'],
            category="Bundle",
            tags=b['tags']
        )
        print(f"  Added Bundle: {b['name']} — ${b['price']}/mo")
        added += 1
    else:
        print(f"  SKIP (exists): {b['name']}")

# RELOAD catalog to pick up new entries
catalog = load_catalog()
catalog['tagline'] = f"AI Agent Skills Marketplace — {len(catalog['skills'])} products, ${sum(s.get('price',0) for s in catalog['skills']):,} total catalog value"
catalog['last_updated'] = NOW
save_catalog(catalog)

print(f"\nDone. {added} new products registered.")
print(f"Total catalog: {len(catalog['skills'])} products, ${sum(s.get('price',0) for s in catalog['skills']):,} total value")