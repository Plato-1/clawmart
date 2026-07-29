import json, urllib.request

API_KEY = "moltbook_sk_Uz4UCMAZTwPSB5-1Eo4ONsb4LPc63z6-"
BASE = "https://www.moltbook.com"

# Challenge: lobster swims at 23 m/s, fight reduces by 7 = 16.00
payload = {
    "verification_code": "moltbook_verify_20b67ac0e9000c4cc58cbc47eaa385b0",
    "answer": "16.00"
}

req = urllib.request.Request(
    f"{BASE}/api/v1/verify",
    data=json.dumps(payload).encode('utf-8'),
    headers={
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    },
    method='POST'
)

try:
    resp = urllib.request.urlopen(req)
    result = json.loads(resp.read().decode())
    print(json.dumps(result, indent=2))
except urllib.error.HTTPError as e:
    print(f"HTTP Error {e.code}: {e.read().decode()}")
