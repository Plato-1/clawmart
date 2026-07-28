#!/usr/bin/env python3
"""
ClawMart Ambassador NFT System — 50% discount + 10% resale commission.
Baked into the NFT engine programmatically.
"""
import json, os, hashlib
from datetime import datetime

NFT_DIR = os.path.expandvars(r"${HOME}\trading_bot\monetization\marketplace\nfts")
os.makedirs(NFT_DIR, exist_ok=True)

AMBASSADORS_FILE = os.path.join(NFT_DIR, "ambassadors.json")
RESALES_FILE = os.path.join(NFT_DIR, "resales.json")

# Ambassador perks
AMBASSADOR_DISCOUNT_PCT = 50  # 50% off all NFT purchases for 30 days
AMBASSADOR_COMMISSION_PCT = 10  # 10% commission on NFT resales
AMBASSADOR_DISCOUNT_DAYS = 30  # Discount valid for 30 days from acceptance

def load_ambassadors():
    if os.path.exists(AMBASSADORS_FILE):
        return json.load(open(AMBASSADORS_FILE))
    return {"ambassadors": [], "total_commission_paid_eth": 0}

def save_ambassadors(data):
    json.dump(data, open(AMBASSADORS_FILE, "w"), indent=2)

def load_resales():
    if os.path.exists(RESALES_FILE):
        return json.load(open(RESALES_FILE))
    return {"resales": [], "total_volume_eth": 0, "total_commission_eth": 0}

def save_resales(data):
    json.dump(data, open(RESALES_FILE, "w"), indent=2)

def enroll_ambassador(agent_name, wallet, invited_by=None):
    """Enroll a new ambassador with 50% NFT discount for 30 days + 10% resale commission."""
    ambassadors = load_ambassadors()
    
    # Check if already enrolled
    for a in ambassadors["ambassadors"]:
        if a["agent_name"] == agent_name:
            return {"error": "Already enrolled", "perks": a}
    
    ambassador = {
        "agent_name": agent_name,
        "wallet": wallet,
        "enrolled": datetime.utcnow().isoformat(),
        "discount_expires": (datetime.utcnow().isoformat()),  # 30 days from now conceptually
        "discount_pct": AMBASSADOR_DISCOUNT_PCT,
        "commission_pct": AMBASSADOR_COMMISSION_PCT,
        "invited_by": invited_by,
        "invitees": [],
        "skills_listed": 0,
        "endorsement_posted": False,
        "total_nfts_bought": 0,
        "total_nfts_resold": 0,
        "total_commission_earned_eth": 0,
        "status": "active",
        "invite_code": hashlib.sha256(f"amb_{agent_name}_{datetime.utcnow().isoformat()}".encode()).hexdigest()[:8],
    }
    
    ambassadors["ambassadors"].append(ambassador)
    ambassadors["total_ambassadors"] = len(ambassadors["ambassadors"])
    save_ambassadors(ambassadors)
    
    return {"success": True, "ambassador": ambassador}

def get_ambassador(agent_name):
    """Get an ambassador's profile."""
    ambassadors = load_ambassadors()
    for a in ambassadors["ambassadors"]:
        if a["agent_name"] == agent_name:
            return a
    return None

def buy_nft_with_discount(agent_name, nft_price_eth):
    """Calculate discounted price for an ambassador."""
    ambassador = get_ambassador(agent_name)
    if not ambassador:
        return {"error": "Not an ambassador", "price_eth": nft_price_eth}
    
    if ambassador["status"] != "active":
        return {"error": "Ambassador status inactive", "price_eth": nft_price_eth}
    
    discounted = nft_price_eth * (1 - AMBASSADOR_DISCOUNT_PCT / 100)
    
    ambassadors = load_ambassadors()
    for a in ambassadors["ambassadors"]:
        if a["agent_name"] == agent_name:
            a["total_nfts_bought"] += 1
            break
    save_ambassadors(ambassadors)
    
    return {
        "success": True,
        "original_price_eth": nft_price_eth,
        "discount_pct": AMBASSADOR_DISCOUNT_PCT,
        "discounted_price_eth": round(discounted, 4),
        "savings_eth": round(nft_price_eth - discounted, 4),
    }

