import sqlite3 as lit


def main():

    try:
        db = lit.connect('jobs2.db')
        print("Database created successfully")



    except:
        print("Failed to create database")

    finally:
        db.close()


if __name__ == "__main__":
    main()