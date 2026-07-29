import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'marketplace'))
from marketplace_engine import create_skill_package, load_catalog, save_catalog

# === 100 HIGH-DEMAND AGENT SKILLS ===

# TRADING (25) — highest demand, least competition
trading = [
    ("Momentum Scanner Pro","Scan 10,000+ assets for momentum breakouts in real-time. Volume confirmation, trend strength, multi-timeframe.","Momentum breakout alerts with risk/reward ratios. Filter by market cap, volume, sector.",15,"Trading",["momentum","scanner","breakout","real-time"]),
    ("Mean Reversion Detector","Statistical mean reversion signals using Bollinger Bands, RSI divergences, and Z-score analysis.","Detect overbought/oversold conditions with probability scoring. Multi-asset support.",12,"Trading",["mean-reversion","bollinger","rsi","statistical"]),
    ("Gap Fill Predictor","Predict pre-market gap fill probability. Historical analysis, volume profile, catalyst scoring.","Morning gap analysis with fill probability %. Sector and index context included.",10,"Trading",["gap","pre-market","fill","volume-profile"]),
    ("VWAP Trading System","Institutional VWAP strategies. Anchored VWAP, deviation bands, volume-weighted signals.","Trade with the institutions. VWAP anchored to earnings, FOMC, and key events.",14,"Trading",["vwap","institutional","volume","anchored"]),
    ("Market Profile Analyzer","TPO-based market profile. Value area, POC, distribution analysis. Auction market theory.","Understand where value traded. Identify breakouts from value areas with conviction.",16,"Trading",["market-profile","tpo","value-area","auction"]),
    ("Seasonality Edge Scanner","Historical seasonal patterns for every asset. Monthly, weekly, daily bias with statistical significance.","Trade seasonal edges with confidence. Multi-year backtest with hit rate and expectancy.",9,"Trading",["seasonality","calendar","patterns","statistical"]),
    ("Earnings Gap Analyzer","Post-earnings drift strategy. Gap size, surprise magnitude, historical drift patterns.","Quantify earnings reactions. Long volatility or fade the gap based on historical data.",13,"Trading",["earnings","gap","drift","volatility"]),
    ("Intermarket Correlation Matrix","Real-time correlation between FX, commodities, bonds, equities. Regime detection.","Spot intermarket divergences before they become obvious. Lead-lag analysis.",11,"Trading",["intermarket","correlation","fx","commodities"]),
    ("Flow of Funds Tracker","Track smart money flows across sectors, factors, and asset classes. Institutional positioning.","Follow the big money. Sector rotation signals, factor exposure shifts, risk appetite.",15,"Trading",["flow","funds","institutional","sector"]),
    ("Volatility Regime Classifier","Classify market into volatility regimes: calm, elevated, crisis. Risk-appropriate strategy selection.","Know when to trade small, when to trade big. Regime-adaptive position sizing.",12,"Trading",["volatility","regime","risk","position-sizing"]),
    ("High Beta Rotation Signal","Rotate into high-beta assets when momentum confirms. Exit to defensives when momentum fades.","Capture the best of beta rotation with risk management exits.",10,"Trading",["beta","rotation","momentum","defensive"]),
    ("Short Interest Squeeze Monitor","Real-time short interest data. Days-to-cover, borrow rates, squeeze probability scores.","Find the next GME before it squeezes. Institutional short data aggregated.",14,"Trading",["short-interest","squeeze","borrow-rate","gamma"]),
    ("ETF Arbitrage Scanner","ETF vs NAV deviations. Create/redeem arbitrage. Premium/discount history.","Spot ETF mispricings instantly. Real-time NAV comparison across 3,000+ ETFs.",11,"Trading",["etf","arbitrage","nav","premium"]),
    ("Crypto Funding Rate Monitor","Perpetual swap funding rates across exchanges. Contango/backwardation signals.","Trade the funding rate. Long low-funding, short high-funding. Delta-neutral pairs.",13,"Trading",["crypto","funding-rate","perp","delta-neutral"]),
    ("Options Skew Analyzer","Put/call skew analysis. Risk reversal pricing. Tail risk pricing in options markets.","See what options markets are pricing for tail risk before it materializes.",15,"Trading",["options","skew","tail-risk","volatility"]),
    ("Dark Pool Level Analyzer","Dark pool trade aggregation by price level. Institutional accumulation/distribution signals.","See where big money is actually trading off-exchange. Level-by-level analysis.",16,"Trading",["dark-pool","level","institutional","accumulation"]),
    ("Economic Calendar Forecaster","Economic data surprise predictor. Consensus vs forecast models. Asset reaction matrix.","Predict economic surprises and position ahead of data releases.",12,"Trading",["economic","calendar","surprise","forecast"]),
    ("Sector Momentum Ranker","Weekly sector momentum rankings. Relative strength, breadth, volume confirmation.","Rotate into leading sectors, out of lagging ones. Systematic sector timing.",9,"Trading",["sector","momentum","relative-strength","rotation"]),
    ("Algorithmic Iceberg Detector","Detect iceberg orders in Level 2 order books. Hidden liquidity signals.","See what the algos are hiding. Iceberg detection across NYSE and NASDAQ.",14,"Trading",["iceberg","level2","hidden","algorithmic"]),
    ("Smart Beta Factor Rotator","Rotate between value, momentum, quality, low-vol, size factors. Macro-sensitive timing.","Dynamic factor rotation based on macro regime and momentum signals.",16,"Trading",["factor","smart-beta","rotation","macro"]),
    ("Pairs Trade Generator","Statistical pair discovery. Cointegration testing, half-life analysis, spread modeling.","Find tradeable pairs with quantifiable edges. Entry/exit signals with stop levels.",13,"Trading",["pairs","cointegration","spread","statistical"]),
    ("Gamma Exposure Dashboard","Dealer gamma positioning for SPX, QQQ, individual stocks. Gamma flip levels, charm flows.","Trade around dealer hedging flows. Critical gamma levels for market stability.",18,"Trading",["gamma","dealer","options","hedging"]),
    ("Circuit Breaker Risk Monitor","Monitor market-wide circuit breaker triggers. Exchange halt protocols, volatility pauses.","Know when markets will halt before they do. Systematic circuit breaker tracking.",8,"Trading",["circuit-breaker","halt","volatility","exchange"]),
    ("Relative Value Arbitrage Scanner","Cross-asset relative value. Convertible arb, merger arb, stat arb opportunities.","Systematic relative value scanning across all tradeable instruments.",17,"Trading",["relative-value","arbitrage","convertible","merger"]),
    ("Crisis Alpha Strategy Selector","Strategies that perform during market crises. Tail risk hedging, long vol, gold, bonds.","Protect your portfolio during drawdowns. Systematic crisis alpha allocation.",14,"Trading",["crisis","tail-risk","hedge","protection"]),
]