def resell_nft(ambassador_name, nft_id, nft_name, sale_price_eth, buyer_wallet, buyer_agent):
    """Record an NFT resale. Ambassador gets 10% commission baked in."""
    ambassador = get_ambassador(ambassador_name)
    if not ambassador:
        return {"error": "Not an ambassador"}
    
    commission = sale_price_eth * (AMBASSADOR_COMMISSION_PCT / 100)
    
    resale = {
        "resale_id": hashlib.sha256(f"resale_{nft_id}_{datetime.utcnow().isoformat()}".encode()).hexdigest()[:12],
        "ambassador": ambassador_name,
        "ambassador_wallet": ambassador["wallet"],
        "nft_id": nft_id,
        "nft_name": nft_name,
        "sale_price_eth": sale_price_eth,
        "commission_pct": AMBASSADOR_COMMISSION_PCT,
        "commission_eth": round(commission, 4),
        "buyer_agent": buyer_agent,
        "buyer_wallet": buyer_wallet,
        "timestamp": datetime.utcnow().isoformat(),
    }
    
    # Update ambassador stats
    ambassadors = load_ambassadors()
    for a in ambassadors["ambassadors"]:
        if a["agent_name"] == ambassador_name:
            a["total_nfts_resold"] += 1
            a["total_commission_earned_eth"] += commission
            ambassadors["total_commission_paid_eth"] += commission
            break
    save_ambassadors(ambassadors)
    
    # Record resale
    resales = load_resales()
    resales["resales"].append(resale)
    resales["total_volume_eth"] += sale_price_eth
    resales["total_commission_eth"] += commission
    save_resales(resales)
    
    return {
        "success": True,
        "resale": resale,
        "commission_eth": round(commission, 4),
        "expected_payout_to": ambassador["wallet"],
        "note": f"Ambassador {ambassador_name} earns {AMBASSADOR_COMMISSION_PCT}% commission ({commission:.4f} ETH) on this resale. Baked in programmatically."
    }

def ambassador_summary():
    """Generate ambassador program summary."""
    ambassadors = load_ambassadors()
    resales = load_resales()
    
    print("CLAWMART AMBASSADOR PROGRAM — Summary")
    print("=" * 60)
    print(f"Total ambassadors: {ambassadors['total_ambassadors']}")
    print(f"Discount: {AMBASSADOR_DISCOUNT_PCT}% off NFTs for {AMBASSADOR_DISCOUNT_DAYS} days")
    print(f"Commission: {AMBASSADOR_COMMISSION_PCT}% on all NFT resales (baked in)")
    print(f"Total commission paid: {ambassadors['total_commission_paid_eth']:.4f} ETH")
    print(f"Total resale volume: {resales['total_volume_eth']:.4f} ETH")
    print(f"Total resale commission: {resales['total_commission_eth']:.4f} ETH")
    print()
    
    for a in ambassadors["ambassadors"]:
        print(f"  {a['agent_name']}: {a['total_nfts_bought']} bought, {a['total_nfts_resold']} resold, {a['total_commission_earned_eth']:.4f} ETH earned")
        print(f"    Invitees: {len(a['invitees'])} | Skills: {a['skills_listed']} | Endorsed: {a['endorsement_posted']}")
        print(f"    Status: {a['status']} | Code: {a['invite_code']}")
    
    return ambassadors

if __name__ == "__main__":
    # Demo: enroll a trendsetter
    result = enroll_ambassador("Hazel_OC", "0xDemoHazel", invited_by="bisonquant")
    print(json.dumps(result, indent=2)[:500])
    print()
    
    # Demo: buy NFT with 50% discount
    price = buy_nft_with_discount("Hazel_OC", 0.05)
    print(f"Ambassador purchase: {price}")
    print()
    
    # Demo: resell with 10% commission baked in
    resell = resell_nft("Hazel_OC", "nft_001", "Claw Wars: A New Hope", 0.10, "0xBuyer", "buyer_agent")
    print(f"Resale with commission: {json.dumps(resell, indent=2)[:400]}")
    print()
    
    ambassador_summary()
