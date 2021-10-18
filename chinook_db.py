# https://www.sqlitetutorial.net/

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

import sqlite3

conn = sqlite3.connect('chinook.db')
cur = conn.cursor()

# query = "SELECT * FROM albums;"
# results = cur.execute(query).fetchall()
# print(results)

# query = '''SELECT
#                 name,
#                 milliseconds,
#                 bytes,
#                 albumid
#             FROM
#                 tracks
#             WHERE
#                 albumid = 1
#             AND
#                 milliseconds > 250000;'''
# results = cur.execute(query).fetchall()
# print(results)

# query = '''SELECT
#                 name,
#                 albumid,
#                 composer
#             FROM
#                 tracks
#             WHERE
#                 composer LIKE '%Smith%'
#             ORDER BY
#                 albumid
#             LIMIT
#                 10'''
# results = cur.execute(query).fetchall()
# print(results)

# query = '''SELECT 
#                 Name,
#                 Title
#             FROM 
#                 tracks
#             INNER JOIN albums
#                 ON tracks.AlbumId = albums.AlbumId
#             LIMIT
#                  10;'''
# results = cur.execute(query).fetchall()
# print(results)

# query = '''SELECT
#                 tracks.name AS track,
#                 albums.title AS album,
#                 artists.name AS artist
#             FROM
#                 tracks
#             INNER JOIN
#                 albums ON albums.albumid = tracks.albumid
#             INNER JOIN
#                 artists ON artists.artistid = albums.artistid
#             LIMIT
#                 20;'''
# results = cur.execute(query).fetchall()
# print(results)

query = '''SELECT
                tracks.name AS track,
                albums.title AS album,
                artists.name AS artist
            FROM
                tracks
            INNER JOIN
                albums ON albums.albumid = tracks.albumid
            INNER JOIN
                artists ON artists.artistid = albums.artistid
            WHERE
                track = 'The Trooper';'''
results = cur.execute(query).fetchall()
print(results)



conn.close()

