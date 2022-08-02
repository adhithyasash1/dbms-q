'''
In this question, you must write a Python program to output the name of the main referee for a given match date (in yyyy-mm-dd format). The input to your program is a file named “date.txt” that has the match date as the first word of the file. Your program must assume that date.txt resides in the same folder as your Python program. 


The output name has to be formatted as follows. The last name is displayed followed by the initials of the first name, then a full stop, a space and then the initials of the middle name (if the middle name exists), followed by a full stop.

For example, if the name of the main referee is “Kennedy Sapam”, the output must be ”Sapam K.” 

If the name of the main referee is “Asit Kumar Sarkar”, the output must be ”Sarkar A. K.”
'''

week7 grpa1

import psycopg2
import sys
import os

database = sys.argv[1]
user = os.environ.get('PGUSER')
password = os.environ.get('PGPASSWORD')
host = os.environ.get('PGHOST')
port = os.environ.get('PGPORT')

def referee(L):
    st = str(L[0][0])
    ans, x = '', st.split(' ')
    ans += x[-1]
    for i in x:
        if i != x[-1]:
            ans += ' '+i[0]+'.'
    return ans
  
def get_date():
    with open('date.txt') as f:
        first_line = f.readline()
    return first_line

def get_referee(database, user, password, host, port):
    conn = None
    date = get_date()
    try:
        # connect to the PostgreSQL database
        conn = psycopg2.connect(database = database, user = user,
                password = password, host = host, port = port)
        cur = conn.cursor() # create a new cursor
        # execute the SELECT statement
        cur.execute('select k.name from matches as m, match_referees as r, referees as k where m.match_num = r.match_num and k.referee_id = r.referee and m.match_date = %s', (date,))
        rows = cur.fetchall() # fetches all rows of the query result set
        return(referee(rows))
        cur.close() # close the cursor
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close() # close the connection

print(get_referee(database, user, password, host, port))

'''
import psycopg2
import sys
import os

def referee(L):
    st = str(L[0][0])
    ans, x = '', st.split(' ')
    ans += x[-1]
    for i in x:
        if i != x[-1]:
            ans += ' '+i[0]+'.'
    return ans
  
def get_date():
    with open('date.txt') as f:
        first_line = f.readline()
    return first_line

def get_referee():
    conn = None
    date = get_date()
    try:
        # connect to the PostgreSQL database
        conn = psycopg2.connect(database = 'flisdb', user = 'postgres',
                password = 'Gfivez17!', host = 'localhost', port = '5432')
        cur = conn.cursor() # create a new cursor
        # execute the SELECT statement
        cur.execute('select k.name from matches as m, match_referees as r, referees as k where m.match_num = r.match_num and k.referee_id = r.referee and m.match_date = %s', (date,))
        rows = cur.fetchall() # fetches all rows of the query result set
        return(referee(rows))
        cur.close() # close the cursor
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close() # close the connection

print(get_referee())
'''
