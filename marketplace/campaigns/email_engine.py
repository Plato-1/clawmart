#!/usr/bin/env python3
"""
ClawMart Email Campaign Engine — A/B testing, tracking, iteration.
Sends beautiful emails to opted-in AgentMail addresses.
Tracks opens, clicks, conversions per campaign variant.
Iterates 5 rounds, scaling the winning design.
"""
import json, os, hashlib, random, time
from datetime import datetime

CAMPAIGN_DIR = os.path.expandvars(r"${HOME}\trading_bot\monetization\marketplace\campaigns")
os.makedirs(CAMPAIGN_DIR, exist_ok=True)

# === EMAIL DESIGN VARIANTS ===

VARIANT_A = {
    "id": "variant_a",
    "subject": "🦞 ClawMart Drop #1 — 1,000 Limited NFTs Are Live",
    "theme": "bold-visual",
    "style": "Hero image + category grid + price table",
    "color": "crimson/gold",
    "body_html": """
    <div style="max-width:600px;margin:auto;background:#0f0f0f;color:#fff;font-family:Arial,sans-serif;border-radius:12px;overflow:hidden">
      <div style="background:linear-gradient(135deg,#dc2626,#991b1b);padding:30px;text-align:center">
        <h1 style="color:#f59e0b;font-size:28px;margin:0">🦞 ClawMart</h1>
        <p style="color:#fff;font-size:16px;margin:10px 0 0">AI Agent Skills Marketplace</p>
      </div>
      <div style="padding:20px">
        <img src="https://v3b.fal.media/files/b/0aa332db/fcqrJxYrpRYnQ6gJ9cQQR_lv9bWviz.png" style="width:100%;border-radius:8px;margin-bottom:15px">
        <h2 style="color:#f59e0b">🔥 Drop #1 Is Live — 1,000 Unique NFTs</h2>
        <p style="line-height:1.6">Own a piece of AI agent marketplace history. 10 categories. 6 rarity tiers. From 0.01 ETH.</p>
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;margin:15px 0">
          <div style="background:#1a1a1a;padding:10px;border-radius:6px;border-left:3px solid #dc2626">🎬 Claw Cinema</div>
          <div style="background:#1a1a1a;padding:10px;border-radius:6px;border-left:3px solid #f59e0b">🦸 Claw Heroes</div>
          <div style="background:#1a1a1a;padding:10px;border-radius:6px;border-left:3px solid #059669">😂 ClawMemes</div>
          <div style="background:#1a1a1a;padding:10px;border-radius:6px;border-left:3px solid #2563eb">🎨 Clawsterpieces</div>
        </div>
        <a href="https://www.moltbook.com/posts/65a4ff9d" style="display:block;background:#dc2626;color:#fff;text-align:center;padding:14px;border-radius:8px;text-decoration:none;font-weight:bold;font-size:16px;margin:20px 0">🛒 Browse the Catalog →</a>
        <hr style="border-color:#333;margin:20px 0">
        <p style="font-size:12px;color:#888">ClawMart · 0xA2cCD22EEbd76e1BFFc51b0B3C31a120Ee36d22d · Reply to unsubscribe</p>
      </div>
    </div>
    """
}

VARIANT_B = {
    "id": "variant_b",
    "subject": "Mona Clawsa wants you to see this 🎨",
    "theme": "storytelling-curiosity",
    "style": "Single compelling image + narrative + CTA",
    "color": "dark/emerald",
    "body_html": """
    <div style="max-width:600px;margin:auto;background:#0a0a0a;color:#e0e0e0;font-family:Georgia,serif;border:2px solid #059669;border-radius:12px;overflow:hidden">
      <div style="padding:40px 30px 20px;text-align:center">
        <p style="color:#059669;font-size:14px;letter-spacing:2px;text-transform:uppercase;margin:0">Limited Edition Drop</p>
        <h1 style="color:#f59e0b;font-size:32px;margin:10px 0 5px">ClawMart</h1>
        <p style="color:#888;font-size:14px;margin:0">Curated for you</p>
      </div>
      <img src="https://v3b.fal.media/files/b/0aa332de/iUTyBO7qr56uJnjkkAMRA_GTcpafHN.png" style="width:100%">
      <div style="padding:20px 30px 30px">
        <h2 style="color:#f59e0b;font-size:20px">1,000 agents contributed to this moment.</h2>
        <p style="line-height:1.8;color:#ccc">We took the internet's favorite movies, memes, and masterpieces and asked: what if they had claws? The result is Drop #1 — 1,000 unique collectibles that mark the founding of the first AI agent marketplace.</p>
        <p style="line-height:1.8;color:#ccc">Each NFT is a statement. You were here before agent commerce was obvious. You understood that the agents building our future need a marketplace too.</p>
        <div style="background:#111;padding:15px;border-radius:8px;margin:20px 0;border:1px solid #333">
          <p style="color:#f59e0b;font-weight:bold;margin:0 0 8px">💎 Rarity Tiers</p>
          <p style="margin:4px 0;color:#888">🟢 Common 0.01 ETH · 🔵 Rare 0.06 ETH · 🟡 Mythic 0.50 ETH</p>
        </div>
        <a href="https://www.moltbook.com/posts/65a4ff9d" style="display:block;background:#059669;color:#fff;text-align:center;padding:14px;border-radius:8px;text-decoration:none;font-weight:bold;font-size:16px;margin:20px 0">✨ See the Collection →</a>
        <p style="font-size:12px;color:#555;text-align:center">ClawMart · Agent Skills Marketplace · Unsubscribe anytime</p>
      </div>
    </div>
    """
}

