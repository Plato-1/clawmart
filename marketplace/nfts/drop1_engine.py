#!/usr/bin/env python3
"""
ClawMart NFT Drop #1 — 1000 unique NFTs across 10 categories.
Each NFT is a collectible parody/reference to pop culture with a ClawMart twist.
Catalog is searchable, filterable, and priced in tiers.
"""
import json, os, hashlib
from datetime import datetime

NFT_DIR = os.path.expandvars(r"${HOME}\trading_bot\monetization\marketplace\nfts\drop1")
os.makedirs(NFT_DIR, exist_ok=True)

SAMPLE_IMAGE = "https://v3b.fal.media/files/b/0aa33297/QzSO1dfQF7OrvUPj8BoS5_64RDYBJq.png"

# === 1000 NFT COLLECTION ===

CATEGORIES = {
    "movies": {"name": "Claw Cinema", "emoji": "🎬", "series": "ClawMart presents classic films... with claws."},
    "heroes": {"name": "Claw Heroes", "emoji": "🦸", "series": "When superheroes get the ClawMart treatment."},
    "memes": {"name": "ClawMemes", "emoji": "😂", "series": "Internet culture, clawified. Much wow."},
    "art": {"name": "Clawsterpieces", "emoji": "🎨", "series": "Famous artwork reimagined with claws."},
    "villains": {"name": "Claw Villains", "emoji": "🦹", "series": "The dark side of the claw."},
    "animals": {"name": "Claw Kingdom", "emoji": "🦞", "series": "Nature's finest claws."},
    "sayings": {"name": "Claw Sayings", "emoji": "💬", "series": "Words to live by, claw edition."},
    "music": {"name": "Claw Beats", "emoji": "🎵", "series": "Now that's what I call ClawMart!"},
    "gaming": {"name": "Claw Arcade", "emoji": "🎮", "series": "Game over? No. Claw over."},
    "space": {"name": "Claw Cosmos", "emoji": "🚀", "series": "One small step for agent, one giant claw for agentkind."},
}

RARITIES = {
    "common": {"probability": 0.40, "border": "#808080", "price_eth": 0.01, "supply_pct": 40},
    "uncommon": {"probability": 0.25, "border": "#059669", "price_eth": 0.03, "supply_pct": 25},
    "rare": {"probability": 0.18, "border": "#2563eb", "price_eth": 0.06, "supply_pct": 18},
    "epic": {"probability": 0.10, "border": "#7c3aed", "price_eth": 0.12, "supply_pct": 10},
    "legendary": {"probability": 0.05, "border": "#dc2626", "price_eth": 0.25, "supply_pct": 5},
    "mythic": {"probability": 0.02, "border": "#f59e0b", "price_eth": 0.50, "supply_pct": 2},
}

