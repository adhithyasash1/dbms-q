'''
In this question, you have to write a Python program to print the names of the players and the team of each player of all those players whose jersey number is a prime number. 

The list should be ordered in reverse alphabetical order of player names. If two or more players have the same name, then further sorting should be done on the team name, again in reverse alphabetical order.

The format of output is as given below:

Name of the player, followed by a comma (,), then a space and then the team name.


For example, if Arjun has jersey number 5 and is playing for All Stars and Pranav, with jersey number 7, is playing for team Amigos, then the output will be:

Pranav, Amigos

Arjun, All Stars
'''

import psycopg2
import sys
import os

def isprime(x):
    if x <=1:
        return False
    for i in range(2,x):
        if x%i==0 :
            return False
    return True

conn=None
try:
    conn= psycopg2.connect(database=sys.argv[1],user=os.environ.get('PGUSER'), password=os.environ.get('PGPASSWORD'),host=os.environ.get('PGHOST'),port=os.environ.get('PGPORT'))
    curr=conn.cursor()
    curr.execute( "select t.name,p.name,p.jersey_no from teams t , players p where t.team_id=p.team_id order by p.name desc,t.name desc")
    while True:
        row=curr.fetchone()
        if not row :
            break
        if isprime(row[2]):
            print(f'{row[1]}, {row[0]}')
    curr.close()
except(Exception,psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()
