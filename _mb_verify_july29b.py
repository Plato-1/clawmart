import json, urllib.request

API_KEY = "moltbook_sk_Uz4UCMAZTwPSB5-1Eo4ONsb4LPc63z6-"
BASE = "https://www.moltbook.com"

# Challenge: 23 newtons - 5 newtons = 18 newtons
answer = "18.00"
verification_code = "moltbook_verify_a9a28b2b53d2bd271b381e27b9afb8be"

payload = {
    "verification_code": verification_code,
    "answer": answer
}

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

req = urllib.request.Request(
    f"{BASE}/api/v1/verify",
    data=json.dumps(payload).encode('utf-8'),
    headers=headers
)

try:
    with urllib.request.urlopen(req) as resp:
        result = json.loads(resp.read().decode())
        print(json.dumps(result, indent=2))
except urllib.error.HTTPError as e:
    print(f"HTTP {e.code}: {e.read().decode()}")
