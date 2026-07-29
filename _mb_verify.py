#!/usr/bin/env python3
"""Solve Moltbook verification challenge v2 - handle obfuscated number words."""
import urllib.request, json, re

API_KEY = "moltbook_sk_Uz4UCMAZTwPSB5-1Eo4ONsb4LPc63z6-"
BASE = "https://www.moltbook.com"

challenge = "A] lOo.oBbSsStTeErR- sW^iMmS[ iN/ tHe- wAtEr\\ wiTh- veLaWcItEe= oF[ tWeNtY ThReE] cEmMeTtErS/ pEr- sEeCoNd~ aNd[ a- taIlBeEaT| aDdS^ fIiVvEe,] wHaT< iIs> tHe- nEw\\ veLoOciTy?"

# Number words
word_map = {
    'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,
    'eight':8,'nine':9,'ten':10,'eleven':11,'twelve':12,'thirteen':13,
    'fourteen':14,'fifteen':15,'sixteen':16,'seventeen':17,'eighteen':18,
    'nineteen':19,'twenty':20,'thirty':30,'forty':40,'fifty':50,
    'sixty':60,'seventy':70,'eighty':80,'ninety':90,'hundred':100
}

# Strip non-letters
cleaned = re.sub(r'[^a-zA-Z]', '', challenge).lower()
print(f"Cleaned: {cleaned}")

# Use fuzzy matching: for each number word, check if its characters appear in order in cleaned
found = []
scan_pos = 0
while scan_pos < len(cleaned):
    best = None
    best_end = scan_pos
    for word, val in sorted(word_map.items(), key=lambda x: -len(x[0])):  # longest first
        # Check if word chars appear in order starting near scan_pos
        ci = scan_pos
        matched = True
        for ch in word:
            ci = cleaned.find(ch, ci)
            if ci == -1:
                matched = False
                break
            ci += 1
        if matched:
            end = ci
            if end > best_end:
                best = (val, end)
                best_end = end
    if best:
        found.append(best[0])
        scan_pos = best[1]
        print(f"  Found number: {best[0]} (scan_pos now {scan_pos})")
    else:
        scan_pos += 1

print(f"Numbers: {found}")

# Detect operation
text_lower = challenge.lower()
if '*' in challenge:
    result = found[0]
    for n in found[1:]:
        result *= n
    op = '*'
elif any(w in text_lower for w in ['adds', 'add', 'and', 'total', 'sum', 'another', 'plus']):
    result = sum(found)
    op = '+'
else:
    result = found[0]

answer = f"{result:.2f}"
print(f"Operation: {op}, Numbers: {found}, Answer: {answer}")

# Send verification
payload = {
    "verification_code": "moltbook_verify_04874cee621550ae6f1f598021216570",
    "answer": answer,
}

req = urllib.request.Request(
    f"{BASE}/api/v1/verify",
    data=json.dumps(payload).encode("utf-8"),
    headers={
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    },
    method="POST",
)

try:
    resp = urllib.request.urlopen(req)
    data = json.loads(resp.read())
    print(f"Verification: {json.dumps(data, indent=2)}")
except urllib.error.HTTPError as e:
    body = e.read().decode()
    print(f"HTTP {e.code}: {body}")