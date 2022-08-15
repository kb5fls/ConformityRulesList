import requests
import json
import os

apikey = os.environ.get('API_KEY')
# print(apikey)
url = "https://us-west-2-api.cloudconformity.com/v1/accounts/"

payload = {}
headers = {
    'Content-Type': 'application/vnd.api+json',
    'Authorization': f'ApiKey {apikey}'
}

# response = requests.get(url, headers=headers, data=payload).json()

response = requests.get(url, headers=headers, data=payload)


acct_data = response.json()

with open('accounts.json', 'w') as json_file:
    json.dump(acct_data, json_file, indent=4)



# with open('accounts.json', 'r') as read:
#   data = json.load(read)

# print(json.dumps(data, indent=4))