import sqlite3

db_file='my_db.db'

def fetch_and_print_names():
    conn = sqlite3.connect(db_file)
    c = conn.cursor()

    # Suoritetaan kysely
    c.execute('SELECT name FROM texttable')

    rows = c.fetchall()

    for row in rows:
        print(row[0])

    conn.close()

if __name__ == "__main__":
    fetch_and_print_names()