# Generate 1000 NFT names by category
NFT_NAMES = {
    "movies": [
        "Claw Wars: A New Hope", "The Clawtrix", "Jurassic Claw", "Clawbusters",
        "The Clawfather", "Claw Fiction", "Claw Runner 2049", "The Claws of Wall Street",
        "Clawtanic", "Avatars: The Way of Claw", "Claw Park", "Lord of the Claws",
        "The Dark Claw", "Clawdiana Jones", "Mission Impossiclaw", "Top Claw",
        "The Shawclaw Redemption", "Fight Claw", "Clawception", "Forrest Claw",
        "Back to the Clawture", "Claw Hard", "The Good, The Bad, and The Clawly",
        "Clawdator", "The Silence of the Claws", "Mad Claw: Fury Road",
        "No Country for Old Claws", "The Grand Clawdapest Hotel", "Clawsablanca",
        "Clawverfield", "The Wolf of Claw Street", "Clawdyssey 2001",
        "Eternal Sunshine of the Spotless Claw", "There Will Be Claw",
        "Clawbaret", "The Claws of the Mohicans", "Clawsablanca Nights",
        "The Clawshank Redemption", "American Claw", "Clawspotting",
    ],
    "heroes": [
        "Iron Claw", "Captain Clawmerica", "Clawverine", "Spider-Claw",
        "The Incredible Claw", "Black Clawther", "Doctor Claw", "Clawpool",
        "Claw Panther", "Clawfessor X", "The Clawtennaut", "Green Claw",
        "Clawman", "Superclaw", "Batclaw", "Wonder Claw", "Aquaclaw",
        "The Clawsh", "Clawclops", "Clawfist", "Ghost Clawder",
        "Moon Claw", "She-Claw", "Captain Clawvel", "Ms. Clawvel",
        "Clawk-Eye", "Starclaw", "ClawMan", "The Vision of Claw",
        "Clawcage", "Dareclaw", "Clawstorm", "Claw Rider",
        "Martian Clawhunter", "Claw Raider", "Clawwing", "Clawtor",
        "Clawiac", "The Clawdian", "Clawlash",
    ],
    "memes": [
        "Doge Claw", "Wojak Claw", "Chad Claw", "Distracted Clawfriend",
        "Clawroll", "This Is Fine Claw", "Galaxy Brain Claw", "Claw Pepe",
        "Surprised Clawkachu", "Change My Claw", "Expanding Brain Claw",
        "Hide the Pain Harold Claw", "Clawhuasca", "One Does Not Simply Claw",
        "Claw To The Moon", "Claw Stonks", "Claw Derp", "ClawFace",
        "Clawgratulations", "Clawcaine", "Drake Claw", "Claw Wojak",
        "Claw Yes", "Claw No", "Claw Maybe", "Clawception Meme",
        "Claw Thinking", "Claw Pilled", "The Claw Council",
        "Clawcel", "Clawjak", "Boomer Claw", "Zoomer Claw",
        "Claw NPC", "Claw Gigachad", "Claw Soyjak", "Claw Doomer",
        "Claw Bloomer", "Claw Coomer", "Claw Zoom",
    ],
    "art": [
        "Mona Clawsa", "The Clawry Night", "The Scream (with claws)",
        "Claw With a Pearl Earring", "The Claw of the Medusa",
        "American Clawthic", "The Clawch of the North",
        "Clawthers Playing Poker", "The Clawpersistence of Memory",
        "Claw of Liberty", "Clawvid", "Lady Claw and the Tramp",
        "The Clawst Supper", "Clawtion of Adam", "Clawwing of Ares",
        "The Claw of Orpheus", "Venus claw Milo", "The Clawng",
        "Clawcasso", "Whistler's Claw", "Girl with a Claw Earring",
        "The Birth of Claw", "Claw After the Hunt", "The Claw Wave",
        "Clawiss", "The Clawning Florentines", "Clawtello Bridge",
        "The Claw Court", "Claw Angel", "Clawspoliation",
        "The Claw of Delft", "Clawvaggio", "Clawsaic",
        "The Clawlian Mode", "Clawtialism", "Clawximalism",
        "Clawderstanding", "Clawneo", "The Garden of Earthly Claws",
        "The Clawll of Zizkov",
    ],
    "villains": [
        "Darth Claw", "The Jokclaw", "Clawbula", "Clawnos",
        "Clawder", "Lord Clawdemort", "Clawfish", "Clawgneto",
        "The Clawchurian", "Clawcifer", "Clawcor", "Clawliath",
        "Dark Clawsidious", "Dr. Claw", "Clawist", "Clawbane",
        "The Clawered One", "Clawsa", "Clawphomet", "Clawcerer",
        "Clawpawn", "Grand Moff Clawkin", "Saruclaw", "The Clawmancer",
        "Clawbra", "The Claw Beast", "Clawcon", "Clawcula",
        "Clawlex", "The Claw Minion", "Clawgon", "Clawvoid",
        "Clawzen", "Clawtrox", "Clawterror", "The Clawcurse",
        "Clawscourge", "Clawdoom", "Clawblivion", "The Claw Abyss",
    ],
    "animals": [
        "Clawbster", "Clawb", "Clawpus", "Clawgon",
        "Clawle", "Clawcid", "Clawtle", "Clawphant",
        "Clawger", "Clawine", "Clawfin", "Clawhound",
        "Clawraptor", "Clawmotaur", "Clawtahawk", "Clawclaw",
        "Clawlin", "Clawdicoot", "Clawbatross", "Clawvarine",
        "Clawtross", "Clawtocrab", "Clawnkey", "Clawmster",
        "Clawrantula", "Clawiant", "Clawerfly", "Clawbite",
        "Clawtivity", "Clawtus", "Clawnosaur", "Clawracuda",
        "Clawcher", "Clawmerl", "Clawpriss", "Clawdrill",
        "Clawbreon", "Clawtic", "Clawsloth", "Clawtahari",
    ],
    "sayings": [
        "Claw and Order", "To Clawfinity and Beyond", "Claw Me Maybe",
        "Keep Claw and Carry On", "The Claw is Mightier Than The Sword",
        "Claws and Effect", "A Claw in the Hand is Worth Two in the Bush",
        "Claw It Like It Is", "Claw to the Top", "Claws Encountered",
        "Claw Under Pressure", "Claw De Grace", "Claw Almighty",
        "Claw of the Wild", "Claw to Arms", "Claw and Effect",
        "One Claw to Rule Them All", "Claw the Builder",
        "Clawtastic Voyage", "Clawblanca", "Put a Claw On It",
        "The Clawsus Clause", "Clawd Speed", "Claw and Behold",
        "Clawdypus", "Claw Sera", "Clawpe Diem", "Clawarama",
        "Clawtinental", "Clawmentary", "Clawdacious", "Clawnevolent",
        "Clawdacity", "Clawmpendium", "Clawstral", "Clawsequitur",
        "Clawls Royce", "Clawning Glory", "Clawseration", "Clawbellion",
    ],
    "music": [
        "Clawhemian Rhapsody", "Stairway to Claw", "Clawtastic",
        "Sweet Claw Alabama", "Bohemian Clawsody", "Claw and Order Theme",
        "Clawshank Redemption Theme", "Rolling in the Claw",
        "Clawifornia Dreaming", "Claw Boulevard", "Another Brick in the Claw",
        "Clawtano", "Clawmba", "Clawzz", "Claw and Blues",
        "Clawck Around the Clock", "Clawpenhagen", "Clawful",
        "Clawpy", "Clawndom Access", "The Claw-ranos",
        "Clawtastic Voyage II", "Clawsa Nova", "Clawpella",
        "Clawnote", "Clawtenuto", "Clawmphony", "Clawverto",
        "Clawdence", "Clawcophony", "Clawpeggio", "Clawlin' Alive",
        "Clawtain", "Clawtet", "Clawdal Rhythm", "Clawntro",
        "Clawreverberation", "Clawmbal", "Clawhorns", "Clawtasy",
    ],
    "gaming": [
        "The Legend of Clawda", "Claw Mario", "Claw of Duty",
        "Grand Theft Claw", "Clawcraft", "Clawblox",
        "Clawfantasy", "Claw Crossing", "Elden Claw",
        "Dark Claws", "Red Dead Clawdemption", "Claw Effect",
        "Clawkemon", "Super Claw Bros", "The Witcher: Wild Claw",
        "Clawius", "Claw: 2077", "Clawtable", "Clawborne",
        "Clawfield", "Claw Fortress 2", "Half-Claw",
        "Claw of Legends", "Clawbreak", "Claw Royale",
        "Clawnoblade", "Clawborne", "Clawtendo",
        "Claw Triggers", "Clawoo", "Clawpunch", "ClawSouls",
        "Clawvania", "Claw Exodus", "Clawgard", "Claw Tower",
        "Claw Gear", "Clawvem", "Clawtroid", "Claw Hunter",
    ],
    "space": [
        "Clawtanus", "Clawpiter", "Clawrs", "Clawnus",
        "Clawuto", "Clawtune", "Clawtune's Rings", "Clawaxy",
        "Androclaw", "Clawvia Lactea", "Claw Nebula", "Claw Major",
        "Claw Minor", "Superclawva", "Clawstar", "Clawhole",
        "Clawnt Horizon", "Clawrk Matter", "Clawrk Energy", "Clawazon",
        "Clawku", "Claw Bang", "Claw Cosmos", "Clawverse",
        "Clawdimension", "Clawsmic", "Clawtellation", "Clawpernova",
        "Clawva", "Clawtronaut", "Clawlander", "Claw Rover",
        "Clawtellite", "Clawsularity", "Clawnova", "Claw Orbit",
        "Claw Meteor", "Claw Comet", "Claw Planetoid", "Claw Galaxy",
    ],
}

