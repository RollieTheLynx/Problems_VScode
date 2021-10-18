'''
SELECT DISTINCT column_list
FROM table_list
  JOIN table ON join_condition
WHERE row_filter
ORDER BY column
LIMIT count OFFSET offset
GROUP BY column
HAVING group_filter;
'''


from os import listdir, stat
from os.path import isfile, join
import sqlite3

conn = sqlite3.connect('files_database.sqlite')
cur = conn.cursor()

def MakeTable(path):
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    # print(onlyfiles)

    # Make some fresh tables using executescript()
    cur.executescript('''
    DROP TABLE IF EXISTS Files;

    CREATE TABLE Files (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name    TEXT UNIQUE,
        size    INTEGER,
        modified    TEXT
    )
    ''')

    for file in onlyfiles:
        size = stat(file).st_size
        modified_date = stat(file).st_mtime

        cur.execute('''INSERT OR IGNORE INTO Files (name) 
                VALUES ( ? )''', ( file, ) )
        cur.execute('''INSERT OR REPLACE INTO Files
            (name, size, modified) 
            VALUES ( ?, ?, ? )''', 
            ( file, size, modified_date ) )

    conn.commit()

def ShowAll():
    query = "SELECT * FROM Files;"
    results = cur.execute(query).fetchall()
    print(results)

def SelectByName(filename):
    query = f"SELECT name FROM Files WHERE name LIKE '%{filename}%' AND modified > 1621641600"
    results = cur.execute(query).fetchall()
    print(results)



# MakeTable("C:\\Users\\Rollie\\Documents\\Python_Scripts\\Problems_VScode")
ShowAll()
SelectByName('Angstrem')


conn.close()