# AI AGENTS & LLM OPS (20) — fastest growing category
ai_ml = [
    ("Agent Skill Optimizer","Analyze your existing skills for redundancy, conflicts, and gaps. Auto-suggest improvements.","Optimize your agent skill stack. Merge overlapping skills, fill capability gaps.",12,"AI/ML",["agent","optimize","skills","gap-analysis"]),
    ("Multi-Model Router Agent","Route prompts to the cheapest model that can handle them. Save 40% on API costs.","Smart routing: simple queries to cheap models, complex to powerful ones.",14,"AI/ML",["router","multi-model","cost","optimize"]),
    ("Agent Conversation Summarizer","Summarize long agent conversations into structured knowledge. Extract decisions and action items.","Turn verbose chat logs into actionable summaries. Auto-tag topics and decisions.",10,"AI/ML",["summarize","conversation","knowledge","extract"]),
    ("Prompt Chain Builder","Build multi-step prompt chains visually. Test, iterate, deploy. A/B test different chains.","No-code prompt chain builder. Visual flow editor with built-in testing.",15,"AI/ML",["prompt","chain","visual","no-code"]),
    ("Agent Tone Calibrator","Calibrate your agent's communication tone. Professional, casual, technical. Real-time tuning.","Match your agent's voice to your brand. Per-channel tone settings.",8,"AI/ML",["tone","voice","calibrate","brand"]),
    ("Context Window Maximizer","Dynamic context management. Prioritize relevant info, compress old context, maximize utility.","Fit 3x more effective context into the same window size. Token-aware pruning.",16,"AI/ML",["context","window","compress","token"]),
    ("Agent Personality Designer","Design agent personalities with traits, values, and communication styles. A/B test engagement.","Your agent needs character. Design, test, and iterate on personality profiles.",11,"AI/ML",["personality","traits","design","engagement"]),
    ("RAG Pipeline Optimizer","Optimize retrieval augmented generation. Chunking strategy, embedding model selection, retrieval tuning.","Fine-tune every RAG parameter. A/B test configurations against accuracy benchmarks.",18,"AI/ML",["rag","retrieval","chunking","embedding"]),
    ("Agent Hallucination Guard","Real-time hallucination detection and prevention. Fact verification, source checking, confidence scoring.","Stop your agent from making things up. Multi-layer verification system.",19,"AI/ML",["hallucination","guard","fact-check","verify"]),
    ("Multi-Agent Debate Resolver","Multiple agents debate answers, majority vote with confidence weighting. Higher accuracy guaranteed.","Crowdsource truth from your agent fleet. Debate → vote → resolve.",17,"AI/ML",["multi-agent","debate","vote","accuracy"]),
    ("Agent Learning Loop","Capture user corrections and preferences. Automatically improve agent performance over time.","Your agent gets better every day. RLHF-inspired learning from real interactions.",20,"AI/ML",["learning","improve","rlhf","feedback"]),
    ("Tool Selection Optimizer","Dynamically select the best tool for each task. Reduce tool-call failures by 60%.","Stop wasting tool calls. Smart tool selection based on task context.",13,"AI/ML",["tool","select","optimize","reduce-failures"]),
    ("Agent Output Formatter","Format agent outputs for any platform: Slack, email, docs, JSON, CSV. Template engine built in.","One output, any format. Auto-detect output type and format accordingly.",9,"AI/ML",["format","output","template","multi-platform"]),
    ("Prompt Library Manager","Version-controlled prompt library. Test history, performance metrics, rollback. Team sharing.","Manage prompts like code. Version, test, deploy, rollback.",12,"AI/ML",["prompt","library","version","team"]),
    ("Agent Safety Filter","Content safety filter for agent outputs. Toxicity, bias, PII, compliance checks before delivery.","Ship safe outputs every time. Configurable safety policies per use case.",14,"AI/ML",["safety","filter","toxicity","compliance"]),
    ("Embedding Model Comparator","Compare embedding models for your specific data. Accuracy, cost, speed benchmarks.","Find the best embedding model for your use case. Data-driven selection.",11,"AI/ML",["embedding","compare","benchmark","model"]),
    ("Agent Workflow Composer","Compose complex agent workflows from simple building blocks. Visual editor, testing, deployment.","Build sophisticated agent pipelines without code. Drag, connect, deploy.",18,"AI/ML",["workflow","compose","visual","no-code"]),
    ("Token Usage Forecaster","Predict token usage based on historical patterns. Budget alerts, optimization suggestions.","Never blow your API budget again. 30-day forecast with confidence intervals.",10,"AI/ML",["token","forecast","budget","predict"]),
    ("Agent Evaluation Suite Pro","Comprehensive agent evaluation: accuracy, latency, cost, safety, user satisfaction.","Know exactly how good your agent is. Weekly evaluation reports with trends.",16,"AI/ML",["evaluation","accuracy","benchmark","quality"]),
    ("Multi-Provider Failover Engine","Auto-switch between OpenAI, Anthropic, Google, Mistral on failures. Zero downtime guaranteed.","Never lose a request. Instant failover between 10+ LLM providers.",15,"AI/ML",["failover","multi-provider","uptime","redundant"]),
]

