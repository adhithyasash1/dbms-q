'''
This API opens a connection to the PostgreSQL database. If database is opened
successfully, it returns a connection object.
'''
psycopg2.connect(database="mydb", user="myuser", password="mypass"
host="127.0.0.1", port="5432")

# This method closes the database connection
connection.close()

# This routine creates a cursor which will be used throughout the program.
connection.cursor()

# This method closes the cursor.
cursor.close()

'''
This routine executes an SQL statement. The SQL statement may be parameterized
(i.e., placeholders instead of SQL literals). The psycopg2 module supports placeholder
using %s sign. For example: cursor.execute("insert into people values (%s,
%s)", (who, age))
'''
cursor.execute(sql [, optional parameters])

'''
This routine executes an SQL command against all parameter sequences or mappings
found in the sequence SQL.
'''
cursor.executemany(sql, seq of parameters)

'''
This routine executes a stored database procedure with the given name. The sequence
of parameters must contain one entry for each argument that the procedure expects.
'''
cursor.callproc(procname[, parameters])

'''
This is a read-only attribute which returns the total number of database rows that have
been modified, inserted, or deleted by the last execute().
'''
cursor.rowcount

'''
This method fetches the next row of a query result set, returning a single sequence, or
None when no more data is available.
'''
cursor.fetchone()

'''
This routine fetches the next set of rows of a query result, returning a list. An empty list
is returned when no more rows are available. The method tries to fetch as many rows as
indicated by the size parameter.
'''
cursor.fetchmany([size=cursor.arraysize])

'''
This routine fetches all (remaining) rows of a query result, returning a list. An empty
list is returned when no rows are available.
'''
cursor.fetchall()

'''
This method commits the current transaction. If you do not call this method, anything
you did since the last call to commit() is not visible to other database connections.
'''
connection.commit()

# This method rolls back any changes to the database since the last call to commit().
connection.rollback()













