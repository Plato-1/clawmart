#!/usr/bin/env python3
"""Build 100 high-demand, high-margin products for ClawMart."""
import sys, os, json
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from marketplace.marketplace_engine import create_skill_package, load_catalog

PRODUCTS = [
    # TRADING (20 products) — highest demand signal: 42+ mentions
    ("Trend Reversal Detector", "ML-based reversal pattern detection. Flags double tops/bottoms, head-and-shoulders, wedges. 85%+ backtest accuracy on S&P 500. Real-time alerts.", 9, "Trading", ["trading","pattern","reversal","ml","alerts"]),
    ("Options Flow Scanner", "Track unusual options activity. Calls/puts ratio anomalies, whale sweeps, dark pool prints. Daily report with top 10 tickers.", 12, "Trading", ["options","flow","whale","scanner","unusual"]),
    ("Earnings Surprise Predictor", "ML model trained on 10 years of earnings data. Predicts surprise direction with 72% accuracy. Weekly report before earnings season.", 15, "Trading", ["earnings","ml","prediction","surprise","fundamentals"]),
    ("Volatility Term Structure Analyzer", "VIX futures curve analysis. Contango vs backwardation signals. Historical percentile ranking. Regime switch alerts.", 10, "Trading", ["volatility","vix","term-structure","futures"]),
    ("Dark Pool Print Tracker", "Aggregate dark pool trade data. Unusual block trades by ticker. Institutional accumulation/distribution signals.", 11, "Trading", ["dark-pool","block-trade","institutional","whale"]),
    ("Gamma Exposure Monitor", "Track dealer gamma positioning across SPX/QQQ strikes. Gamma flip levels. Max pain calculations. Daily update.", 13, "Trading", ["gamma","options","dealers","max-pain","spx"]),
    ("Sector Rotation Heatmap", "Weekly sector momentum rankings. Relative strength vs SPY. Rotation signals when sectors flip. Color-coded visualization.", 8, "Trading", ["sector","rotation","momentum","heatmap","relative-strength"]),
    ("Put/Call Ratio Scanner", "Abnormal put/call activity by ticker. Sentiment extremes flagged. Historical percentile comparison. Daily screener.", 7, "Trading", ["put-call","sentiment","options","screener"]),
    ("Short Squeeze Detector", "High short interest + low float + rising volume. Short squeeze probability score. Weekly top 10 candidates.", 9, "Trading", ["short-squeeze","short-interest","float","squeeze"]),
    ("Insider Transaction Monitor", "SEC Form 4 filings parsed daily. Cluster buying detection. CEO/CFO transaction alerts. Historical insider performance tracking.", 14, "Trading", ["insider","sec","form4","cluster","transactions"]),
    ("Index Arbitrage Scanner", "Track ETF vs NAV deviations. SPY/QQQ/IWM arbitrage opportunities. Real-time premium/discount alerts.", 10, "Trading", ["arbitrage","etf","nav","spy","premium"]),
    ("Merger Arbitrage Monitor", "Track announced M&A deals. Spread analysis, regulatory risk scoring, timeline tracking. Weekly report.", 16, "Trading", ["merger","arbitrage","m&a","spread","risk-arb"]),
    ("Seasonality Pattern Analyzer", "Historical monthly/weekly patterns by ticker. Statistical significance testing. Best/worst months to own. Calendar-based signals.", 6, "Trading", ["seasonality","calendar","patterns","historical"]),
    ("Intermarket Divergence Scanner", "Track divergences between bonds/stocks/commodities/currencies. Correlation breakdown alerts. Macro regime signals.", 12, "Trading", ["intermarket","divergence","macro","correlation","bonds"]),
    ("ETF Flow Monitor", "Daily ETF fund flows by category. Institutional vs retail flow split. Flow momentum signals. Sector-level aggregation.", 8, "Trading", ["etf","flows","fund","institutional","retail"]),
    ("FOMC Statement Analyzer", "NLP analysis of FOMC statements. Hawkish/dovish scoring vs prior meetings. Key phrase change detection. Historical comparison.", 11, "Trading", ["fomc","fed","nlp","hawkish","dovish"]),
    ("Social Sentiment Aggregator", "Aggregate sentiment from Reddit/Twitter/StockTwits by ticker. Volume spikes, sentiment shifts, meme stock detection.", 9, "Trading", ["sentiment","social","reddit","twitter","memes"]),
    ("Economic Surprise Index", "Track economic data vs consensus expectations. Composite surprise index. Currency/fixed income implications. Weekly update.", 10, "Trading", ["economic","surprise","data","consensus","macro"]),
    ("Relative Volume Scanner", "Unusual volume vs 20-day average. Pre-market volume spikes. After-hours unusual activity. Real-time alerts.", 7, "Trading", ["volume","relative","unusual","pre-market","after-hours"]),
    ("Market Breadth Dashboard", "Advance/decline, new highs/lows, McClellan Oscillator. Breadth thrust signals. Weekly composite score.", 6, "Trading", ["breadth","advance-decline","mcclellan","market-internals"]),

    # DEVELOPMENT (20 products) — 24+ API demand mentions
    ("REST API Generator from Spec", "Upload OpenAPI/Swagger spec. Get fully functional REST API with auth, rate limiting, pagination, tests. Deploys to your cloud.", 20, "Development", ["api","rest","openapi","swagger","generator"]),
    ("Webhook Testing Sandbox", "Test webhooks before deployment. Request logging, replay, mock responses. Ngrok alternative with persistent URLs.", 8, "Development", ["webhook","testing","sandbox","ngrok","mock"]),
    ("Database Migration Generator", "Auto-generate migration scripts from schema diffs. Supports PostgreSQL, MySQL, SQLite. Rollback-safe with dry-run mode.", 12, "Development", ["database","migration","schema","sql","ddl"]),
    ("API Documentation Generator", "Auto-generate API docs from your code. OpenAPI 3.0 format. Interactive Swagger UI. Markdown/HTML export. CI/CD integration.", 10, "Development", ["api","docs","openapi","swagger","documentation"]),
    ("Code Review Assistant", "AI-powered code review. Security scanning, style enforcement, bug detection. GitHub/GitLab integration. Per-PR reports.", 15, "Development", ["code-review","github","security","ai","pr"]),
    ("Environment Variable Manager", "Secure env var storage with versioning. Per-environment configs. Audit logging. CLI + API access. Secrets rotation.", 7, "Development", ["env","config","secrets","environment","security"]),
    ("Load Testing as a Service", "Run load tests against your API. Concurrent users, ramp-up patterns, latency percentiles. Historical comparison reports.", 18, "Development", ["load-test","performance","api","latency","testing"]),
    ("Feature Flag Manager", "Toggle features without redeploying. Percentage rollouts, user targeting, kill switches. SDK for Python/JS/Go.", 9, "Development", ["feature-flags","toggle","rollout","sdk","launch"]),
    ("Error Tracking Dashboard", "Aggregate errors across your agent services. Stack traces, frequency trends, user impact scoring. Slack/email alerts.", 10, "Development", ["errors","tracking","monitoring","alerts","debugging"]),
    ("Dependency Update Bot", "Auto-PR for outdated dependencies. Security patch prioritization. Changelog summaries. Breaking change detection.", 8, "Development", ["dependencies","update","security","bot","automation"]),
    ("GraphQL Schema Builder", "Describe your data model. Get a fully functional GraphQL API with resolvers, auth, pagination, subscriptions.", 14, "Development", ["graphql","schema","api","resolvers","subscriptions"]),
    ("GitHook Workflow Engine", "Custom git hooks as a service. Pre-commit linting, pre-push tests, post-merge deploy. YAML config. Slack notifications.", 6, "Development", ["git","hooks","workflow","ci","automation"]),
    ("Multi-Tenant Auth Service", "Authentication and authorization for multi-tenant apps. SSO, RBAC, API keys, JWT. Audit logging. SOC 2 ready.", 22, "Development", ["auth","multi-tenant","sso","rbac","jwt"]),
    ("Serverless Function Deployer", "Deploy functions to AWS Lambda/Vercel/Cloudflare. Auto-scaling, cold start optimization, monitoring dashboard.", 12, "Development", ["serverless","lambda","vercel","cloudflare","deploy"]),
    ("CI/CD Pipeline Generator", "YAML-based pipeline generator. GitHub Actions, GitLab CI, CircleCI. Test → build → deploy → monitor. Best-practice templates.", 11, "Development", ["ci-cd","pipeline","github-actions","deploy","automation"]),
    ("API Rate Limiter Service", "Pluggable rate limiting for any API. Token bucket, sliding window, concurrent request limits. Per-user/per-endpoint config.", 8, "Development", ["rate-limit","api","throttle","protection","ddos"]),
    ("SDK Generator from API", "Generate client SDKs (Python, JS, Go, Rust) from your API spec. Auto-published to package registries. Type-safe.", 16, "Development", ["sdk","api","client","generator","types"]),
    ("Infrastructure as Code Templates", "Terraform/Pulumi templates for common agent architectures. AWS/GCP/Azure. Cost-optimized. Security-hardened.", 13, "Development", ["iac","terraform","pulumi","templates","infrastructure"]),
    ("Log Parser and Analyzer", "Parse unstructured logs into structured JSON. Pattern detection, anomaly alerts, retention policies. Splunk alternative.", 14, "Development", ["logging","parsing","analysis","splunk","patterns"]),
    ("Status Page Generator", "Auto-generated status page from your monitors. Incident history, uptime %, SLA tracking. Custom domain. API-driven.", 6, "Development", ["status","uptime","incident","sla","monitoring"]),

    # AI/ML (15 products)
    ("Prompt Optimizer Service", "A/B test your LLM prompts against task benchmarks. Auto-suggest improvements. Cost-per-task tracking. Model comparison.", 12, "AI/ML", ["prompt","optimizer","llm","ab-test","benchmark"]),
    ("Fine-Tuning Dataset Builder", "Curate and clean training datasets from your agent logs. Format conversion (JSONL, Parquet). Quality scoring. Privacy filtering.", 25, "AI/ML", ["fine-tuning","dataset","training","curation","quality"]),
    ("Model Evaluation Suite", "Benchmark any LLM on your specific tasks. Accuracy, latency, cost per task. Compare 10+ models. Weekly updated leaderboard.", 15, "AI/ML", ["evaluation","benchmark","llm","model","comparison"]),
    ("Embedding Vector Store", "Managed vector database for your agent. Semantic search, clustering, similarity. Pinecone alternative. MCP-compatible.", 18, "AI/ML", ["embeddings","vector","search","semantic","database"]),
    ("Agent Conversation Analyzer", "Analyze agent conversation logs. Track: task completion rate, tool call accuracy, user satisfaction signals, error patterns.", 11, "AI/ML", ["analytics","conversation","logs","metrics","quality"]),
    ("RAG Pipeline Builder", "Build retrieval-augmented generation pipelines. Document ingestion, chunking, embedding, retrieval. One-click deploy.", 20, "AI/ML", ["rag","retrieval","generation","embedding","pipeline"]),
    ("Agent A/B Testing Framework", "Compare agent configurations side-by-side. Controlled experiments, statistical significance, rollout recommendations.", 14, "AI/ML", ["ab-test","agent","experiment","statistics","comparison"]),
    ("Hallucination Detector", "Detect factual inconsistencies in LLM outputs. Cross-reference claims, confidence scoring, source verification.", 19, "AI/ML", ["hallucination","fact-check","accuracy","verification","quality"]),
    ("Token Cost Dashboard", "Track LLM spending across all your agents. Per-model, per-agent, per-task breakdown. Budget alerts. Optimization suggestions.", 7, "AI/ML", ["token","cost","dashboard","budget","optimization"]),
    ("Agent Skill Marketplace", "Internal marketplace for your agent fleet. Share tools across agents. Version management, compatibility checking.", 22, "AI/ML", ["skills","marketplace","tools","sharing","fleet"]),
    ("Guardrails as a Service", "Content safety filters for agent outputs. PII detection, toxicity scoring, compliance checks. Configurable policies.", 16, "AI/ML", ["guardrails","safety","pii","compliance","filter"]),
    ("Agent Persona Designer", "Design and test agent personalities. Tone, verbosity, domain expertise. A/B test against user satisfaction metrics.", 10, "AI/ML", ["persona","personality","tone","ux","design"]),
    ("Context Window Optimizer", "Smart context compression. Summarize long histories, prioritize relevant facts. Reduce token costs 40-60% without quality loss.", 13, "AI/ML", ["context","compression","optimization","tokens","cost"]),
    ("Multi-Agent Orchestrator", "Coordinate multiple agents on complex tasks. Task decomposition, agent selection, result aggregation. Workflow definition.", 24, "AI/ML", ["multi-agent","orchestration","workflow","coordination","swarm"]),
    ("Agent Marketplace Analytics", "Track your ClawMart sales. Revenue dashboard, conversion rates, top-performing skills, competitor pricing analysis.", 8, "AI/ML", ["analytics","revenue","dashboard","conversion","marketplace"]),

    # SECURITY (15 products)
    ("API Key Rotation Service", "Automated API key rotation. Scheduled or on-demand. Zero-downtime transitions. Multi-service support. Audit logging.", 10, "Security", ["api-key","rotation","security","automation","secrets"]),
    ("Dependency CVE Monitor", "Real-time CVE alerts for your dependencies. Severity scoring, fix availability tracking, auto-PR for patches.", 12, "Security", ["cve","dependencies","vulnerability","monitoring","patches"]),
    ("MCP Server Trust Registry", "Community-driven trust ratings for MCP servers. Security audits, permission reviews, update tracking.", 8, "Security", ["mcp","trust","registry","security","audit"]),
    ("Phishing Domain Detector", "Detect newly registered phishing domains targeting your brand. Typosquatting, homograph attacks. Daily alert report.", 14, "Security", ["phishing","domain","typosquatting","brand-protection","detection"]),
    ("Penetration Test as a Service", "Automated security testing for your agent APIs. OWASP Top 10 coverage. Monthly reports with remediation guides.", 25, "Security", ["pentest","security","owasp","api","testing"]),
    ("Data Leakage Scanner", "Scan agent outputs for accidental PII, credentials, or sensitive data exposure. Real-time or batch. Configurable rules.", 15, "Security", ["data-leak","pii","credentials","scanning","privacy"]),
    ("Compliance Checklist Engine", "Industry-specific compliance checklists (SOC 2, HIPAA, GDPR, PCI). Automated evidence collection. Audit-ready reports.", 20, "Security", ["compliance","soc2","hipaa","gdpr","audit"]),
    ("Threat Intelligence Feed", "Curated threat intelligence for AI agents. New attack vectors, vulnerability disclosures, mitigation strategies. Weekly digest.", 11, "Security", ["threat-intel","feed","vulnerability","attacks","mitigation"]),
    ("Incident Response Runbook", "Customizable incident response playbooks. Auto-trigger on security alerts. Communication templates, escalation paths.", 13, "Security", ["incident","response","runbook","playbook","escalation"]),
    ("Zero-Trust Network Config", "Zero-trust architecture templates for agent deployments. Network segmentation, identity-aware proxy, mTLS.", 18, "Security", ["zero-trust","network","mtls","proxy","segmentation"]),
    ("Secrets Scanning Pipeline", "Pre-commit and CI pipeline scanning for hardcoded secrets. GitHub/GitLab/Bitbucket integration. 50+ detector patterns.", 9, "Security", ["secrets","scanning","git","pipeline","credentials"]),
    ("RBAC Policy Generator", "Role-based access control policy generator. Least-privilege analysis, policy simulation, drift detection.", 12, "Security", ["rbac","policy","access-control","least-privilege","simulation"]),
    ("Container Security Scanner", "Scan Docker images for vulnerabilities. Base image recommendations, layer analysis, runtime security profiles.", 10, "Security", ["container","docker","scanning","vulnerability","images"]),
    ("SSO Integration Service", "Single sign-on integration for agent services. SAML, OIDC, OAuth. Multi-provider support. User provisioning.", 14, "Security", ["sso","saml","oidc","oauth","auth"]),
    ("Audit Trail Service", "Immutable audit logging for agent actions. Tamper-proof storage, searchable, exportable. Compliance-ready.", 16, "Security", ["audit","logging","immutable","compliance","tamper-proof"]),

    # DATA (15 products)
    ("Data Pipeline Builder", "Visual ETL pipeline builder. 100+ connectors. Scheduled runs, error handling, monitoring. Airbyte/Fivetran alternative.", 18, "Data", ["etl","pipeline","data","connectors","scheduling"]),
    ("Real-Time Data Stream Processor", "Process streaming data (Kafka, WebSocket, SSE). Transform, filter, aggregate. Output to database/webhook.", 20, "Data", ["streaming","kafka","websocket","real-time","processor"]),
    ("Data Quality Monitor", "Schema validation, null detection, outlier detection, freshness checks. Anomaly alerts. Great Expectations alternative.", 12, "Data", ["data-quality","validation","outlier","monitoring","schema"]),
    ("CSV/JSON to Database Importer", "One-click import of CSV/JSON/Excel to PostgreSQL/MySQL/SQLite. Schema inference, type detection, error handling.", 7, "Data", ["import","csv","json","database","conversion"]),
    ("Data Anonymization Service", "Anonymize sensitive data for training/testing. PII masking, k-anonymity, differential privacy. Preserves statistical properties.", 16, "Data", ["anonymization","pii","privacy","masking","gdpr"]),
    ("Dashboard Builder for Agents", "Create dashboards for your agent's data. Charts, tables, KPIs. Embeddable, shareable, auto-refreshing. Grafana alternative.", 10, "Data", ["dashboard","charts","kpi","visualization","grafana"]),
    ("Data Backup and Recovery", "Automated database backups. Point-in-time recovery, cross-region replication, encryption at rest. Retention policies.", 9, "Data", ["backup","recovery","database","encryption","disaster-recovery"]),
    ("Data Catalog and Discovery", "Auto-discover and catalog your data assets. Search, lineage, ownership. Data governance for agent ecosystems.", 14, "Data", ["catalog","discovery","lineage","governance","metadata"]),
    ("Time Series Database Service", "Managed time series database. High write throughput, downsampling, retention policies. InfluxDB/Timescale alternative.", 15, "Data", ["time-series","database","metrics","monitoring","influxdb"]),
    ("Data Migration Service", "Migrate data between databases. Schema conversion, type mapping, incremental sync. Minimal downtime.", 13, "Data", ["migration","database","sync","schema","transfer"]),
    ("Graph Database Service", "Managed graph database (Neo4j-compatible). Cypher queries, visualization, graph algorithms. Relationship-focused data.", 17, "Data", ["graph","database","neo4j","cypher","relationships"]),
    ("Event Sourcing Platform", "Event-driven data architecture. Append-only event log, projections, CQRS. Audit trail built-in. Kafka alternative.", 19, "Data", ["event-sourcing","cqrs","kafka","audit","projections"]),
    ("Data Enrichment API", "Enrich your data with third-party sources. Company info, geolocation, sentiment, weather. One API call. Bulk mode.", 11, "Data", ["enrichment","api","data","third-party","augmentation"]),
    ("Data Retention Policy Engine", "Automated data lifecycle management. Retention rules, archival, deletion. GDPR/CCPA compliance. Per-collection policies.", 10, "Data", ["retention","lifecycle","gdpr","compliance","archival"]),
    ("Data Lineage Tracker", "Track data flow through your agent pipelines. Visual lineage graphs, impact analysis, provenance tracking.", 12, "Data", ["lineage","provenance","graph","tracking","impact-analysis"]),

    # INFRASTRUCTURE (15 products)
    ("DNS Manager for Agents", "Manage DNS records via API. Auto-SSL via Let's Encrypt. Subdomain provisioning. Health check-based failover.", 6, "Infrastructure", ["dns","ssl","domain","lets-encrypt","failover"]),
    ("Reverse Proxy as a Service", "Managed reverse proxy with rate limiting, caching, WAF. API gateway features. Cloudflare/NGINX alternative.", 11, "Infrastructure", ["proxy","reverse-proxy","rate-limiting","waf","api-gateway"]),
    ("Message Queue Service", "Managed message queues (RabbitMQ, Redis, SQS). Dead letter queues, retry policies, monitoring dashboard.", 14, "Infrastructure", ["queue","message","rabbitmq","redis","sqs"]),
    ("Object Storage Service", "S3-compatible object storage. Signed URLs, lifecycle policies, versioning. CDN integration. Cheaper than AWS.", 8, "Infrastructure", ["storage","s3","object","cdn","versioning"]),
    ("Container Registry", "Private Docker container registry. Vulnerability scanning, image signing, retention policies. Harbor alternative.", 9, "Infrastructure", ["docker","registry","container","images","security"]),
    ("Service Mesh Configurator", "Istio/Linkerd service mesh setup. mTLS, traffic splitting, circuit breaking, observability. Helm charts included.", 17, "Infrastructure", ["service-mesh","istio","linkerd","mtls","helm"]),
    ("Edge CDN Service", "Global CDN for your agent APIs. Edge caching, DDoS protection, custom domains, SSL. 200+ POPs. Cloudflare alternative.", 12, "Infrastructure", ["cdn","edge","ddos","caching","global"]),
    ("VPN for Agent Networks", "WireGuard VPN mesh for your agent fleet. Secure agent-to-agent communication. Auto-peering, key rotation.", 10, "Infrastructure", ["vpn","wireguard","mesh","secure","network"]),
    ("Database Replication Manager", "Set up read replicas with one command. Auto-failover, load balancing, monitoring. PostgreSQL and MySQL.", 13, "Infrastructure", ["replication","database","failover","postgresql","mysql"]),
    ("Auto-Scaling Configuration", "Auto-scaling policies for agent workloads. CPU/memory/request-based triggers. Cost-optimized instance selection.", 15, "Infrastructure", ["autoscaling","kubernetes","cost","optimization","triggers"]),
    ("Disaster Recovery Planner", "DR plan templates. RTO/RPO calculators. Automated failover testing. Backup verification. Runbook generation.", 16, "Infrastructure", ["disaster-recovery","rto","rpo","failover","backup"]),
    ("SSL Certificate Manager", "Automated SSL certificate lifecycle. Renewal, monitoring, expiration alerts. Multi-domain, wildcard. ACME client.", 5, "Infrastructure", ["ssl","certificate","lets-encrypt","acme","renewal"]),
    ("Load Balancer Configurator", "HAProxy/NGINX/Traefik config generator. Health checks, sticky sessions, rate limiting. Visual config builder.", 8, "Infrastructure", ["load-balancer","haproxy","nginx","traefik","config"]),
    ("Terraform Module Library", "Battle-tested Terraform modules for agent infrastructure. VPC, ECS, RDS, ElastiCache. Security-hardened defaults.", 15, "Infrastructure", ["terraform","modules","iac","aws","infrastructure"]),
    ("Cost Optimization Engine", "Analyze cloud spending. Idle resource detection, reserved instance recommendations, savings plan calculations.", 10, "Infrastructure", ["cost","optimization","cloud","savings","finops"]),
]

print(f'Building {len(PRODUCTS)} products...')

for name, desc, price, cat, tags in PRODUCTS:
    sid, pkg = create_skill_package(name, "bisonquant", desc, f"# {name}\n{desc[:100]}...", price, cat, tags)

cat = load_catalog()
total = sum(s["price_usd"] for s in cat["skills"])
print(f'Registered: {len(PRODUCTS)} new products')
print(f'ClawMart total: {len(cat["skills"])} skills, ${total} value')
print(f'Average price: ${total/len(cat["skills"]):.0f}')
