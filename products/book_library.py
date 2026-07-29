#!/usr/bin/env python3
"""Trading Book Summary Library — subscription delivery."""
import json, os, glob

BOOK_DIR = os.path.expandvars(r"${HOME}\trading_bot")
OUT_DIR = os.path.expandvars(r"${HOME}\trading_bot\monetization\products\book_summaries")
os.makedirs(OUT_DIR, exist_ok=True)

# Map of book files to human-readable titles
BOOKS = {
    "market_wizards_2012.txt": "Market Wizards (Schwager, 2012)",
    "reminiscences_stock_operator_2005.txt": "Reminiscences of a Stock Operator (Lefevre, 2005)",
    "flash_boys_2015.txt": "Flash Boys (Lewis, 2015)",
    "dual_momentum_2015.txt": "Dual Momentum (Antonacci, 2015)",
    "evidence_based_technical_analysis_2007.txt": "Evidence-Based Technical Analysis (Aronson, 2007)",
    "technical_analysis_financial_markets_1999.txt": "Technical Analysis of Financial Markets (Murphy, 1999)",
    "option_volatility_pricing_1994.txt": "Option Volatility & Pricing (Natenberg, 1994)",
    "long_term_secrets_short_term_trading_1999.txt": "Long-Term Secrets to Short-Term Trading (Williams, 1999)",
    "come_into_my_trading_room_2002.txt": "Come Into My Trading Room (Elder, 2002)",
    "jesse_livermore_worlds_greatest_2001.txt": "Jesse Livermore: World's Greatest Stock Trader (Smitten, 2001)",
    "stock_market_wizards_2001.txt": "Stock Market Wizards (Schwager, 2001)",
    "mastering_trade_2006.txt": "Mastering the Trade (Carter, 2006)",
    "intermarket_trading_strategies_2009.txt": "Intermarket Trading Strategies (Murphy, 2009)",
    "principles_life_work_2017.txt": "Principles: Life and Work (Dalio, 2017)",
    "millionaire_traders_2007.txt": "Millionaire Traders (Lien/Schlossberg, 2007)",
}

def list_books():
    available = []
    for fname, title in BOOKS.items():
        path = os.path.join(BOOK_DIR, fname)
        if os.path.exists(path):
            size = os.path.getsize(path)
            available.append({"title": title, "file": fname, "size_bytes": size})
    return available

def catalog():
    books = list_books()
    catalog = {
        "service": "Trading Book Summary Library",
        "total_books": len(books),
        "available_books": books,
        "subscription_monthly_usd": 8,
        "subscription_annual_usd": 69,
        "note": "Summaries are generated fresh on demand. Each summary includes key frameworks, actionable rules, and strategy blueprints."
    }
    path = os.path.join(OUT_DIR, "catalog.json")
    json.dump(catalog, open(path, "w"), indent=2)
    print(f"Catalog: {len(books)} books indexed")
    return catalog

if __name__ == "__main__":
    catalog()
    books = list_books()
    print(f"Catalog saved. {len(books)} books available.")
    for b in books[:5]:
        print(f"  {b['title']} ({b['size_bytes']:,} bytes)")
