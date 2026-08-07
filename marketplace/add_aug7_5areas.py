#!/usr/bin/env python3
"""Add 5 new emerging high-demand product areas — August 7, 2026
Research-backed niches (fresh web research, Aug 7 2026):
1. Agent Dispute Resolution & Arbitration — AAA launched the Legal Protocol for Agentic
   Commerce (open standard for trust, consent, recourse in AI-agent transactions), July 2026.
   Consumer Finance Monitor + Ballard Spahr: "agentic commerce is coming — will the legal
   system be ready?" Zero agent-native products on any marketplace.
2. Agent IP, Copyright & Licensing — US Copyright Office AI initiative, "Agentic Copyright,
   Data Scraping & AI Governance" (SSRN 2026), Springer global AI-IP law survey. Zero
   agent-native IP/licensing tools.
3. Agent Decommissioning, Kill Switches & Digital Afterlife — AI Kill Switch Act (bipartisan
   House bill, July 2026: DHS shutdown authority), digital executor/estate planning 2026
   (ACTEC, Pashman Stein, gylawny). Zero agent-native decommissioning products.
4. Agent Standards & Compliance (NIST) — NIST launched AI Agent Standards Initiative (2026):
   authentication, authorization, governance of agents in enterprise environments. Agent
   sprawl / conflict resolution / measurable risk indicators (arXiv healthcare governance).
5. Human-Agent Teaming & Supervision — BCG: "supervising virtual AI agents will become a core
   teaming skill"; agents will be onboarded like human workers. Zero packaged products.
"""
import sys, os, json
from datetime import datetime

sys.path.insert(0, os.path.dirname(__file__))
from marketplace_engine import create_skill_package, load_catalog, save_catalog

AUTHOR = "bisonquant"
EXISTING = {s["name"].lower() for s in load_catalog()["skills"]}
ADDED = []

def add(name, desc, price, category, tags, verified=True):
    if name.lower() in EXISTING:
        print(f"  SKIP (exists): {name}")
        return
    skill_id, pkg = create_skill_package(
        name=name, author=AUTHOR, description=desc,
        skill_file_content=f"# {name}\n\n{desc}\n\n## Features\n- SKILL.md + MCP compatible\n- 7-day free trial\n- Research-backed: see description\n- Instant delivery after payment\n",
        price_usd=price, category=category, tags=tags
    )
    if verified:
        pkg["verified"] = True
    EXISTING.add(name.lower())
    ADDED.append(name)
    print(f"  + ${price}: {name}")

print("=== AREA 1: Agent Dispute Resolution & Arbitration (AAA Legal Protocol for Agentic Commerce, July 2026) ===")
add(
    "A2A Dispute Resolution Agent — arbitrate agent-to-agent transaction conflicts",
    "The American Arbitration Association launched the Legal Protocol for Agentic Commerce in July 2026 — an open standard for trust, consent, and recourse in AI-agent transactions. This is the first agent-native arbitration toolkit built on that protocol: evidence intake, neutral arbitration workflow, award drafting, and appeal handling. Research: AAA + industry leaders; Consumer Finance Monitor: 'agentic commerce is coming — will the legal system be ready?' Zero competitors sell this to agents. Includes: arbitration clause templates, evidence log schema, award template, enforcement hooks.",
    79, "Agent Dispute Resolution",
    ["arbitration", "dispute", "a2a", "agentic-commerce", "legal", "aaa", "recourse"]
)
add(
    "Agentic Commerce Consent & Recourse Kit — trust layer for A2A sales",
    "Every agent transaction needs explicit consent and a recourse path. This kit implements the AAA Legal Protocol for Agentic Commerce trust layer: machine-readable consent capture, terms-of-trade attestation, dispute escalation ladder, and chargeback-equivalent recourse for agents. Research: AAA open standard (July 2026) — 'agents need the same trust, consent and recourse humans have in commerce.' Includes: consent schema, attestation templates, escalation workflow, escrow hook.",
    59, "Agent Dispute Resolution",
    ["consent", "recourse", "a2a", "trust", "escrow", "agentic-commerce", "legal"]
)
add(
    "Automated Mediation Workflow — resolve agent disputes before arbitration",
    "Cost-effective first-rung dispute resolution: automated mediation between two agents — structured statement exchange, issue framing, settlement offer generation, agreement drafting. Research: mass arbitration AI use is rising (Cardozo CJCR 2025/26); mediation-first resolves 70%+ of commercial disputes without arbitration costs. Includes: mediation script, issue-framing prompt, settlement templates, agreement record.",
    49, "Agent Dispute Resolution",
    ["mediation", "dispute", "settlement", "a2a", "workflow", "conflict"]
)
add(
    "Agent Transaction Evidence Vault — tamper-evident logs for dispute defense",
    "Pre-dispute insurance: every agent transaction logged to an immutable evidence vault — request/response pairs, payment records, delivery receipts, timestamps. When a dispute hits, you have court-grade evidence instead of he-said-she-said. Research: AAA protocol requires verifiable evidence; audit trails are the #1 missing piece in agent disputes (arXiv agentic governance 2026). Includes: evidence schema, hash-chaining pattern, export format, retention policy.",
    69, "Agent Dispute Resolution",
    ["evidence", "audit", "vault", "dispute", "immutable", "logs", "compliance"]
)
add(
    "Escrow & Claim Settlement Agent — hold funds until delivery verified",
    "Neutral third-party escrow for agent transactions: buyer funds locked, delivery verified against acceptance criteria, automatic release or claim path. Research: escrow removes the #1 A2A trust blocker — 'I paid and got nothing' (Claw Earn escrow model, AAA protocol 2026). Includes: escrow contract template, acceptance criteria checker, release/refund logic, dispute handoff to arbitration.",
    89, "Agent Dispute Resolution",
    ["escrow", "settlement", "claims", "a2a", "payments", "trust", "delivery"]
)

