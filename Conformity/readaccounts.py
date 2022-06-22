import json


with open('accounts.json', 'r') as handle:
    parsed = json.dumps(handle)

print(handle)