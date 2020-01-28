import sqlite3 as lit


def main():
    try:
        db = lit.connect('jobs2.db')
        cursor = db.cursor()

        table_query = "CREATE TABLE jobsList (jobId INTEGER PRIMARY KEY AUTOINCREMENT, JSON TEXT NOT NULL)"

        cursor.execute(table_query)
        print("Table created successfully")

    except:
        print("Failed to make table")

    finally:
        db.close()


if __name__ == "__main__":
    main()
