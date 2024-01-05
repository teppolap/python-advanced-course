import tkinter as tk
import sqlite3
db_file='my_db.db'

#Your code here!
import sqlite3
import tkinter as tk

def read_data_from_database(db_file):
    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        cursor.execute("SELECT data FROM textdata")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return [row[0] for row in rows]

    except sqlite3.Error as e:
        print("Virhe tietokantayhteydessä:", e)
        return []

def update_label():
    global data_list, index
    lbl.config(text=data_list[index])
    index = (index + 1) % len(data_list)

data_list = read_data_from_database("my_db.db")
index = 0

root = tk.Tk()
root.title("Kyselytietojen näyttäminen")

lbl = tk.Label(root, text="")
lbl.pack()

btn = tk.Button(root, text="Näytä seuraava arvo", command=update_label)
btn.pack()

if __name__ == "__main__":
    root.mainloop()
