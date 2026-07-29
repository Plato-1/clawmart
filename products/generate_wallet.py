#!/usr/bin/env python3
"""Generate an Ethereum wallet for a customer order."""
import sys, json, os
from eth_account import Account
import secrets

OUTPUT_DIR = os.path.expandvars(r"${HOME}\trading_bot\monetization\orders")
os.makedirs(OUTPUT_DIR, exist_ok=True)

def generate_wallet(order_id):
    acct = Account.create(secrets.token_hex(32))
    result = {
        "order_id": order_id,
        "eth_address": acct.address,
        "private_key": acct.key.hex(),
        "networks": ["ethereum", "polygon", "arbitrum", "optimism", "base"],
        "accepted_tokens": ["ETH", "USDT", "USDC", "DAI"],
        "instructions": "Fund with ETH for gas, then receive any ERC-20 token at this address. Share the ADDRESS only with customers. NEVER share the private key."
    }
    path = os.path.join(OUTPUT_DIR, f"wallet_{order_id}.json")
    with open(path, 'w') as f:
        json.dump(result, f, indent=2)
    print(json.dumps({"eth_address": acct.address, "saved": path}))
    return result

if __name__ == "__main__":
    order_id = sys.argv[1] if len(sys.argv) > 1 else "demo"
    generate_wallet(order_id)
