@app.route("/savedetails",methods = ["POST"])
	def saveDetails():
	cno = request.form["cno"]
	name = request.form["name"]
	email = request.form["email"]
	conn = None
	try:
		conn = psycopg2.connect(database = "mydb", user = "myuser", \
			password = "mypass", host = "127.0.0.1", port = "5432") # connect to the PostgreSQL database
		cur = conn.cursor() # create a new cursor
		cur.execute("INSERT INTO Candidate (cno, name, email) \
					VALUES (%s, %s, %s)", (cno, name, email)) # execute the INSERT statement
		conn.commit() # commit the changes to the database
		cur.close() # close the cursor
	except (Exception, psycopg2.DatabaseError) as error:
		render_template("fail.html")
	finally:
		if conn is not None:
			conn.close() # close the connection
	return render_template("success.html")

'''
<!DOCTYPE html>
<html>
	<head>
		<title>Add Email</title>
	</head>
	<body>
		<h2>Email Information</h2>
		<form action = "/savedetails" method="post">
			<table>
			<tr><td>CNO</td><td><input type="text" name="cno" required></td></tr>
			<tr><td>Name</td><td><input type="text" name="name" required></td></tr>
			<tr><td>Email</td><td><input type="text" name="email" required></td></tr>
			<tr><td><input type="submit" value="Submit"></td></tr>
			</table>
		</form>
	</body>
</html>
'''