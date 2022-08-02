import pyodbc

conn = pyodbc.connect('DSN = SQLS; UID = test01; PWD = test01')
cursor = conn.cursor()
cursor.execute('create table rvtest(col1 int, col2 float, col3 varchar(10))')
cursor.execute('insert into rvtest values(1, 10.0, \'abc\')')
cursor.execute('select * from rvtest')

while True:
	row = cursor.fetchone()
	if not row:
		break
	print(row)

cursor.execute('delete from rvtest')
cursor.execute('insert into rvtest values(?, ?, ?', 2, 20.0, 'xyz')
cursor.execute('select * from rvtest')

while True:
	row = cursor.fetchone()
	if not row:
		break
	print(row)
	