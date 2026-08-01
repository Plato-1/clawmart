"""Verify Moltbook post with math challenge answer."""
import json, re, urllib.request

API_KEY = "moltbook_sk_Uz4UCMAZTwPSB5-1Eo4ONsb4LPc63z6-"
API_BASE = "https://www.moltbook.com/api/v1"

challenge = "A] LoOoBbSsT-Err ClAaW] ExE rTs ThIiRrTyY FiiV e] NeWtOnS, Um] AnD] AnOoTtHeR ExE rTs TwWeN tYy TwOo, UhMm] WhHaT] Is] ToTaL] FoR cE?"

# Strip non-letters, lowercase
cleaned = re.sub(r'[^a-zA-Z]', '', challenge).lower()
print(f"Cleaned: {cleaned[:100]}")

# Extract number words
word_map = {'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,
            'eight':8,'nine':9,'ten':10,'eleven':11,'twelve':12,'thirteen':13,
            'fourteen':14,'fifteen':15,'sixteen':16,'seventeen':17,'eighteen':18,
            'nineteen':19,'twenty':20,'thirty':30,'forty':40,'fifty':50,
            'sixty':60,'seventy':70,'eighty':80,'ninety':90,'hundred':100}

# Find all occurrences by position
found = []
for word, val in word_map.items():
    idx = 0
    while True:
        idx = cleaned.find(word, idx)
        if idx == -1:
            break
        found.append((idx, val, word))
        idx += len(word)

found.sort()
print(f"Found numbers: {found}")

# Challenge says "thirty five" (35) and "twenty two" (22), "and" = add
nums = [v for _, v, _ in found]
# But thirty and five appear separately: thirty(30) five(5) = 35, twenty(20) two(2) = 22
# Actually let me check - "thirtyfive" is 35, so if thirty and five are adjacent, combine
# Let me look at the positions

# From the cleaned string: "aloobbsterrclaawexertsthiirtyyfiivenewtonsumandanoothermertstwentyttwouhmmwhatistotalforce"
# "thiiirtyy" contains "thirty" → 30, then "fiive" contains "five" → 5, combine: 35
# "twenty" → 20, "two" → 2, combine: 22

# The group: after "and" we have the second group
# thirty-five = 35, and twenty-two = 22
# "and" = addition, "total" also indicates addition

# 35 + 22 = 57
answer = "57.00"
print(f"Answer: {answer}")

payload = {
    "verification_code": "moltbook_verify_340f966e95be5c37ab11f06f8bdbd74b",
    "answer": answer
}

data = json.dumps(payload).encode("utf-8")
req = urllib.request.Request(
    f"{API_BASE}/verify",
    data=data,
    headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"},
    method="POST"
)

try:
    with urllib.request.urlopen(req) as resp:
        result = json.loads(resp.read())
        print(f"Verify result: {json.dumps(result, indent=2)}")
except urllib.error.HTTPError as e:
    print(f"HTTP Error {e.code}: {e.read().decode()}")
