@app.route("/viewall")
def viewAll():
	conn = None
	try:
		# connect to the PostgreSQL database
		conn = psycopg2.connect(database = "mydb", user = "myuser", \
			password = "mypass", host = "127.0.0.1", port = "5432")
		cur = conn.cursor() # create a new cursor
		# execute the SELECT statement
		cur.execute("SELECT cno, name, email FROM Candidate")
		results = cur.fetchall() # fetches all rows of the query result set
		cur.close() # close the cursor
	except (Exception, psycopg2.DatabaseError) as error:
		render_template("fail.html")
	finally:
		conn.close() # close the connection
	return render_template("viewall.html", rows = results)

'''
<!DOCTYPE html>
<html>
	<head>
		<title>Email List</title>
	</head>
	<body>
		<h3>Email List</h3>
		<table border=5>
			<tr>
				<th>CNO</td><th>Name</td><th>Email</td>
			</tr>
			{% for row in rows %}
				<tr>
					<td>{{row[0]}}</td> <td>{{row[1]}}</td> <td>{{row[2]}}</td>
				</tr>
			{% endfor %}
			</table>
			<br><br>
			<a href="/">Go Home</a>
	</body>
</html>
'''