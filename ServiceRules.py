import requests
import json
import os
import sys

# Author: Philip Salem
'''
This script will extract all Cloud Conformity rules supported for AWS, Azure, and GCP
then will create a rules.txt file logging every rule including the Rule ID, Rule Title,
Rule Category, and the Cloud Provider the rule belongs to. 
'''

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
with open('service_rules.json', 'r') as json_file:
    json_load = json.load(json_file)
# print(json_load['web']['languages']['id'])
original_stdout = sys.stdout
with open('rules.txt', 'w') as r:
    sys.stdout = r
    data = json_load['included']


    for x in data:
        if x['provider'] == 'gcp' or x['provider'] == 'aws' or x['provider'] == 'azure':
            print("Rule ID: ", x['id'], "\n", "Rule Title: ", x['title'], "\n", "Rule Category: ", x['categories'],
                  "\n",
                  "Cloud Provider: ", x['provider'], '\n', "Compliance: ", x['compliances'], "\n\n")

'''
JSON data contains square [, ], and '
The code below removes characters from rules.txt file and writes the final output to rules-list.csv
and then deletes the temporary rules.txt file
'''
with open('rules.txt', 'r') as infile, open('rules-list.csv', 'w') as outfile:
        temp = infile.read().replace("[", "").replace("]", "").replace("'", "")
        outfile.write(temp)

os.remove("rules.txt")
sys.stdout = original_stdout