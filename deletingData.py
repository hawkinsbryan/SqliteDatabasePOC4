import sqlite3 as lit

db = lit.connect('jobs2.db')

with db:
    jobId = 4

    cursor = db.cursor()
    cursor.execute("DELETE FROM jobsList WHERE jobId = ? ", (jobId,))
    # cursor.execute("DELETE FROM jobsList")

    db.commit()
    print("Data deleted successfully")

