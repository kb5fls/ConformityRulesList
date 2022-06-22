import json


# with open("service_rules.json", 'r') as json_file:
#     json_load = json.load(json_file)

# print(json.dumps(json_load, json_file, indent=4))
# print(json.dumps(json_load['data']['included']['id']['name'], indent=4))

# print(json.dumps(json_load['data'], json_file, indent=4))
# print(json_load['included'][2]['name'])

f = open('service_rules.json')

data = json.load(f)

for i in data:
    print(i)

f.close()