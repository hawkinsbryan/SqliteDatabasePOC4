import sqlite3 as lit

db = lit.connect('jobs2.db')

with db:
    newJson = ("""{
        "name": "Steve jobs",
        "work": "Inventor",
        "email": "steve.jobs@chef.org",
        "dob": "29/04/1950",
        "address": "7665 Hacker Way",
        "city": "Silicon Valley",
        }""")
    jobId = 4

    cursor = db.cursor()
    cursor.execute('UPDATE jobsList SET JSON = ? WHERE jobId = ? ', (newJson, jobId))
    db.commit()
    print("Data updated successfully")

