import psycopg2

def deleteRecord(num):
	conn = None
	try:
		# connect to the PostgreSQL database
		conn = psycopg2.connect(database = "mydb", user = "myuser", \
				password = "mypass", host = "127.0.0.1", port = "5432")
		cur = conn.cursor() # create a new cursor
		# execute the DELETE statement
		cur.execute("DELETE FROM EMPLOYEE WHERE emp_num = %s", (num,))
		conn.commit() # commit the changes to the database
		print ("Total number of rows deleted :", cur.rowcount)
		cur.close() # close the cursor
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		conn.close() # close the connection

deleteRecord(110) #function call