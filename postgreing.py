# -*- coding: utf-8 -*-
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="blog_tutorial",
    user="postgres",
    password="splurgeola")

cur = conn.cursor()


def ShowEntries():
    # A sample query of all data from the "posts" table in the "blog_tutorial" database
    cur.execute("""SELECT * FROM posts""")
    query_results = cur.fetchall()
    print(query_results)
    # Close the cursor and connection to so the server can allocate
    # bandwidth to other requests


def AddEntry(title, content, author, date_posted):
    cur.execute("""INSERT INTO posts (title, content, author, date_posted)
    VALUES ('{}', '{}', '{}', '{}');""".format(title, content, author, date_posted))
    conn.commit()


def DeleteByID(id):
    cur.execute("""DELETE FROM posts WHERE id = {};""".format(id))
    conn.commit()


def EditByID(new_date, id):
    cur.execute("""UPDATE posts
                   SET date_posted = '{}' 
                   WHERE id = {};""".format(new_date, id))
    conn.commit()


# AddEntry("python entry", "python content", "not me", "2021-09-09")
# DeleteByID(7)
# EditByID('2022-01-01', 7)
# ShowEntries()

cur.close()
conn.close()

#%%
cur.execute("""CREATE DATABASE airports
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'Russian_Russia.1251'
    LC_CTYPE = 'Russian_Russia.1251'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;""")
query_results = cur.fetchall()
print(query_results)