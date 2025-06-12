import sqlite3

con = sqlite3.connect("mydatabase.db")
cursor = con.cursor()

cursor.execute(''' 
CREATE TABLE IF NOT EXISTS videos (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
''')

def main():
    pass

if __name__ == "__main__":
    main()