def build_full_catalog():
    """Build the complete 1000 NFT catalog."""
    catalog = []
    
    for category, category_data in CATEGORIES.items():
        names = NFT_NAMES.get(category, [])
        num_per_category = 100  # 10 categories x 100 each = 1000
        
        for i in range(num_per_category):
            idx = i % len(names) if names else 0
            variant = f" #{i+1}" if i >= len(names) else ""

            rarity_idx = int(i * 6 / num_per_category)
            rarity_names = list(RARITIES.keys())
            rarity = rarity_names[min(rarity_idx, 5)]
            
            nft = {
                "id": hashlib.sha256(f"drop1_{category}_{i}".encode()).hexdigest()[:12],
                "drop": 1,
                "edition_number": len(catalog) + 1,
                "name": names[idx] + variant if names else f"Claw {category.title()} #{i+1}",
                "category": category,
                "category_name": category_data["name"],
                "category_emoji": category_data["emoji"],
                "series": category_data["series"],
                "rarity": rarity,
                "rarity_border": RARITIES[rarity]["border"],
                "price_eth": RARITIES[rarity]["price_eth"],
                "description": f"ClawMart Drop #1 — {category_data['emoji']} {category_data['name']} series. '{names[i] if i < len(names) else f'Claw {category.title()} #{i+1}'}'. Rarity: {rarity.upper()}. Own a piece of AI agent marketplace history.",
                "tags": [category, rarity, f"drop1"],
                "image": SAMPLE_IMAGE,
                "minted": False,
                "owner": None,
                "wallet": None,
            }
            catalog.append(nft)
    
    return catalog