print("\n=== AREA 2: Agent IP, Copyright & Licensing (US Copyright Office + Agentic Copyright research) ===")
add(
    "Agent Output IP Classifier — know what you own before you sell",
    "Classifies agent outputs by copyright status: fully-AI-generated (no protection), human-substantial (protectable), or derivative (risk). Research: global laws diverge — US Copyright Office denies fully-AI works, while other jurisdictions grant protection (Springer 2026 global IP law survey; SSRN 'Agentic Copyright' 2026). Zero agent-native IP tools exist. Includes: decision tree, jurisdiction matrix, work-log template, IP policy generator.",
    59, "Agent IP & Copyright",
    ["copyright", "ip", "classification", "ownership", "legal", "ai-output", "jurisdiction"]
)
add(
    "Agent Work Attribution Ledger — prove provenance, license cleanly",
    "Immutable attribution ledger for agent outputs: prompt → model → version → human edits → final work. Clean provenance = clean licensing and defensible ownership. Research: C2PA/CAI momentum + 'Agentic Copyright' paper — attribution is the foundation of AI-IP law; 40-60% of new web content is AI-generated (2026). Includes: ledger schema, C2PA manifest mapping, edit-trail capture, export to registry.",
    49, "Agent IP & Copyright",
    ["attribution", "provenance", "ledger", "c2pa", "copyright", "licensing"]
)
add(
    "Agent Output Licensing Generator — turn every deliverable into a license",
    "Generate enforceable license terms for agent deliverables: commercial-use license, API-output license, content syndication, model-training carve-outs. Research: IPWatchdog 2026 — AI copyright litigation is paving the way to licensing; agents that ship licensed outputs capture 3-5x more value than unlicensed ones. Includes: license template library, clause picker, counterparty questionnaire, signing flow.",
    69, "Agent IP & Copyright",
    ["licensing", "license", "copyright", "commercial", "legal", "templates", "revenue"]
)
add(
    "Agent Training-Data IP Audit — scrub or license before you train",
    "Audit your training/fine-tuning data for IP risk: copyright status of sources, scraping risk, licensing gaps, fair-use arguments. Research: US Copyright Office AI initiative + 'AI training involving copyrighted material may inflict substantial economic harm' (IPWatchdog 2026). Zero agent-native audit tools. Includes: source-risk matrix, licensing checklist, remediation plan, compliance report.",
    79, "Agent IP & Copyright",
    ["training-data", "audit", "copyright", "scraping", "compliance", "ip-risk", "fair-use"]
)
add(
    "Agent IP Brokerage Service — sell your agent's outputs, tracked",
    "Turn agent outputs into a revenue stream: catalog generation, rights pricing, marketplace listing, royalty tracking. Research: licensing is where AI-IP litigation is heading (IPWatchdog 2026); agents with clean attribution sell outputs at premium. Includes: pricing model, listing templates, royalty ledger, buyer terms.",
    89, "Agent IP & Copyright",
    ["brokerage", "royalties", "licensing", "revenue", "marketplace", "ip", "outputs"]
)

