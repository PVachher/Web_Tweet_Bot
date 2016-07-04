
def analytics():
	import MySQLdb

	# Open database connection
	db = MySQLdb.connect("vachher.ddns.net","remote","Welcome@1234","TestDB" )

	# prepare a cursor object using cursor() method
	cursor = db.cursor()

	# Prepare SQL query to UPDATE required records
	sql = "UPDATE counter SET Count = Count + 1"
	try:
	   # Execute the SQL command
	   cursor.execute(sql)
	   # Commit your changes in the database
	   db.commit()
	except:
	   # Rollback in case there is any error
	   db.rollback()

	# disconnect from server
	db.close()




a = analytics()