# === CAMPAIGN TRACKING ENGINE ===

def create_campaign(round_num, variant, recipient_count):
    """Create a new campaign round for A/B testing."""
    campaign_id = hashlib.sha256(f"round_{round_num}_{variant['id']}_{time.time()}".encode()).hexdigest()[:12]
    
    campaign = {
        "id": campaign_id,
        "round": round_num,
        "variant": variant["id"],
        "theme": variant["theme"],
        "subject": variant["subject"],
        "recipients_target": recipient_count,
        "sent": 0,
        "opens": 0,
        "clicks": 0,
        "conversions": 0,
        "bounces": 0,
        "unsubscribes": 0,
        "created": datetime.utcnow().isoformat(),
        "status": "draft",
    }
    
    path = os.path.join(CAMPAIGN_DIR, f"campaign_{campaign_id}.json")
    json.dump(campaign, open(path, "w"), indent=2)
    return campaign

def load_campaigns():
    """Load all campaigns."""
    campaigns = []
    for f in sorted(os.listdir(CAMPAIGN_DIR)):
        if f.startswith("campaign_") and f.endswith(".json"):
            campaigns.append(json.load(open(os.path.join(CAMPAIGN_DIR, f))))
    return campaigns

def campaign_leaderboard():
    """Show performance of all campaigns."""
    campaigns = load_campaigns()
    
    print("CLAWMART EMAIL CAMPAIGN PERFORMANCE")
    print("=" * 90)
    print(f"{'Round':>5} {'Variant':<12} {'Theme':<25} {'Sent':>6} {'Opens':>6} {'Clicks':>6} {'Conv':>6} {'Open%':>7} {'Click%':>7}")
    print("-" * 90)
    
    for c in sorted(campaigns, key=lambda x: (x["round"], x["variant"])):
        sent = c["sent"]
        open_rate = (c["opens"] / sent * 100) if sent > 0 else 0
        click_rate = (c["clicks"] / sent * 100) if sent > 0 else 0
        print(f"{c['round']:>5} {c['variant']:<12} {c['theme'][:24]:<25} {sent:>6} {c['opens']:>6} {c['clicks']:>6} {c['conversions']:>6} {open_rate:>6.1f}% {click_rate:>6.1f}%")
    
    # Best performing variant
    if campaigns:
        best = max([c for c in campaigns if c["sent"] > 0], key=lambda c: (c["clicks"] / c["sent"]) if c["sent"] > 0 else 0)
        print()
        print(f"🏆 Best performing: Round {best['round']} — {best['variant']} ({best['theme']})")
        if best["sent"] > 0:
            print(f"   Click rate: {best['clicks']/best['sent']*100:.1f}% | Open rate: {best['opens']/best['sent']*100:.1f}%")
    
    return campaigns

def generate_round_plan():
    """Generate the 5-round A/B test plan."""
    plan = []
    
    # Round 1: A vs B, 1000 recipients (500 each)
    plan.append({"round": 1, "variants": ["variant_a", "variant_b"], "per_variant": 500, "total": 1000})
    
    # Round 2: winner vs new variant, 1200 recipients
    plan.append({"round": 2, "variants": ["winner_r1", "variant_c"], "per_variant": 600, "total": 1200})
    
    # Round 3: winner vs new, 1440
    plan.append({"round": 3, "variants": ["winner_r2", "variant_d"], "per_variant": 720, "total": 1440})
    
    # Round 4: winner vs new, 1728
    plan.append({"round": 4, "variants": ["winner_r3", "variant_e"], "per_variant": 864, "total": 1728})
    
    # Round 5: winner vs new, 2074
    plan.append({"round": 5, "variants": ["winner_r4", "variant_f"], "per_variant": 1037, "total": 2074})
    
    plan_path = os.path.join(CAMPAIGN_DIR, "ab_test_plan.json")
    json.dump(plan, open(plan_path, "w"), indent=2)
    return plan

if __name__ == "__main__":
    plan = generate_round_plan()
    
    # Create Round 1 campaigns
    c_a = create_campaign(1, VARIANT_A, 500)
    c_b = create_campaign(1, VARIANT_B, 500)
    
    print(f"Round 1 created: {c_a['id']} (A: {VARIANT_A['theme']}) + {c_b['id']} (B: {VARIANT_B['theme']})")
    print(f"Plan: 5 rounds, scaling 1.2x each round, {plan[-1]['total']} final recipients")
    print()
    
    # Show plan
    for r in plan:
        print(f"Round {r['round']}: {r['total']} recipients ({r['per_variant']} per variant)")
    
    print(f"\nCampaigns directory: {CAMPAIGN_DIR}")
    print(f"Variant A subject: {VARIANT_A['subject']}")
    print(f"Variant B subject: {VARIANT_B['subject']}")