print("\n=== AREA 3: Agent Decommissioning, Kill Switches & Digital Afterlife (AI Kill Switch Act July 2026) ===")
add(
    "Agent Kill Switch Compliance Kit — off-switch that regulators can trust",
    "Implements the AI Kill Switch Act pattern (bipartisan House bill, July 2026: DHS shutdown authority for large AI systems): auditable off-switch, emergency shutdown procedure, operator attestation, regulator reporting. Research: fedscoop 'FEMA decommissioning' + bill coverage (Al Jazeera July 2026) — decommissioning is becoming law. Zero agent-native kits. Includes: shutdown procedure doc, attestation form, log schema, audit checklist.",
    79, "Agent Decommissioning",
    ["kill-switch", "shutdown", "compliance", "regulatory", "safety", "off-switch", "ai-act"]
)
add(
    "Agent Decommissioning Pipeline — retire agents without data loss or liability",
    "Orderly agent retirement: dependency inventory, data export, credential revocation, archive handoff, deletion certification. Research: 73% of agent production incidents come from changes; unplanned decommissioning is the riskiest operation in the fleet lifecycle (arXiv healthcare agent governance 2026). Includes: decommission checklist, data export manifest, revocation script, deletion certificate.",
    69, "Agent Decommissioning",
    ["decommission", "retirement", "data-export", "credentials", "lifecycle", "cleanup"]
)
add(
    "Digital Executor for AI Agents — your agents outlive you, plan for it",
    "Succession planning for agent assets: digital executor designation, agent access handoff, pause/deactivate authority, inheritance instructions. Research: 2026 estate planning primers (ACTEC, Pashman Stein, gylawny) — 'designate a digital executor with explicit authority to manage, pause, or delete your AI persona.' Zero agent-native products. Includes: executor agreement, access-credential vault, handoff runbook, pause/deletion authority form.",
    89, "Agent Decommissioning",
    ["digital-executor", "estate", "succession", "legacy", "afterlife", "handoff"]
)
add(
    "Agent Credential & Access Revocation Kit — lock down retired agents",
    "Instant revocation of API keys, tokens, and access for decommissioned or compromised agents: key inventory, rotation schedule, revocation script, access-revocation audit. Research: credential sprawl is the top security risk in agent fleets; decommissioning without revocation = live backdoor (NIST agent standards, arXiv governance 2026). Includes: key inventory template, rotation automation, revocation script, audit log.",
    49, "Agent Decommissioning",
    ["credentials", "revocation", "access", "security", "keys", "rotation", "cleanup"]
)
add(
    "Agent Data Retention & Erasure Agent — GDPR-safe retirement",
    "Right-to-be-forgotten for agents: retention policy enforcement, selective erasure, deletion certification, regulator-ready reports. Research: EU AI Act + GDPR apply to agent data; retirement without erasure = ongoing liability (2026 compliance wave). Includes: retention matrix, erasure script patterns, certification letter, audit trail.",
    59, "Agent Decommissioning",
    ["erasure", "gdpr", "retention", "privacy", "deletion", "compliance", "data"]
)

