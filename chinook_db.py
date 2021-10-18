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

## все записи
# query = "SELECT * FROM albums;"
# results = cur.execute(query).fetchall()
# print(results)

## поиск по условиям
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

## неточное соответствие
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

## JOIN
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

## два JOIN
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
#             WHERE
#                 track = 'The Trooper';'''
# results = cur.execute(query).fetchall()
# print(results)

## суммирование (MIN, MAX, SUM, COUNT, AVG)
# query = '''SELECT
#                 albums.title AS album,
#                 COUNT(trackid)
#             FROM
#                 tracks
#             INNER JOIN
#                 albums ON albums.albumid = tracks.albumid
#             GROUP BY
#                 album;'''
# results = cur.execute(query).fetchall()
# print(results)

## GROUP BY date
# query = '''SELECT
#    STRFTIME('%Y', InvoiceDate) InvoiceYear, 
#    COUNT(InvoiceId) InvoiceCount
# FROM
#    invoices
# GROUP BY
#    STRFTIME('%Y', InvoiceDate)
# ORDER BY
#    InvoiceYear;'''
# results = cur.execute(query).fetchall()
# print(results)

# несколько запросов в одну выдачу
query = '''SELECT FirstName, LastName, 'Employee' AS Type
            FROM employees
            UNION
            SELECT FirstName, LastName, 'Customer'
            FROM customers
            ORDER BY FirstName, LastName;'''
results = cur.execute(query).fetchall()
print(results)

conn.close()

