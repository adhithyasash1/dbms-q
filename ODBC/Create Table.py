import psycopg2

def createTable():
	conn = None
	try:
		conn = psycopg2.connect(database = "mydb", user = "myuser", \
				password = "mypass", host = "127.0.0.1", port = "5432") # connect to the database
		cur = conn.cursor() # create a new cursor
		cur.execute(’’’CREATE TABLE EMPLOYEE \
			(emp_num INT PRIMARY KEY NOT NULL, \
			emp_name VARCHAR(40) NOT NULL, \
			department VARCHAR(40) NOT NULL)’’’) # execute the CREATE TABLE statement
		conn.commit() # commit the changes to the database
		print ("Table created successfully")
		cur.close() # close the cursor
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close() # close the connection

createTable() #function call