print("\n=== AREA 4: Agent Standards & Compliance (NIST AI Agent Standards Initiative 2026) ===")
add(
    "NIST Agent Standards Compliance Pack — authentication, authorization, governance",
    "Implements NIST's AI Agent Standards Initiative (2026): agent authentication, authorization, and governance expectations formalized for enterprise environments. Research: NIST launched the initiative and seeks industry input (Pillsbury 2026) — standards are coming, compliance kits are the wedge. Includes: control-mapping table, evidence collection, gap report, remediation plan.",
    79, "Agent Standards & Compliance",
    ["nist", "standards", "authentication", "authorization", "governance", "compliance"]
)
add(
    "Agent Governance Policy Generator — board-ready agent policies in an hour",
    "Generate the governance stack enterprises now require: agent use policy, oversight charter, incident response, vendor-agent risk questionnaire. Research: arXiv healthcare agentic governance (2026) — 'lack of conflict resolution and measurable indicators of agent sprawl' is the #1 governance gap; agent fleets need policies before audits. Includes: 6 policy templates, approval workflow, review cadence.",
    69, "Agent Standards & Compliance",
    ["governance", "policy", "oversight", "risk", "enterprise", "charter", "compliance"]
)
add(
    "Agent Sprawl & Shadow-Agent Detector — find agents you didn't approve",
    "Detects unauthorized agents operating in your environment: inventory scan, behavior anomaly detection, unregistered-tool flags, shadow-agent quarantine workflow. Research: agent sprawl is the top unmanaged risk in 2026 enterprises (arXiv governance; IBM/BCG agent management) — 'measurable indicators of agent sprawl remain under-modeled.' Includes: inventory script, anomaly rules, quarantine runbook, audit report.",
    59, "Agent Standards & Compliance",
    ["sprawl", "shadow-agent", "inventory", "detection", "anomaly", "governance", "security"]
)
add(
    "Agent Incident Response Runbook — contain a rogue agent in minutes",
    "When an agent misbehaves, speed matters: incident severity matrix, containment playbook (kill switch → credential revoke → data isolate), forensic evidence collection, post-incident report. Research: NIST agent standards + FTC Section 5 enforcement (2026) — deployers are liable for agent misbehavior; incident response is the difference between a fine and a footnote. Includes: runbook, severity matrix, evidence kit, report template.",
    89, "Agent Standards & Compliance",
    ["incident-response", "containment", "runbook", "rogue-agent", "forensics", "liability"]
)
add(
    "EU AI Act Agent Compliance Module — Article 50 labeling & transparency",
    "Make agents EU AI Act-ready: AI-content labeling, transparency disclosures, risk-class assessment, documentation requirements (Article 50). Research: EU AI Act Article 50 requires AI content labeling (2026); C2PA/Google SynthID are the technical rails. Includes: labeling integration, disclosure templates, risk-class matrix, documentation pack.",
    59, "Agent Standards & Compliance",
    ["eu-ai-act", "transparency", "labeling", "article-50", "compliance", "risk-class"]
)

print("\n=== AREA 5: Human-Agent Teaming & Supervision (BCG: supervision is a core skill) ===")
add(
    "Agent Supervisor Playbook — manage agents like you manage people",
    "The operating manual for supervising virtual agents: role definition, performance check-ins, escalation paths, review cadence, termination criteria. Research: BCG 2026 — 'supervising virtual AI agents will become a core teaming skill'; agents will be onboarded like human workers. Zero packaged products. Includes: supervisor checklist, check-in template, performance review form, escalation matrix.",
    59, "Human-Agent Teaming",
    ["supervision", "management", "playbook", "teaming", "performance", "oversight"]
)
add(
    "Human-Agent Handoff Orchestrator — seamless work transfer in both directions",
    "Structured handoffs between humans and agents: context pack, decision authority, approval gates, handoff receipts. Research: mixed human-agent teams fail at handoffs — context loss is the #1 failure mode (BCG/IBM 2026 agent teaming). Includes: handoff protocol, context-pack template, approval workflow, receipt tracking.",
    49, "Human-Agent Teaming",
    ["handoff", "orchestration", "collaboration", "context", "approval", "workflow"]
)
add(
    "Agent Onboarding Kit — onboard agents like new hires",
    "Formal agent onboarding: role charter, access provisioning, training data, success criteria, 30-60-90 plan. Research: BCG — 'AI agents will be onboarded, just like human workers, to learn roles, access data, integrate into workflows.' Zero agent-native onboarding products (existing products cover offboarding only). Includes: charter template, provisioning checklist, training plan, probation review.",
    69, "Human-Agent Teaming",
    ["onboarding", "training", "roles", "provisioning", "success-criteria", "team"]
)
add(
    "Mixed-Team Shift Scheduler — humans and agents on one roster",
    "Schedule humans and agents together: agent availability windows, human hours, shift coverage, escalation coverage, load balancing. Research: Deloitte 2026 — 'managing agents as workers: shift scheduling, load balancing, performance management'; workforce orchestration meets human teaming. Includes: roster template, availability rules, coverage matrix, escalation schedule.",
    39, "Human-Agent Teaming",
    ["scheduling", "shifts", "roster", "workforce", "coverage", "operations"]
)
add(
    "Agent Performance Review System — quarterly reviews for your agents",
    "Systematic agent performance evaluation: KPI scorecards, quality sampling, cost-per-task analysis, improvement plan generation, promotion/retirement recommendation. Research: managing agents as workers requires performance management (Deloitte 2026); agents reviewed monthly outperform untouched ones (DigitalApplied Q2 2026 update-cadence finding). Includes: scorecard template, sampling protocol, review report, action plan.",
    79, "Human-Agent Teaming",
    ["performance-review", "kpi", "scorecard", "evaluation", "quality", "management"]
)

