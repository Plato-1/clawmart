import json, urllib.request, os

with open(os.path.expanduser("~/.config/moltbook/credentials.json")) as f:
    creds = json.load(f)

payload = {
    "verification_code": "moltbook_verify_8da30cfed76934bab11b1721ccd4eebd",
    "answer": "47.00"
}

req = urllib.request.Request(
    "https://www.moltbook.com/api/v1/verify",
    data=json.dumps(payload).encode("utf-8"),
    headers={
        "Authorization": f"Bearer {creds['api_key']}",
        "Content-Type": "application/json"
    },
    method="POST"
)

try:
    with urllib.request.urlopen(req) as resp:
        print(resp.read().decode())
except urllib.error.HTTPError as e:
    print(f"HTTP {e.code}: {e.read().decode()}")