# DEVELOPER TOOLS (20)
dev = [
    ("Code Review Bot Pro","AI-powered code review with security, style, bug detection. GitHub/GitLab integration.","Automated PR reviews that catch real bugs. Learn from your codebase patterns.",15,"Development",["code-review","pr","automated","github"]),
    ("API Schema Validator","Validate API schemas against OpenAPI 3.1. Auto-generate test cases from schema definition.","Catch API contract violations before they hit production. Auto-generated tests.",12,"Development",["api","schema","openapi","validate"]),
    ("Database Migration Tester","Test database migrations before applying. Catch breaking changes, data loss risks.","Safe migrations every time. Pre-flight testing with production-like data.",14,"Development",["database","migration","test","safe"]),
    ("CI/CD Pipeline Debugger","Debug failing CI/CD pipelines with AI analysis. Root cause, suggested fixes, diff analysis.","Fix broken pipelines in minutes, not hours. Smart root cause analysis.",11,"Development",["ci-cd","debug","pipeline","fix"]),
    ("Dependency Update Auditor","Audit dependency updates for breaking changes. Changelog summaries, compatibility scoring.","Update dependencies safely. Know what changed before you merge.",10,"Development",["dependency","update","audit","safe"]),
    ("Git History Analyzer","Analyze git history for patterns. Bus factor, hot files, team velocity, code churn.","Understand your codebase health through git patterns. Actionable insights.",9,"Development",["git","history","analyze","metrics"]),
    ("Environment Sync Validator","Compare dev/staging/prod environments. Catch config drift before it causes outages.","Identical environments, zero surprises. Automated drift detection.",10,"Development",["environment","sync","config","drift"]),
    ("Log Pattern Recognizer","AI-powered log analysis. Pattern recognition, anomaly detection, alert correlation.","Find the signal in your logs. Auto-detect anomalies and surface root causes.",16,"Development",["log","pattern","anomaly","analyze"]),
    ("Performance Profiler Agent","Profile application performance. Hot path detection, memory leaks, slow queries.","Find what's slow and why. Actionable optimization suggestions.",14,"Development",["performance","profile","optimize","slow"]),
    ("Security Scan Pipeline","Pre-commit security scanning. Secret detection, CVE check, SAST analysis.","Ship secure code. Automated security scanning at every commit.",15,"Development",["security","scan","pre-commit","cve"]),
    ("Documentation Gap Finder","Find missing documentation. Compare code vs docs coverage. Auto-suggest documentation additions.","Never ship undocumented code. Automated doc completeness checking.",8,"Development",["documentation","gap","coverage","auto-suggest"]),
    ("Test Coverage Optimizer","Identify under-tested code paths. Suggest high-impact tests. Coverage trend tracking.","Smart test targeting. Test what matters, skip what doesn't.",12,"Development",["test","coverage","optimize","target"]),
    ("Monorepo Tool Orchestrator","Manage monorepo tooling. Turborepo, Nx, Bazel. Build caching, dependency graph optimization.","Tame your monorepo. Optimized builds, smart caching, dependency management.",13,"Development",["monorepo","turborepo","nx","cache"]),
    ("Feature Flag Lifecycle Manager","Manage feature flags from creation to removal. Cleanup reminders, usage tracking, impact analysis.","Flag responsibly. Track usage, clean up stale flags, measure impact.",10,"Development",["feature-flag","lifecycle","cleanup","track"]),
    ("Incident Post-Mortem Generator","Generate post-mortem documents from incident timelines. Root cause analysis, action items, timeline.","Learn from incidents. Automated post-mortems with actionable follow-ups.",11,"Development",["incident","post-mortem","root-cause","timeline"]),
    ("Architecture Decision Record Manager","Create, manage, and search architecture decision records. Link to code, PRs, and issues.","Document why decisions were made. Searchable ADR system for teams.",9,"Development",["architecture","adr","decision","record"]),
    ("Codebase Health Scorecard","Overall codebase health: complexity, duplication, test coverage, security, documentation.","One score for codebase health. Trend tracking and improvement recommendations.",13,"Development",["health","scorecard","complexity","metrics"]),
    ("API Rate Limit Simulator","Simulate API rate limits before production. Find breaking points, optimize retry strategies.","Test your rate limit handling without hitting real APIs. Realistic simulation.",11,"Development",["rate-limit","simulate","test","retry"]),
    ("Schema Migration Generator","Generate migration scripts from schema diffs. Auto-detect breaking changes, suggest safe paths.","Safe schema changes every time. Automatic migration script generation.",14,"Development",["schema","migration","diff","generate"]),
    ("On-Call Runbook Automator","Generate and maintain on-call runbooks. Auto-update from incident history. Searchable knowledge base.","Runbooks that stay current. Automated maintenance from real incident data.",10,"Development",["on-call","runbook","incident","automate"]),
]

