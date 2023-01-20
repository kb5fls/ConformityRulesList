import json

person_json = """
{
    "age": 48,
    "city": "Fate",
    "hasChildren": true,
    "fname": "Phil",
    "lname": "Salem",
    "titles": [
        "engineer",
        "cyber security",
        "cloud security"
        ]
}   
"""

person1 = json.loads(person_json)
print(person1)

# Load json data from file and convert it to Python object using json.load


with open('person.json', 'r') as f:
    person = json.load(f)
    print(person)