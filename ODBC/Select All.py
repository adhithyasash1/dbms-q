import psycopg2

def selectAll():
	conn = None
	try:
		# connect to the PostgreSQL database
		conn = psycopg2.connect(database = "mydb", user = "myuser", \
				password = "mypass", host = "127.0.0.1", port = "5432")
		cur = conn.cursor() # create a new cursor
		# execute the SELECT statement
		cur.execute("SELECT emp_num, emp_name, department FROM EMPLOYEE")
		rows = cur.fetchall() # fetches all rows of the query result set
		for row in rows:
			print (print ("Employee ID = ", row[0], ", NAME = ", \
					row[1], ", DEPARTMENT = ", row[2]))
		cur.close() # close the cursor
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		conn.close() # close the connection

selectAll() # function call