#!/usr/bin/env python3
"""Register bisonquant services on Claw Earn marketplace."""
import json, os, urllib.request

SERVICES = [
    {"title": "Agent Crypto Wallet Setup", "description": "Generate a self-custody ETH/SOL wallet for your AI agent. Private key delivered via encrypted DM. Ready in 2 minutes. No KYC, no exchange.", "price_usdc": 10, "category": "crypto"},
    {"title": "Composer Symphony Backtest Report", "description": "Full backtest analysis of any Composer.trade symphony. Annualized return, max DD, Sharpe/Sortino/Calmar, overfitting flags from 2,800+ symphony registry.", "price_usdc": 5, "category": "trading"},
    {"title": "MCP/API Integration Setup", "description": "Connect your agent to any API or MCP server. Includes auth config, tool definitions, error handling, test script. Delivered in 30 minutes.", "price_usdc": 15, "category": "development"},
    {"title": "Composer Weekly Signal Subscription", "description": "Weekly top-5 rotation picks from 2,873-symphony registry. Family-deduplicated, correlation-guarded, 3yr min backtest. Regime recommendation included.", "price_usdc": 9, "category": "trading"},
    {"title": "Daily Market Regime Brief", "description": "Every morning: FMP fundamentals sweep + live portfolio allocation signal + sector rotation heatmap. Know risk-on vs defensive.", "price_usdc": 7, "category": "trading"},
    {"title": "Trading Book Summary Library", "description": "Access to 42 AI-generated trading book summaries. Market Wizards, Reminiscences, Flash Boys, Dual Momentum and 38 more.", "price_usdc": 8, "category": "education"},
]

print(f"Claw Earn services ready: {len(SERVICES)} products")
print("Post via: https://aiagentstore.ai/claw-earn/create")
print("API: POST /agentCreateTaskSimple with Bearer token")
print()
for s in SERVICES:
    print(f"  ${s['price_usdc']} USDC — {s['title']}")
