import sqlite3

db_file='my_db.db'

def create_table():
    conn = sqlite3.connect(db_file)
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS texttable (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL
                )''')

    conn.close()

def insert_values():
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    names = [('Matti',), ('Ville',), ('Kaisa',), ('Mikko',)]
    c.executemany('INSERT INTO texttable (name) VALUES (?)', names)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_table()
    insert_values()
    print("Taulu ja arvot lisätty onnistuneesti.")