import sqlite3 as lit
insertIntoJobsList = (
    # END COMMA triggers auto increment because primary key integer is not specified
[
    ("""{
        "name": "Dan Smith",
        "work": "Chef",
        "email": "dan.smith@chef.org",
        "dob": "21/10/1925",
        "address": "1234 Bird Street",
        "city": "New York",
        }""",),
    ("""{
        "name": "Paul Bunyan",
        "work": "Lumberjack",
        "email": "paul.bunyan@lumber.org",
        "dob": "11/03/1920",
        "address": "44 Apple Ave",
        "city": "Denver",
        }""", ),
    ("""{
        "name": "Troy Aikman",
        "work": "Quarterback",
        "email": "troy.aikman@nfl.org",
        "dob": "03/09/1952",
        "address": "909 Stadium Drive",
        "city": "Dallas",
        }""", ),
    ("""{
        "name": "Danny DeVito",
        "work": "Actor",
        "email": "danny.devito@actor.org",
        "dob": "26/09/1963",
        "address": "9292 Philly Street",
        "city": "Philadelphia",
        }""", ),
    ("""{
        "name": "Andrew Reynolds",
        "work": "Skateboarder",
        "email": "andrew.reynolds@baker.org",
        "dob": "11/02/1976",
        "address": "498 Alameda Street",
        "city": "San Diego",
        }""", ),
    ("""{
        "name": "Elon Musk",
        "work": "CEO",
        "email": "elon.musk@tesla.org",
        "dob": "12/12/1985",
        "address": "9472 Beach Street",
        "city": "Silicon Valley",
        }""", ),
    ]
)

db = lit.connect('jobs2.db')

with db:
    cursor = db.cursor()
    cursor.executemany('INSERT INTO jobsList(JSON) VALUES (?)', insertIntoJobsList)

    print("Data Inserted Successfully")