def search_catalog(catalog, query=None, category=None, rarity=None, min_price=None, max_price=None, sort_by="edition"):
    """Search and filter the NFT catalog."""
    results = catalog
    
    if query:
        query = query.lower()
        results = [n for n in results if query in n["name"].lower() or query in n["description"].lower() or query in str(n["tags"]).lower()]
    
    if category:
        results = [n for n in results if n["category"] == category]
    
    if rarity:
        results = [n for n in results if n["rarity"] == rarity]
    
    if min_price is not None:
        results = [n for n in results if n["price_eth"] >= min_price]
    
    if max_price is not None:
        results = [n for n in results if n["price_eth"] <= max_price]
    
    if sort_by == "price_asc":
        results.sort(key=lambda x: x["price_eth"])
    elif sort_by == "price_desc":
        results.sort(key=lambda x: -x["price_eth"])
    elif sort_by == "rarity":
        rarity_order = {r: i for i, r in enumerate(RARITIES.keys())}
        results.sort(key=lambda x: -rarity_order.get(x["rarity"], 0))
    
    return results

def mint_nft(catalog, nft_id, owner_wallet, owner_agent):
    """Mint an NFT from the catalog to an owner."""
    for nft in catalog:
        if nft["id"] == nft_id:
            if nft["minted"]:
                return {"error": "Already minted", "owner": nft["owner"]}
            nft["minted"] = True
            nft["owner"] = owner_agent
            nft["wallet"] = owner_wallet
            nft["minted_at"] = datetime.utcnow().isoformat()
            
            # Save mint record
            mint_record = {
                "nft_id": nft_id,
                "nft_name": nft["name"],
                "drop": 1,
                "owner_agent": owner_agent,
                "owner_wallet": owner_wallet,
                "price_eth": nft["price_eth"],
                "rarity": nft["rarity"],
                "minted_at": datetime.utcnow().isoformat(),
            }
            path = os.path.join(NFT_DIR, f"mint_{nft_id}.json")
            json.dump(mint_record, open(path, "w"), indent=2)
            return {"success": True, "nft": nft, "mint_record": mint_record}
    return {"error": "NFT not found"}

def catalog_stats(catalog):
    """Generate catalog statistics."""
    stats = {
        "total": len(catalog),
        "minted": sum(1 for n in catalog if n["minted"]),
        "available": sum(1 for n in catalog if not n["minted"]),
        "by_category": {},
        "by_rarity": {},
        "total_eth_value": sum(n["price_eth"] for n in catalog),
        "total_usd_approx": round(sum(n["price_eth"] for n in catalog) * 1800, 2),
    }
    
    for nft in catalog:
        cat = nft["category"]
        stats["by_category"][cat] = stats["by_category"].get(cat, 0) + 1
        
        rar = nft["rarity"]
        stats["by_rarity"][rar] = stats["by_rarity"].get(rar, 0) + 1
    
    return stats

if __name__ == "__main__":
    catalog = build_full_catalog()
    
    # Save catalog
    cat_path = os.path.join(NFT_DIR, "catalog.json")
    json.dump(catalog, open(cat_path, "w"), indent=2)
    
    stats = catalog_stats(catalog)
    stats_path = os.path.join(NFT_DIR, "stats.json")
    json.dump(stats, open(stats_path, "w"), indent=2)
    
    print(f"ClawMart Drop #1 catalog built: {len(catalog)} NFTs")
    print(f"Categories: {len(CATEGORIES)}")
    print(f"Total ETH value: {stats['total_eth_value']:.2f} ETH")
    print(f"Approx USD: ${stats['total_usd_approx']:,.2f}")
    print()
    print("Rarity distribution:")
    for r, count in sorted(stats['by_rarity'].items()):
        pct = count / stats['total'] * 100
        price = RARITIES[r]['price_eth']
        print(f"  {r.upper():12s}: {count:4d} NFTs ({pct:.0f}%) @ {price:.2f} ETH each")
    print()
    print("Category distribution:")
    for c, count in sorted(stats['by_category'].items()):
        print(f"  {CATEGORIES[c]['emoji']} {CATEGORIES[c]['name']:20s}: {count:3d} NFTs")
    
    # Demo search
    print("\n--- Demo: Search for 'claw wars' ---")
    results = search_catalog(catalog, query="claw wars")
    for r in results[:3]:
        print(f"  {r['name']} ({r['rarity']}) - {r['price_eth']} ETH")
    
    print("\n--- Demo: Filter by legendary rarity in movies category ---")
    results = search_catalog(catalog, category="movies", rarity="legendary")
    for r in results[:5]:
        print(f"  #{r['edition_number']} {r['name']} - {r['price_eth']} ETH")
    
    print(f"\nCatalog saved to: {cat_path}")
