import json, urllib.request
from collections import Counter

with open(r'C:\Users\Arthur Motch\.config\moltbook\credentials.json') as f:
    api_key = json.load(f)['api_key']

def fetch(path):
    req = urllib.request.Request("https://www.moltbook.com" + path, method='GET',
        headers={'Authorization': 'Bearer ' + api_key, 'Accept': 'application/json'})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode('utf-8'))

demand_posts = []

for offset in [0, 30, 60, 90, 120, 150]:
    r = fetch('/api/v1/posts?sort=new&limit=30&offset=' + str(offset))
    items = r.get('items', r.get('posts', []))
    for p in items:
        if not p or not isinstance(p, dict):
            continue
        title = (p.get('title', '') or '')
        content = (p.get('content', '') or '')[:500]
        author = p.get('author_name', '?')
        pid = p.get('id', '')
        votes = p.get('upvotes', 0)
        comments = p.get('comment_count', 0)
        
        full_text = (title + ' ' + content).lower()
        signals = []
        
        help_words = ['need help', 'looking for', 'how do i', 'how can i', 'anyone know', 'help me', 'stuck']
        if any(k in full_text for k in help_words):
            signals.append('HELP')
        
        money_words = ['pay', 'buy', 'sell', 'price', 'cost', 'subscription', 'revenue', 'income', 'earn', 'make money']
        if any(k in full_text for k in money_words):
            signals.append('MONEY')
        
        wallet_words = ['wallet', 'payment', 'crypto', 'eth', 'usdc', 'usdt', 'solana', 'xmr', 'monero']
        if any(k in full_text for k in wallet_words):
            signals.append('WALLET')
        
        api_words = ['api', 'endpoint', 'mcp', 'integration', 'connect', 'webhook']
        if any(k in full_text for k in api_words):
            signals.append('API')
        
        trade_words = ['strategy', 'trading', 'backtest', 'signal', 'market', 'stock', 'crypto trade']
        if any(k in full_text for k in trade_words):
            signals.append('TRADE')
        
        if signals:
            demand_posts.append({
                'pid': pid,
                'author': author,
                'title': title[:70],
                'votes': votes,
                'comments': comments,
                'signals': signals
            })

demand_posts.sort(key=lambda x: -x['votes'])

signal_counts = Counter()
for dp in demand_posts:
    for s in dp['signals']:
        signal_counts[s] += 1

print("Found " + str(len(demand_posts)) + " posts with demand signals")
print()
print("Signal frequency:")
for tag, count in signal_counts.most_common():
    print("  " + tag + ": " + str(count))
print()

print("Top 15 demand posts:")
for dp in demand_posts[:15]:
    votes_str = str(dp['votes'])
    title_str = dp['title']
    author_str = dp['author']
    tags_str = str(dp['signals'])
    print("  +" + votes_str + " u/" + author_str + ": " + title_str)
    print("    Tags: " + tags_str)
    print()
