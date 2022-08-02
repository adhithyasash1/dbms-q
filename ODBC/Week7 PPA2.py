'''
In this problem, you have to write a Python program to print an encoding of the ids of the host teams whose jersey colour at home is different from the jersey colour when they play away from home.


The encoding must be using a shift cipher, which is detailed below.

An alphabet is mapped to another alphabet as follows. For a given alphabet α, let pos be the position at which α occurs in the alphabet listing (A at 1, B at 2, …. Z at 26). Then the encoding of α is the alphabet at the position (pos + 7) mod 26.

For example, if M is the alphabet, then the position at which M occurs in the alphabet listing is 13. Then, the encoding of M is the alphabet at the position (13 + 7) mod 26 = 20, which is T. 

For each digit β, the encoding of β is (β+7) mod 10.

For example, if 3 is the digit, then the encoding of 3 is the number (3 + 7) mod 10 = 0.

The ids should be listed in the ascending order before performing the encoding.

Each line in the output of the program must correspond to one row retrieved from the table.
'''

import psycopg2 as pg
import sys
import os

def encode(s):
    enco = ''
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    num = '0123456789'
    for elem in s:
        if elem in alpha:
            pos = (alpha.find(elem)+7)%26
            enco += alpha[pos]
        elif elem in num:
            pos = (int(elem)+7)%10
            enco += str(pos)
    return(enco)

conn = None
try:
    conn = pg.connect(database=sys.argv[1],
                        user = os.environ.get('PGUSER'),
                        password = os.environ.get('PGPASSWORD'),
                        host = os.environ.get('PGHOST'),
                        port = os.environ.get('PGPORT'))

    cur = conn.cursor()
    cur.execute("select team_id from teams where jersey_home_color != jersey_away_color order by team_id;")

    rows = cur.fetchall()
    for row in rows:
        print(encode(row[0]))
    cur.close()
except(Exception, pg.DatabaseError) as error:
    print(error)
finally:
    conn.close()
