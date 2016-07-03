import MySQLdb

# Open database connection
db = MySQLdb.connect("vachher.ddns.net","remote","Welcome@1234","TestDB" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT * FROM `counter`;")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()

print "Database version : %s " % data

# disconnect from server
db.close()
