import json, os
with open('C:/Users/Arthur Motch/.config/moltbook/credentials.json') as f:
    creds = json.load(f)
print(creds['api_key'])
