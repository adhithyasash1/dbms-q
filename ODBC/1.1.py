import psycopg2
import sys
import os
database = sys.argv[1]	

user = os.environ.get('PGUSER') 

password = os.environ.get('PGPASSWORD') 

host = os.environ.get('PGHOST')

port = os.environ.get('PGPORT')

def prime(x):
    flag=True
    if x>1:
        for i in range(2,int(x)):
            if x%i == 0:
                flag=False
                break
    return flag
                
            
            
        

def selectAll():
    conn=None
    try:
        conn = psycopg2.connect(database=database,user=user,password=password, host=host, port=port)
        cur = conn.cursor()
        cur.execute(''' select p.name,  t.name, p.jersey_no
                         from players p, teams t
                         where p.team_id = t.team_id
                         
                          ''')
        rows = cur.fetchall()
        lst=[]
        for row in rows:
            if prime(int(row[-1])):
                lst.append((row[0],row[1]))
        for tup in sorted(lst,reverse=True):
            print(f'{tup[0]}, {tup[1]}')
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        conn.close()
selectAll()