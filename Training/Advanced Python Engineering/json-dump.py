import json

# Convert Python objects into JSON objects and save them to a file using the json.dump() method

person = {"fname": "Philip", "lname": "Salem", "age": 48, "city": "Fate", "hasChildren": True, "titles": ["engineer", "cyber security", "cloud security"]}

with open('person.json', 'w') as f:
    json.dump(person, f, indent=4, separators=(";", ":"))