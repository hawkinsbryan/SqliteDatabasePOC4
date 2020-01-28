import json

insertIntoJobsList = '''
{
    "people": [
    {
        "name": "John Smith",
        "phone": "615-555-7164",
        "emails": null,
        "has_license": true
        },
        {
        "name": "Jane Doe",
        "phone": "560-555-5153",
        "emails": null,
        "has_license": true
        }
        ]
        }
'''

data = json.loads(insertIntoJobsList)
print(type(data))
print(data)

for person in data['people']:
    print(person)
    print(person['name'])
