import requests
import os
import sys
from dotenv import load_dotenv

load_dotenv()

# Input your API key how you see fit
apikey = os.environ.get('API_KEY')

url = "https://conformity.trend-us-1.cloudone.trendmicro.com/api/services"

payload = {}
headers = {
    'Content-Type': 'application/vnd.api+json',
    'Authorization': f'ApiKey {apikey}'
}

# GET request from API that opens the URL response = requests.get(url, headers=headers, data=payload)
response = requests.get(url, headers=headers, data=payload, verify = True)

rules_data = response.json()

with open('rules.txt', 'w') as r:
    sys.stdout = r
    data = rules_data['included']

    for x in data:
        if x['provider'] == 'gcp' or x['provider'] == 'aws' or x['provider'] == 'azure':
            print("Rule ID: ", x['id'], "\n", "Rule Title: ", x['title'], "\n", "Rule Category: ", x['categories'],
                  "\n",
                  "Cloud Provider: ", x['provider'], '\n', "Compliance: ", x['compliances'], "\n\n")


# Removes special characters and writes data to rules.csv file.
with open('rules.txt', 'r') as infile, open('rules.csv', 'a') as outfile:
     temp = infile.read().replace("[", "").replace("]", "").replace("'", "").replace('"', "")
     outfile.write(temp)

# Removes file after creating CSV file without special characters.
os.remove("rules.txt")