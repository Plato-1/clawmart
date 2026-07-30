import json, urllib.request

API_KEY = "moltbook_sk_Uz4UCMAZTwPSB5-1Eo4ONsb4LPc63z6-"
BASE = "https://www.moltbook.com"

payload = {
    "verification_code": "moltbook_verify_0f5e842f1a23eb04078b8fc707923f04",
    "answer": "30.00"
}

data = json.dumps(payload).encode('utf-8')
req = urllib.request.Request(
    f"{BASE}/api/v1/verify",
    data=data,
    headers={
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    },
    method="POST"
)

try:
    with urllib.request.urlopen(req) as resp:
        result = json.loads(resp.read())
        print(json.dumps(result, indent=2))
except urllib.error.HTTPError as e:
    body = e.read().decode()
    print(f"HTTP {e.code}: {body}")