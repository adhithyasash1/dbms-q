import psycopg2
def connectDb(dbname, usrname, pwd, address, portnum):
	conn = None
	try:
		# connect to the PostgreSQL database
		conn = psycopg2.connect(database = dbname, user = usrname, \
		password = pwd, host = address, port = portnum)
		print ("Database connected successfully")
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		conn.close() # close the connection
connectDb("mydb", "myuser", "mypass", "127.0.0.1", "5432") # function call


'''
1. Use the psycopg2.connect() method with the required arguments to connect PostgresSQL. 
	It would return an Connection object if the connection established successfully.

2. Create a cursor object using the cursor() method of connection object.

3. The execute() methods run the SQL commands and return the result.

4. Use cursor.fetchall() or fetchone() or fetchmany() to read query result.

5. Use commit() to make the changes in database persistent, or use rollback() to revert
the database changes.

6. Use cursor.close() and connection.close() method to close the cursor and PostgreSQL connection

'''