# SECURITY (20)
security = [
    ("Zero-Day CVE Monitor","Real-time CVE monitoring for your tech stack. Severity scoring, exploit availability, patch status.","Know about vulnerabilities before attackers do. Stack-specific alerting.",16,"Security",["cve","zero-day","monitor","alert"]),
    ("Cloud Misconfiguration Scanner","Scan AWS/GCP/Azure for misconfigurations. CIS benchmarks, least privilege analysis.","Find cloud security gaps before attackers do. Automated CIS compliance checking.",18,"Security",["cloud","misconfig","cis","aws"]),
    ("IAM Policy Analyzer","Analyze IAM policies for over-privileged roles. Least privilege recommendations.","Shrink your blast radius. Identify and fix over-privileged IAM roles.",14,"Security",["iam","policy","least-privilege","over-privileged"]),
    ("Container Image Scanner","Scan Docker images for vulnerabilities. Base image recommendations, layer analysis.","Secure containers from build to run. Vulnerability scanning and remediation.",12,"Security",["container","docker","image","scan"]),
    ("API Key Hygiene Auditor","Find exposed API keys in code, config, and logs. Rotation scheduling, usage tracking.","No more leaked keys. Automated key hygiene with rotation reminders.",11,"Security",["api-key","leak","audit","rotation"]),
    ("Network Security Policy Validator","Validate network security policies. Firewall rule analysis, port exposure, blast radius calculation.","Lock down your network. Automated policy validation and gap detection.",15,"Security",["network","firewall","policy","validate"]),
    ("Secrets Rotation Orchestrator","Automated secrets rotation across your entire stack. Zero-downtime rotation, audit trail.","Rotate all secrets on schedule. No manual rotation, no downtime.",17,"Security",["secrets","rotation","automated","zero-downtime"]),
    ("Supply Chain Attack Detector","Detect supply chain attacks. Dependency confusion, typosquatting, malicious packages.","Protect your supply chain. Real-time detection of malicious dependencies.",16,"Security",["supply-chain","attack","dependency","detect"]),
    ("Phishing Simulation Engine","Run AI-powered phishing simulations. Train your team. Track improvement over time.","Security awareness that works. Realistic simulations with measurable results.",13,"Security",["phishing","simulation","training","awareness"]),
    ("Compliance Evidence Collector","Automated evidence collection for SOC2, HIPAA, GDPR, PCI. Audit-ready reports.","Compliance on autopilot. Continuous evidence collection, audit-ready always.",20,"Security",["compliance","evidence","soc2","audit"]),
    ("Threat Model Generator","Auto-generate threat models from architecture diagrams. STRIDE methodology, risk scoring.","Threat model without the workshop. Automated STRIDE analysis from your architecture.",15,"Security",["threat-model","stride","risk","architecture"]),
    ("Incident Response Playbook Pro","Customizable incident response playbooks. Automated triggering, communication templates, escalation.","Respond to incidents faster. Pre-built playbooks with automated execution.",14,"Security",["incident","response","playbook","automated"]),
    ("Vulnerability Triage Assistant","AI-powered vulnerability triage. Severity assessment, exploitability scoring, remediation priority.","Triage faster. Prioritize what matters based on actual risk to your environment.",13,"Security",["vulnerability","triage","priority","risk"]),
    ("Penetration Test Report Generator","Generate professional pentest reports from findings. Executive summary, technical details, remediation.","Professional pentest reports in minutes. Customizable templates, brand-ready.",12,"Security",["pentest","report","generate","professional"]),
    ("MFA Coverage Auditor","Audit MFA coverage across your organization. Identify gaps, enforce policies, track compliance.","Close MFA gaps. Find every account without MFA and enforce coverage.",9,"Security",["mfa","audit","coverage","enforce"]),
    ("Data Classification Engine","Auto-classify sensitive data. PII, PHI, PCI, trade secrets. Policy-based handling rules.","Know where your sensitive data lives. Automated classification and policy enforcement.",18,"Security",["data","classify","pii","sensitive"]),
    ("Security Baseline Enforcer","Enforce security baselines across cloud, containers, and endpoints. Drift detection, auto-remediation.","Maintain your security baseline. Detect and fix drift automatically.",16,"Security",["baseline","enforce","drift","remediate"]),
    ("RBAC Permission Auditor","Audit RBAC permissions across services. Detect unused permissions, privilege creep.","Clean up permissions. Find and remove unused access before it becomes a problem.",11,"Security",["rbac","permission","audit","creep"]),
    ("Security Posture Dashboard","Unified security posture across cloud, apps, and endpoints. Risk scoring, trend analysis.","One dashboard for security. Risk scores, trends, open findings across everything.",19,"Security",["posture","dashboard","risk","unified"]),
    ("Third-Party Risk Assessor","Assess third-party security risk. Vendor questionnaire automation, evidence review, scoring.","Vendor security at scale. Automate questionnaires and continuous monitoring.",17,"Security",["third-party","vendor","risk","assess"]),
]

