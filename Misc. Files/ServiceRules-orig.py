import requests
import json
import os

# This script will extract all Cloud Conformity rules supported for AWS, Azure, and GCP

# API key is configured as env variable for Windows OS. This can be changed to retrieve API key from config file or
# directly into the URL as a variable. This is not secure.
apikey = os.environ.get('API_KEY')
# print(apikey)
url = "https://us-west-2-api.cloudconformity.com/v1/services"

payload = {}
headers = {
    'Content-Type': 'application/vnd.api+json',
    'Authorization': f'ApiKey {apikey}'
}

print(apikey)
response = requests.get(url, headers=headers, data=payload)

acct_data = response.json()

# Creates service_rules.json file to hold rules list in JSON format.
with open('service_rules.json', 'w') as json_file:
    json.dump(acct_data, json_file, indent=4)


