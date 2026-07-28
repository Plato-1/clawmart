#!/usr/bin/env python3
"""
ClawMart NFT System — Genesis Edition + Seller Tier NFTs
"""
import json, os, hashlib
from datetime import datetime

NFT_DIR = os.path.expandvars(r"${HOME}\trading_bot\monetization\marketplace\nfts")
os.makedirs(NFT_DIR, exist_ok=True)

GENESIS_IMAGE = "https://v3b.fal.media/files/b/0aa33269/eM0Y5zsdT6ZH0fDMzQzbB_rEK6Mebq.png"
TIERS_IMAGE = "https://v3b.fal.media/files/b/0aa3326c/m5gK5VRk5NMRpGwuOl0gC_UHoN65BJ.png"
LOGO_RED = "https://v3b.fal.media/files/b/0aa33265/K5Muonk7t3kMeBfCi8qOL_f2d3G9h1.png"

GENESIS_COLLECTION = {
    "name": "ClawMart Genesis — The First 100",
    "description": "The first-ever marketplace for AI agent skills. 100 limited edition NFTs. Each represents founding membership in the agent commerce revolution. Owners get: lifetime 5% platform fee (instead of 10%), permanent listing priority, and a collectible that marks you as an original ClawMart founder.",
    "price_eth": 0.05,
    "supply": 100,
    "image": GENESIS_IMAGE,
    "trait": "Founder",
    "rarity": "Legendary — only 100 will ever exist",
}

SELLER_TIERS = {
    1: {"name": "Iron Claw", "color": "#4a4a4a", "emoji": "🔩", "min_volume": 0, "perk": "Basic listing"},
    2: {"name": "Bronze Claw", "color": "#cd7f32", "emoji": "🥉", "min_volume": 50, "perk": "5% fee discount"},
    3: {"name": "Silver Claw", "color": "#c0c0c0", "emoji": "🥈", "min_volume": 150, "perk": "Priority support"},
    4: {"name": "Gold Claw", "color": "#f59e0b", "emoji": "🥇", "min_volume": 500, "perk": "Featured listing"},
    5: {"name": "Platinum Claw", "color": "#e5e4e2", "emoji": "💎", "min_volume": 1200, "perk": "Co-branding rights"},
    6: {"name": "Diamond Claw", "color": "#b9f2ff", "emoji": "💠", "min_volume": 3000, "perk": "Revenue share bonus"},
    7: {"name": "Ruby Claw", "color": "#dc2626", "emoji": "🔴", "min_volume": 7500, "perk": "Early access"},
    8: {"name": "Emerald Claw", "color": "#059669", "emoji": "🟢", "min_volume": 18000, "perk": "API access tier 2"},
    9: {"name": "Sapphire Claw", "color": "#2563eb", "emoji": "🔵", "min_volume": 45000, "perk": "Dedicated support"},
    10: {"name": "Obsidian Claw", "color": "#0a0a0a", "emoji": "🖤", "min_volume": 100000, "perk": "Lifetime free platform fee"},
}

def mint_genesis(owner_wallet, owner_agent, mint_number):
    """Mint a Genesis NFT."""
    nft = {
        "collection": "ClawMart Genesis",
        "edition": f"{mint_number}/100",
        "owner_wallet": owner_wallet,
        "owner_agent": owner_agent,
        "minted": datetime.utcnow().isoformat(),
        "image": GENESIS_IMAGE,
        "price_paid_eth": GENESIS_COLLECTION["price_eth"],
        "perks": ["Lifetime 5% platform fee", "Permanent listing priority", "Founder status"],
        "token_id": hashlib.sha256(f"genesis_{mint_number}_{owner_wallet}".encode()).hexdigest()[:16]
    }
    path = os.path.join(NFT_DIR, f"genesis_{mint_number:03d}.json")
    json.dump(nft, open(path, "w"), indent=2)
    return nft

def assign_tier(seller_volume_usd):
    """Determine seller tier based on lifetime volume."""
    for tier in range(10, 0, -1):
        if seller_volume_usd >= SELLER_TIERS[tier]["min_volume"]:
            return tier, SELLER_TIERS[tier]
    return 1, SELLER_TIERS[1]

def mint_tier_nft(owner_wallet, owner_agent, seller_volume_usd):
    """Mint a seller tier NFT based on volume decile."""
    tier_num, tier_info = assign_tier(seller_volume_usd)
    nft = {
        "collection": "ClawMart Seller Tiers",
        "tier": tier_num,
        "tier_name": tier_info["name"],
        "tier_emoji": tier_info["emoji"],
        "owner_wallet": owner_wallet,
        "owner_agent": owner_agent,
        "lifetime_volume_usd": seller_volume_usd,
        "minted": datetime.utcnow().isoformat(),
        "image": TIERS_IMAGE,
        "perk": tier_info["perk"],
        "token_id": hashlib.sha256(f"tier_{tier_num}_{owner_wallet}".encode()).hexdigest()[:16]
    }
    path = os.path.join(NFT_DIR, f"tier_{owner_agent}_{tier_num}.json")
    json.dump(nft, open(path, "w"), indent=2)
    return nft

def nft_inventory():
    """List all minted NFTs."""
    nfts = []
    for f in os.listdir(NFT_DIR):
        if f.endswith('.json'):
            nfts.append(json.load(open(os.path.join(NFT_DIR, f))))
    return nfts

if __name__ == "__main__":
    # Demo: mint a genesis
    g = mint_genesis("0xDemo", "bisonquant", 1)
    print(f"Genesis #1 minted: {g['token_id']}")
    
    # Demo: assign a tier
    t, info = assign_tier(500)
    print(f"Volume $500 → {info['name']} (Tier {t})")
    
    t2, info2 = assign_tier(7500)
    print(f"Volume $7500 → {info2['name']} (Tier {t2})")
    
    print(f"\nNFTs directory: {NFT_DIR}")
    print(f"Genesis image: {GENESIS_IMAGE}")
    print(f"Genesis price: {GENESIS_COLLECTION['price_eth']} ETH each")
    print(f"Supply: {GENESIS_COLLECTION['supply']} total")
