import psycopg2
import sys
import os
from math import pi, cos

def L1():
    with open('numbers.txt') as f:
        x = f.readline()
    return x

def L2(x):
    y = int(x)
    year =  2001 + 4*(y)
    return year

def get_ans(database, user, password, host, port):
    conn = None
    x = L1()
    year = L2(x)
    try:
        # connect to the PostgreSQL database
        conn = psycopg2.connect(database = database, user = user,
                password = password, host = host, port = port)
        cur = conn.cursor() # create a new cursor
        # execute the SELECT statement
        cur.execute('select b.ISBN_no from book_catalogue as b where b.year = %s', (year,))
        ans = cur.fetchall() # fetches all rows of the query result set
        for i in ans:
            print()
            print(i[0])
        cur.close() # close the cursor
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close() # close the connection

def ans():
    return(get_ans('lisdb', 'postgres', 'password', 'localhost', '5432'))

