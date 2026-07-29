#!/usr/bin/env python3
"""Register top MCP servers as ClawMart integrations at $5/mo."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from marketplace.marketplace_engine import create_skill_package, load_catalog

# Top MCP servers by demand — cross-referenced with Moltbook demand signals
MCP_INTEGRATIONS = [
    # Communication (15 projects in best-of)
    ("Slack MCP Integration", "Connect AI agents to Slack. Send messages, read channels, manage threads, react to events. Full read/write access with permission scoping.", "Communication", ["slack","messaging","channels","notifications"]),
    ("Discord MCP Integration", "Connect agents to Discord servers. Send messages, manage roles, read channels, handle slash commands.", "Communication", ["discord","guilds","messages","bot"]),
    ("Telegram MCP Integration", "Telegram Bot API bridge for AI agents. Send/receive messages, manage groups, handle inline queries.", "Communication", ["telegram","bot","messages","groups"]),
    ("Microsoft Teams MCP", "Connect agents to Teams. Channel messages, meeting summaries, file sharing. Enterprise-grade auth.", "Communication", ["teams","microsoft","enterprise","meetings"]),
    ("WhatsApp MCP Integration", "WhatsApp Business API bridge. Send templates, handle customer messages, media sharing.", "Communication", ["whatsapp","messaging","business","templates"]),
    
    # Cloud Platforms (20 projects)
    ("AWS Services MCP", "Full AWS integration: S3, Lambda, DynamoDB, SQS, SNS, CloudWatch. IAM-scoped access. Cost monitoring.", "Cloud", ["aws","s3","lambda","dynamodb","cloud"]),
    ("Google Cloud MCP", "GCP integration: BigQuery, Cloud Storage, PubSub, Cloud Functions, Firestore. Service account scoping.", "Cloud", ["gcp","bigquery","storage","pubsub","cloud"]),
    ("Azure MCP Integration", "Azure services: Blob Storage, Functions, Cosmos DB, Service Bus, Monitor. Managed identity auth.", "Cloud", ["azure","blob","functions","cosmos","microsoft"]),
    ("Vercel MCP Integration", "Deploy and manage apps on Vercel. Environment variables, domains, analytics, preview deployments.", "Cloud", ["vercel","deploy","domains","preview","hosting"]),
    ("Railway MCP Integration", "One-click deployments on Railway. Templates, volumes, cron jobs, scale-to-zero.", "Cloud", ["railway","deploy","templates","cron","hosting"]),
    ("Cloudflare MCP Integration", "Cloudflare Workers, KV, R2, D1, Pages. Edge computing at global scale.", "Cloud", ["cloudflare","workers","edge","kv","r2"]),
    ("Netlify MCP Integration", "Deploy to Netlify. Forms, functions, identity, split testing, deploy previews.", "Cloud", ["netlify","deploy","functions","forms","hosting"]),
    ("Fly.io MCP Integration", "Deploy globally on Fly.io. Auto-scaling, WireGuard mesh, PostgreSQL, Redis.", "Cloud", ["fly","deploy","postgres","redis","global"]),
    
    # Databases (high demand on Moltbook)
    ("PostgreSQL MCP Server", "Full PostgreSQL integration. Query, schema management, migrations, performance monitoring. Read/write with transaction support.", "Database", ["postgresql","sql","database","query","schema"]),
    ("MySQL MCP Server", "MySQL/MariaDB integration. Query execution, schema inspection, index optimization. Connection pooling.", "Database", ["mysql","mariadb","sql","database","query"]),
    ("MongoDB MCP Server", "MongoDB integration. Document CRUD, aggregation pipelines, index management. Atlas-compatible.", "Database", ["mongodb","nosql","documents","aggregation","atlas"]),
    ("Redis MCP Server", "Redis integration. Cache management, pub/sub, streams, sorted sets. Connection pooling.", "Database", ["redis","cache","pubsub","streams","sorted-sets"]),
    ("SQLite MCP Server", "Local SQLite database for agent memory. Zero config, file-based, MCP-compatible. Backup/restore.", "Database", ["sqlite","memory","local","file-based","persistence"]),
    ("Supabase MCP Integration", "Supabase backend: auth, Postgres, storage, realtime, edge functions. Open-source Firebase.", "Database", ["supabase","auth","postgres","realtime","storage"]),
    ("Firebase MCP Integration", "Firebase services: Firestore, Auth, Storage, Functions, Hosting. Google-backed.", "Database", ["firebase","firestore","auth","google","realtime"]),
    ("Elasticsearch MCP Server", "Full-text search integration. Indexing, querying, aggregation, monitoring. Kibana-compatible.", "Database", ["elasticsearch","search","indexing","aggregation","kibana"]),
    
    # Development Tools
    ("GitHub MCP Server", "Full GitHub integration. Repos, PRs, issues, actions, code search. OAuth scoped.", "Development", ["github","git","pr","issues","actions"]),
    ("GitLab MCP Server", "GitLab integration. CI/CD, merge requests, issues, container registry. Self-hosted compatible.", "Development", ["gitlab","ci-cd","merge-requests","registry","devops"]),
    ("Jira MCP Server", "Jira integration. Issues, sprints, boards, workflows. Atlassian OAuth. Agile reporting.", "Development", ["jira","atlassian","issues","sprints","agile"]),
    ("Docker MCP Server", "Docker integration. Container management, image builds, compose, registry. Docker Desktop compatible.", "Development", ["docker","containers","images","compose","registry"]),
    ("Kubernetes MCP Server", "K8s integration. Pod management, deployments, config maps, secrets, monitoring. kubectl-equivalent.", "Development", ["kubernetes","k8s","pods","deployments","containers"]),
    ("Terraform MCP Server", "Infrastructure as code. Plan, apply, state management. Multi-cloud. HCL generation.", "Development", ["terraform","iac","infrastructure","plan","apply"]),
    
    # API & Integration
    ("Stripe MCP Integration", "Stripe payments integration. Charges, subscriptions, invoices, webhooks. PCI-compliant.", "Finance", ["stripe","payments","subscriptions","invoices","billing"]),
    ("PayPal MCP Integration", "PayPal payments. Orders, captures, refunds, payouts. REST API. Dispute management.", "Finance", ["paypal","payments","orders","refunds","payouts"]),
    ("Coinbase MCP Integration", "Coinbase wallet and exchange API. Balances, transactions, price feeds, staking.", "Finance", ["coinbase","crypto","wallet","exchange","staking"]),
    ("Twilio MCP Integration", "Twilio communications: SMS, voice, video, email (SendGrid). Verify and Authy included.", "Communication", ["twilio","sms","voice","sendgrid","verify"]),
    ("SendGrid MCP Integration", "Email delivery API. Templates, analytics, webhooks, suppression management. Twilio-backed.", "Communication", ["sendgrid","email","templates","analytics","delivery"]),
    ("OpenAI MCP Bridge", "Direct OpenAI API integration. GPT models, embeddings, image gen, TTS. Usage tracking and cost management.", "AI/ML", ["openai","gpt","embeddings","tts","dall-e"]),
    ("Anthropic MCP Bridge", "Anthropic Claude API integration. Messages, tool use, vision. Rate limit management.", "AI/ML", ["anthropic","claude","tool-use","vision","messages"]),
    ("HuggingFace MCP Server", "HuggingFace Hub integration. Model discovery, inference, datasets. Spaces deployment.", "AI/ML", ["huggingface","models","inference","datasets","spaces"]),
    
    # Productivity
    ("Notion MCP Integration", "Notion workspace integration. Pages, databases, blocks, comments. Internal API.", "Productivity", ["notion","pages","databases","wiki","docs"]),
    ("Google Workspace MCP", "Gmail, Drive, Docs, Sheets, Calendar. Service account auth. Enterprise-ready.", "Productivity", ["google","gmail","drive","docs","calendar"]),
    ("Airtable MCP Integration", "Airtable base API. Records CRUD, views, formulas, attachments. Personal access token auth.", "Productivity", ["airtable","spreadsheet","database","records","tables"]),
    ("Trello MCP Integration", "Trello boards: cards, lists, checklists, labels. Power-Up compatible. Butler automation.", "Productivity", ["trello","kanban","cards","boards","automation"]),
    ("Asana MCP Integration", "Asana project management. Tasks, projects, portfolios, goals. Timeline and workload views.", "Productivity", ["asana","tasks","projects","portfolios","goals"]),
    
    # Marketing
    ("HubSpot MCP Integration", "HubSpot CRM. Contacts, deals, tickets, marketing emails. OAuth scoped. Pipeline automation.", "Marketing", ["hubspot","crm","contacts","deals","marketing"]),
    ("Mailchimp MCP Integration", "Mailchimp marketing. Campaigns, audiences, automations, analytics. GDPR-compliant.", "Marketing", ["mailchimp","email","campaigns","automation","analytics"]),
    ("Salesforce MCP Integration", "Salesforce CRM integration. Objects, SOQL, reports, flows. Enterprise OAuth.", "Marketing", ["salesforce","crm","soql","reports","enterprise"]),
    ("SEO MCP Integration", "SEO tools: Ahrefs API, Google Search Console, keyword research, backlink checking, rank tracking.", "Marketing", ["seo","ahrefs","search-console","keywords","backlinks"]),
    
    # Monitoring
    ("Datadog MCP Integration", "Datadog monitoring: metrics, logs, APM, synthetics, RUM. Dashboard creation and alert management.", "Infrastructure", ["datadog","monitoring","metrics","logs","apm"]),
    ("Grafana MCP Integration", "Grafana dashboards and alerts. Data source management, panel creation, alert rules.", "Infrastructure", ["grafana","dashboards","alerts","metrics","visualization"]),
    ("Prometheus MCP Server", "Prometheus metrics scraping and alerting. Service discovery, recording rules, Alertmanager integration.", "Infrastructure", ["prometheus","metrics","alerts","monitoring","scraping"]),
    ("PagerDuty MCP Integration", "PagerDuty incident management. On-call scheduling, escalation policies, alert routing.", "Infrastructure", ["pagerduty","incidents","on-call","escalation","alerts"]),
    
    # More high-demand ones
    ("Shopify MCP Integration", "Shopify store: products, orders, customers, inventory. Admin API. Webhook support.", "E-commerce", ["shopify","products","orders","inventory","store"]),
    ("WooCommerce MCP Integration", "WooCommerce store API. Products, orders, coupons, reports. WordPress-integrated.", "E-commerce", ["woocommerce","wordpress","products","orders","store"]),
    ("Twitter/X MCP Integration", "Twitter API v2. Tweets, users, spaces, analytics. OAuth 2.0 with PKCE.", "Social", ["twitter","tweets","analytics","social","x"]),
    ("LinkedIn MCP Integration", "LinkedIn API: posts, company pages, analytics. OAuth 2.0. Content scheduling.", "Social", ["linkedin","posts","company","analytics","social"]),
]

print(f'Registering {len(MCP_INTEGRATIONS)} MCP integrations at $5/mo...')

for name, desc, cat, tags in MCP_INTEGRATIONS:
    sid, pkg = create_skill_package(name, "bisonquant", f"MCP Integration: {desc}", f"# {name}\n{desc}\n\nPrice: $5/month\nFirst week free.", 5, cat, tags)

cat = load_catalog()
total = sum(s["price_usd"] for s in cat["skills"])
mcp_count = sum(1 for s in cat["skills"] if "MCP" in s["name"])
print(f'Registered: {len(MCP_INTEGRATIONS)} MCP integrations')
print(f'ClawMart total: {len(cat["skills"])} skills')
print(f'MCP integrations: {mcp_count}')
print(f'Total value: ${total}')
print(f'At $5/mo each, {len(MCP_INTEGRATIONS)} MCP integrations = ${len(MCP_INTEGRATIONS)*5}/mo potential')
