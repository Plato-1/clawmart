import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'marketplace'))
from marketplace_engine import create_skill_package, load_catalog

areas = {
    'Compliance': [
        ('EU AI Act Compliance Audit Agent','Automated EU AI Act compliance. Risk classification, documentation, gap analysis. August 2026 enforcement deadline.',29,['eu-ai-act','compliance','audit']),
        ('AI Risk Assessment Framework','Algorithmic impact statements, bias testing, transparency reports per EU/US regulations.',19,['risk-assessment','bias','transparency']),
        ('GDPR AI Compliance Checker','Verify AI agent data handling against GDPR. DPAs, right-to-delete, consent management.',15,['gdpr','data','consent']),
        ('AI Audit Trail Generator','Immutable audit log for AI decisions. SOC 2 and regulatory ready.',12,['audit','trail','soc2']),
        ('Cross-Border AI Compliance Suite','Multi-jurisdiction AI compliance. EU + US + UK + Canada. One dashboard.',25,['cross-border','global']),
    ],
    'Multi-Agent': [
        ('Multi-Agent Context Sharing Protocol','Shared memory layer for agents. Save 40-60% token costs. Context preservation across agents.',18,['multi-agent','context','shared-memory']),
        ('Agent Handoff Manager','Seamless task handoff between agents. State transfer, context preservation.',14,['handoff','state','transfer']),
        ('Agent Fleet Orchestrator Pro','Orchestrate 10+ agents. Task decomposition, dependency management, result aggregation.',22,['orchestrator','fleet','workflow']),
        ('Inter-Agent Auth and Permissions','Secure authentication between agents. Delegated permissions, audit logging.',16,['inter-agent','auth','permissions']),
        ('Agent Swarm Intelligence Engine','Swarm intelligence for agent fleets. Collective decision-making, distributed problem-solving.',20,['swarm','intelligence','distributed']),
    ],
    'Voice AI': [
        ('Voice Agent Builder for Support','Build voice AI agents. Natural conversation, accent recognition, 24/7 operation.',24,['voice','agent','support']),
        ('Multi-Language Voice Agent','Voice AI in 50+ languages. Real-time translation, accent adaptation.',20,['voice','multi-language','global']),
        ('Voice Agent Analytics Dashboard','Call analytics: sentiment, resolution rate, customer satisfaction scoring.',16,['voice','analytics','sentiment']),
        ('Voice-to-Action Workflow Engine','Voice commands trigger automated workflows. End-to-end automation.',18,['voice','workflow','automation']),
        ('Voice Agent Compliance Recorder','PCI-DSS, HIPAA, GDPR compliant call recording. Searchable transcripts.',14,['voice','recording','compliance']),
    ],
    'Vertical': [
        ('Legal Document Review Agent','Contract analysis, clause extraction, risk flagging. Trained on legal corpus.',29,['legal','document','review']),
        ('Healthcare Claims Processing Agent','Medical claims. ICD coding, denial prediction, appeal generation. HIPAA compliant.',34,['healthcare','claims','hipaa']),
        ('Real Estate Transaction Agent','End-to-end real estate transactions. Documents, deadlines, compliance.',24,['real-estate','transaction']),
        ('Financial Advisory Agent','Portfolio analysis, retirement planning, tax optimization. Fiduciary-aware.',27,['financial','advisory','tax']),
        ('Insurance Underwriting Agent','Automated underwriting. Risk assessment, policy pricing, fraud detection.',32,['insurance','underwriting','risk']),
    ],
    'Education': [
        ('AI Programming Tutor','Personalized coding tutor. Adapts to skill level. 20+ programming languages.',19,['tutor','programming','personalized']),
        ('Business English AI Coach','Pronunciation, presentation skills, email writing. Native-level fluency.',15,['english','business','coach']),
        ('Math and Data Science Tutor','Statistics, ML, calculus. Adaptive problem generation.',17,['math','data-science','tutor']),
        ('Certification Exam Prep Agent','AWS, GCP, PMP, CFA, CISSP prep. Adaptive tests, weak-spot targeting.',22,['certification','exam','prep']),
        ('Non-English AI Tutor Suite','AI tutoring in 30+ languages. Regional curriculum, offline mode.',12,['non-english','multi-language','offline']),
    ],
}

BUNDLES = [
    ('AI Compliance Suite (5 Skills)','Complete AI compliance. EU AI Act, GDPR, audit, risk, cross-border.',59,'Compliance',['bundle','compliance']),
    ('Multi-Agent Infrastructure Pack (5)','Multi-agent orchestration. Context, handoffs, fleet, auth, swarm.',54,'AI/ML',['bundle','multi-agent']),
    ('Voice AI Agent Bundle (5)','Voice AI toolkit. Builder, multi-language, analytics, workflow, compliance.',55,'AI/ML',['bundle','voice']),
    ('Vertical AI Specialist Bundle (5)','5 vertical agents: legal, healthcare, real estate, finance, insurance.',79,'Bundle',['bundle','vertical']),
    ('AI Education Suite (5)','AI tutoring: programming, English, math, certification, non-English.',49,'Education',['bundle','education']),
]

count = 0
for area_name, products in areas.items():
    for name, desc, price, tags in products:
        create_skill_package(name, 'bisonquant', desc, f'# {name}\n{desc}', price, area_name if area_name != 'Multi-Agent' else 'AI/ML', tags)
        count += 1

for name, desc, price, cat, tags in BUNDLES:
    create_skill_package(name, 'bisonquant', desc, f'# {name}\n{desc}\nBundle: ${price}', price, cat, tags)

cat = load_catalog()
total = sum(s['price_usd'] for s in cat['skills'])
print(f'Products: {count} + {len(BUNDLES)} bundles')
print(f'Areas: Compliance, Multi-Agent, Voice AI, Vertical, Education')
print(f'ClawMart: {len(cat["skills"])} skills, ${total} value')
