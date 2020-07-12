
from os import listdir, stat
from os.path import isfile, join
import sqlite3

mypath = "C:\\Users\\Rollie\\Desktop\\Coursera\\Problems"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
#print(onlyfiles)

conn = sqlite3.connect('files_database.sqlite')
cur = conn.cursor()

# Make some fresh tables using executescript()
cur.executescript('''
DROP TABLE IF EXISTS Files;

CREATE TABLE Files (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE,
    size    INTEGER
)
''')

for file in onlyfiles:
    size = stat(file).st_size

    cur.execute('''INSERT OR IGNORE INTO Files (name) 
            VALUES ( ? )''', ( file, ) )
    cur.execute('''INSERT OR REPLACE INTO Files
        (name, size) 
        VALUES ( ?, ? )''', 
        ( file, size ) )

    conn.commit()
