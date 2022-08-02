import psycopg2

def updateRecord(num, dept):
	conn = None
	try:
		# connect to the PostgreSQL database
		conn = psycopg2.connect(database = "mydb", user = "myuser", \
				password = "mypass", host = "127.0.0.1", port = "5432")
		cur = conn.cursor() # create a new cursor
		# execute the UPDATE statement
		cur.execute("UPDATE EMPLOYEE set department = %s where emp_num = \
			%s", (dept, num))
		conn.commit() # commit the changes to the database
		print ("Total number of rows updated :", cur.rowcount)
		cur.close() # close the cursor
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		conn.close() # close the connection

updateRecord(110, "Finance") #function call