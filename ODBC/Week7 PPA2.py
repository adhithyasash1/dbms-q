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