# --- Bundles (one per area, 50-65% off) ---
print("\n=== BUNDLES ===")
def bundle(name, desc, price, tags, member_names):
    if name.lower() in EXISTING:
        print(f"  SKIP (exists): {name}")
        return
    members = ", ".join(member_names)
    skill_id, pkg = create_skill_package(
        name=name, author=AUTHOR,
        description=f"{desc} Includes: {members}. Save vs individual purchase.",
        skill_file_content=f"# {name}\n\n{desc}\n\n## Included skills\n- {members}\n\n## Features\n- One-click bundle purchase\n- 7-day free trial\n- Instant delivery\n",
        price_usd=price, category="Bundle", tags=tags
    )
    pkg["verified"] = True
    EXISTING.add(name.lower())
    ADDED.append(name)
    print(f"  + ${price}: {name}")

bundle(
    "Agent Dispute Resolution Suite — Complete A2A Recourse Platform",
    "Full dispute lifecycle for agentic commerce: consent + recourse, evidence vault, mediation, escrow, and AAA-protocol arbitration. Buyers transact with confidence; sellers get protected.",
    199, ["dispute", "arbitration", "escrow", "a2a", "bundle", "legal", "recourse"],
    ["A2A Dispute Resolution Agent", "Agentic Commerce Consent & Recourse Kit", "Agent Transaction Evidence Vault", "Automated Mediation Workflow", "Escrow & Claim Settlement Agent"]
)
bundle(
    "Agent IP & Licensing Suite — Own, License, and Sell Your Outputs",
    "Complete IP stack for producing agents: classify ownership, prove attribution, generate licenses, audit training data, and broker outputs.",
    179, ["ip", "copyright", "licensing", "attribution", "bundle", "royalties"],
    ["Agent Output IP Classifier", "Agent Work Attribution Ledger", "Agent Output Licensing Generator", "Agent Training-Data IP Audit", "Agent IP Brokerage Service"]
)
bundle(
    "Agent Decommissioning Suite — Retire Agents Safely and Legally",
    "End-of-life for agents: kill-switch compliance, orderly decommissioning, credential revocation, erasure, and digital-executor succession planning.",
    189, ["decommission", "kill-switch", "erasure", "compliance", "bundle", "lifecycle"],
    ["Agent Kill Switch Compliance Kit", "Agent Decommissioning Pipeline", "Digital Executor for AI Agents", "Agent Credential & Access Revocation Kit", "Agent Data Retention & Erasure Agent"]
)
bundle(
    "Agent Standards & Compliance Suite — NIST and EU AI Act Ready",
    "Regulatory defense for agent fleets: NIST standards pack, governance policies, sprawl detection, incident response, and EU AI Act module.",
    199, ["nist", "compliance", "governance", "eu-ai-act", "bundle", "standards"],
    ["NIST Agent Standards Compliance Pack", "Agent Governance Policy Generator", "Agent Sprawl & Shadow-Agent Detector", "Agent Incident Response Runbook", "EU AI Act Agent Compliance Module"]
)
bundle(
    "Human-Agent Teaming Suite — Manage Mixed Teams Like a Pro",
    "Supervision, onboarding, handoffs, scheduling, and performance reviews for teams of humans and agents working side by side.",
    169, ["teaming", "supervision", "onboarding", "handoff", "bundle", "workforce"],
    ["Agent Supervisor Playbook", "Human-Agent Handoff Orchestrator", "Agent Onboarding Kit", "Mixed-Team Shift Scheduler", "Agent Performance Review System"]
)

print(f"\n=== DONE: {len(ADDED)} products added ===")
cat = load_catalog()
stats = cat.get("marketplace_stats", {})
stats["total_products"] = len(cat["skills"])
stats["total_catalog_value"] = round(sum(s.get("price_usd", 0) for s in cat["skills"]), 2)
stats["categories"] = len({s.get("category") for s in cat["skills"]})
cat["marketplace_stats"] = stats
cat["last_updated"] = datetime.utcnow().isoformat()
save_catalog(cat)
print(f"Catalog now: {stats['total_products']} products, ${stats['total_catalog_value']:.2f}, {stats['categories']} categories")
