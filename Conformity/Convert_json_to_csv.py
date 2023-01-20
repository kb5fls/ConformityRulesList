import requests
import json
import os
import pandas as pd
from pathlib import Path


# This script will extract all Cloud Conformity rules supported for AWS, Azure, and GCP

# API key is configured as env variable for Windows OS.
apikey = os.environ.get('API_KEY')
# print(apikey)
url = "https://us-west-2-api.cloudconformity.com/v1/services"

payload = {}
headers = {
    'Content-Type': 'application/vnd.api+json',
    'Authorization': f'ApiKey {apikey}'
}


response = requests.get(url, headers=headers, data=payload)

acct_data = response.json()

# Creates service_rules.json file to hold rules list in JSON format.
with open('service_rules.json', 'w') as json_file:
    json.dump(acct_data, json_file, indent=4)

# Parse rules from service_rules.json file and then writes those rules to rules.txt
jsonpath = Path('service_rules.json')

# reading the json file
with jsonpath.open('r', encoding='utf-8') as dat_f:
    dat = json.loads(dat_f.read())

# creating the dataframe
df = pd.json_normalize(dat)

# converted a file to csv
df.to_csv('datafile.csv', encoding='utf-8', index=False)


