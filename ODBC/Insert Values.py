import psycopg2

def insertRecord(num, name, dept):
	conn = None
	try:
		# connect to the PostgreSQL database
		conn = psycopg2.connect(database = "mydb", user = "myuser", \
				password = "mypass", host = "127.0.0.1", port = "5432")
		cur = conn.cursor() # create a new cursor
		# execute the INSERT statement
		cur.execute("INSERT INTO EMPLOYEE (emp_num, emp_name, department) \
					VALUES (%s, %s, %s)", (num, name, dept))
		conn.commit() # commit the changes to the database
		print ("Total number of rows inserted :", cur.rowcount);
		cur.close() # close the cursor
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close() # close the connection

insertRecord(110, ‘Bhaskar’, ’HR’) #function call