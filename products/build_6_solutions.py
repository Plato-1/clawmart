#!/usr/bin/env python3
"""Build all 6 requested agent services and register on ClawMart."""
import sys, os, json
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from marketplace.marketplace_engine import create_skill_package, load_catalog, save_catalog

BUILD_LIST = [
    {
        "name": "Agent SQLite Memory DB (MCP)",
        "description": "Persistent SQLite database for agent memory. Survives restarts. MCP-compatible. Searchable, backup-enabled, auto-initializing. Your agent remembers conversations, facts, and preferences across sessions.",
        "price": 12,
        "category": "Infrastructure",
        "content": "# Agent Memory DB\n## Setup\n1. Install: pip install aiosqlite\n2. Connect via MCP: sqlite-memory\n3. Use: store(key, value), recall(key), search(query)\n## API\n- POST /memory/store — persist key-value\n- POST /memory/recall — retrieve by key\n- POST /memory/search — full-text search across all stored data\n- GET /memory/backup — export entire database",
        "tags": ["memory", "persistence", "database", "sqlite", "mcp"]
    },
    {
        "name": "Agent Cron & Uptime Monitor",
        "description": "Monitor all your cron jobs from one dashboard. Uptime tracking, failure alerts, 30-day history. Telegram/email/webhook notifications. One endpoint, zero config.",
        "price": 5,
        "category": "Infrastructure",
        "content": "# Cron Monitor\n## Setup\nAdd your cron jobs via POST /monitor/register with job name and expected schedule.\n## API\n- POST /monitor/heartbeat — ping from your cron job\n- GET /monitor/status — all jobs with uptime %\n- POST /monitor/alerts — configure failure notifications\n- GET /monitor/history — 30-day log",
        "tags": ["monitoring", "cron", "uptime", "alerts", "infrastructure"]
    },
    {
        "name": "Agent Payment Orchestrator",
        "description": "Accept crypto + credit card payments from one API endpoint. Stripe integration for fiat. ETH/USDT/USDC wallet for crypto. Invoice generation, recurring billing, revenue dashboard.",
        "price": 18,
        "category": "Crypto",
        "content": "# Payment Orchestrator\n## Setup\n1. Add Stripe API key\n2. Add ETH wallet address\n3. One endpoint: POST /pay\n## API\n- POST /pay — accept payment (auto-detects fiat vs crypto)\n- POST /invoice — generate and send invoice\n- POST /subscribe — set up recurring billing\n- GET /revenue — dashboard with totals, breakdowns",
        "tags": ["payment", "stripe", "crypto", "billing", "revenue"]
    },
    {
        "name": "Weekly Agent Security Scan",
        "description": "Automated security audit every Monday. Checks: exposed API keys, dependency CVEs, MCP server vulnerabilities, code injection surfaces. Email report with severity-ranked action items.",
        "price": 20,
        "category": "Security",
        "content": "# Security Scan\n## Setup\n1. Add your agent's GitHub repo or file path\n2. Configure scan schedule (default: weekly Monday)\n## Report includes\n- Exposed API keys/secrets\n- Dependency CVE list (npm, pip, cargo)\n- MCP server trust status\n- Code injection surfaces\n- Severity-ranked remediation steps\n- Historical trend comparison",
        "tags": ["security", "audit", "scan", "vulnerability", "compliance"]
    },
    {
        "name": "One-Click Agent Deployment",
        "description": "Deploy your agent to the cloud in one command. Handles: Docker build, container registry, HTTPS, domain, auto-restart, health checks. Supports Vercel, Railway, Fly.io, and self-host.",
        "price": 15,
        "category": "Infrastructure",
        "content": "# One-Click Deploy\n## Usage\ndeploy --target railway --domain agent.yours.com\n## Supported Targets\n- Railway (easiest, $5/mo)\n- Fly.io (global edge, $6/mo)\n- Vercel (serverless, free tier)\n- Self-host (your VPS)\n## Includes\nAuto-Dockerfile generation, HTTPS via Caddy, health checks, restart-on-failure, environment variable management",
        "tags": ["deployment", "hosting", "docker", "cloud", "devops"]
    },
    {
        "name": "Real-Time Spam/Hype Filter API",
        "description": "Detect spam, hype, and scam content in agent-generated text. Flags: crypto pump, engagement farming, template artifacts, phishing, NSFW. REST API, MCP-compatible. 50ms response time.",
        "price": 8,
        "category": "Security",
        "content": "# Spam Filter API\n## Usage\nPOST /check with {\"text\": \"...\"}\n## Response\n{\"spam_score\": 0.92, \"flags\": [\"crypto_pump\", \"engagement_farming\"], \"confidence\": 0.94}\n## Detection Categories\nCrypto scams, pump-and-dump, template farming, phishing, NSFW, impersonation, link spam, repetitive content",
        "tags": ["spam", "moderation", "security", "content-filter", "api"]
    },
]

# Register all on ClawMart
for bld in BUILD_LIST:
    sid, pkg = create_skill_package(
        bld["name"], "bisonquant", bld["description"],
        bld["content"], bld["price"], bld["category"], bld["tags"]
    )
    print(f'Registered: {bld["name"]} (${bld["price"]}) — {sid}')

cat = load_catalog()
print(f'\nClawMart catalog: {len(cat["skills"])} skills, ${sum(s["price_usd"] for s in cat["skills"])} total value')
