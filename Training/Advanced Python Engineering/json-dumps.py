import json

person = {"fname": "Philip", "lname": "Salem", "age": 48, "city": "Fate", "hasChildren": True, "skills": ["Engineer", "Cyber Security", "Cloud Security"]}

# Convert from json
person_json = json.dumps(person)

# Different formatting style
person_json2 = json.dumps(person, indent=4, separators=("; ", ": "), sort_keys=True)

# Print the results of the json strings
print(person_json)

print(person_json2)