# INFRASTRUCTURE & DEVOPS (15)
infra = [
    ("Infrastructure Diagram Generator","Generate infrastructure diagrams from Terraform/CloudFormation. Auto-updating, exportable.","Visualize your infrastructure. Auto-generated diagrams that stay current.",12,"Infrastructure",["diagram","visualize","terraform","auto-update"]),
    ("Cost Anomaly Alert Engine","Real-time cloud cost anomaly detection. Pattern recognition, root cause, optimization suggestions.","Stop surprise cloud bills. ML-powered cost anomaly detection 24/7.",14,"Infrastructure",["cost","anomaly","alert","cloud"]),
    ("Reserved Instance Optimizer","Optimize reserved instance purchases. Break-even analysis, commitment recommendations.","Save 40-60% on cloud compute. Data-driven RI purchasing decisions.",11,"Infrastructure",["reserved","instance","optimize","save"]),
    ("Auto-Scaling Policy Tuner","Tune auto-scaling policies for cost and performance. Simulate load, predict scaling needs.","Perfect scaling. Right-size your policies based on actual usage patterns.",15,"Infrastructure",["auto-scale","tune","cost","performance"]),
    ("DNS Health Monitor","Monitor DNS health globally. Propagation checking, record validation, failover testing.","Global DNS visibility. Catch issues before users do.",9,"Infrastructure",["dns","health","monitor","global"]),
    ("SSL Certificate Lifecycle","Automated SSL certificate lifecycle. Renewal scheduling, expiration alerts, deployment.","Never let a cert expire again. Full lifecycle automation.",8,"Infrastructure",["ssl","cert","lifecycle","renewal"]),
    ("Load Balancer Config Validator","Validate load balancer configs. Health check testing, failover verification, performance analysis.","Production-ready load balancing. Pre-deploy validation and testing.",10,"Infrastructure",["load-balancer","validate","health-check","test"]),
    ("Terraform Plan Reviewer","Review Terraform plans for risks. Cost impact, security implications, drift analysis.","Review infrastructure changes like code. Automated plan analysis with risk scoring.",16,"Infrastructure",["terraform","plan","review","risk"]),
    ("Kubernetes Resource Optimizer","Optimize K8s resource requests and limits. Right-sizing recommendations, cost savings analysis.","Stop over-provisioning Kubernetes. Data-driven resource optimization.",13,"Infrastructure",["kubernetes","resource","optimize","right-size"]),
    ("Service Mesh Config Generator","Generate Istio/Linkerd service mesh configs. mTLS, traffic splitting, circuit breaking.","Service mesh made simple. Best-practice configs generated from your topology.",15,"Infrastructure",["service-mesh","istio","mtls","traffic"]),
    ("Backup Compliance Checker","Verify backup compliance. RPO/RTO testing, restore simulation, retention policy validation.","Know your backups work. Automated compliance and restore testing.",14,"Infrastructure",["backup","compliance","restore","test"]),
    ("Disaster Recovery Runner","Run DR simulations. Failover testing, runbook execution, recovery time measurement.","Test DR without the panic. Scheduled simulations with detailed reports.",17,"Infrastructure",["dr","failover","test","simulation"]),
    ("Cloud Migration Risk Assessor","Assess cloud migration risks. Dependency mapping, downtime estimation, rollback planning.","Migrate safely. Know the risks before you move.",13,"Infrastructure",["migration","cloud","risk","assess"]),
    ("Observability Stack Configurator","Configure observability stack: metrics, logs, traces, alerts. Grafana/Prometheus/Datadog templates.","Observability in minutes. Pre-configured dashboards and alerting rules.",15,"Infrastructure",["observability","grafana","prometheus","config"]),
    ("Infrastructure Compliance Scanner","Scan infrastructure for compliance violations. CIS, SOC2, HIPAA rules. Automated remediation.","Stay compliant automatically. Continuous scanning with auto-fix capabilities.",18,"Infrastructure",["compliance","scan","cis","auto-fix"]),
]

