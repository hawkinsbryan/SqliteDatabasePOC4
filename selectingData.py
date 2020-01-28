import sqlite3 as lit
import json

db = lit.connect('jobs2.db')
# db.text_factory = str  # removes the u in the fetchall

with db:
    cursor = db.cursor()
    select_query = "SELECT * FROM jobsList"
    cursor.execute(select_query)

    rows = cursor.fetchall()

    for data in rows:
        print(data)