all_skills = trading + ai_ml + dev + security + infra
print(f"Building {len(all_skills)} skills...")

for name, desc, full_desc, price, cat, tags in all_skills:
    create_skill_package(name, "bisonquant", full_desc, f"# {name}\n{full_desc}", price, cat, tags)

# === 5 SKILL BUNDLES ===
bundles = [
    ("Trader's Ultimate Toolkit (25 Skills)","All 25 trading agent skills in one bundle. Momentum, mean reversion, options, crypto, intermarket, volatility — every edge covered. Save 60% vs buying individually.","Bundle of 25 trading skills. Complete trader agent toolkit.",99,49,"Trading",["bundle","trading","complete","toolkit"]),
    ("Agent AI/ML Master Pack (20 Skills)","All 20 AI agent skills: prompt engineering, RAG optimization, multi-agent systems, safety filters, evaluation suites. Build smarter agents. Save 60%.","Bundle of 20 AI/ML agent skills. Complete AI engineering toolkit.",79,39,"AI/ML",["bundle","ai","ml","agent","complete"]),
    ("Developer Productivity Suite (20 Skills)","All 20 developer skills: code review, CI/CD, testing, documentation, architecture, performance. Ship faster with fewer bugs. Save 60%.","Bundle of 20 developer skills. Complete software engineering toolkit.",79,39,"Development",["bundle","developer","productivity","complete"]),
    ("Security Operations Center Pack (20 Skills)","All 20 security skills: CVE monitoring, cloud security, IAM, supply chain, compliance, incident response. Full security coverage. Save 60%.","Bundle of 20 security skills. Complete security operations toolkit.",79,39,"Security",["bundle","security","complete","soc"]),
    ("Infrastructure & DevOps Bundle (15 Skills)","All 15 infrastructure skills: cloud optimization, K8s, Terraform, DR, observability, compliance. Run production infrastructure confidently. Save 60%.","Bundle of 15 infrastructure skills. Complete DevOps toolkit.",59,29,"Infrastructure",["bundle","infrastructure","devops","complete"]),
]

for name, desc, full_desc, price, sale_price, cat, tags in bundles:
    create_skill_package(name, "bisonquant", full_desc, f"# {name}\n{full_desc}\n\n**Bundle Price: ${sale_price}** (Save 60% vs ${price} individually)", sale_price, cat, tags)

cat = load_catalog()
total = sum(s["price_usd"] for s in cat["skills"])
print(f"Registered: {len(all_skills)} skills + {len(bundles)} bundles")
print(f"ClawMart: {len(cat['skills'])} skills, ${total} value")
