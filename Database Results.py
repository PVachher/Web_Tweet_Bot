def get_sitehits():
	import MySQLdb
	db = MySQLdb.connect("db4free.net","tweetbotpv","Welcome123","tweetbotpv" )
	cursor = db.cursor()
	from time import gmtime, strftime
	sql = "SELECT * FROM SiteHits"
	try:
	   cursor.execute(sql)
	   results = cursor.fetchall()
	   for k in results:
		print k

	   db.commit()
	except:
	   print "ERROR"
	   db.rollback()
	db.close()

def get_tweetcount():
	import MySQLdb
	db = MySQLdb.connect("db4free.net","tweetbotpv","Welcome123","tweetbotpv" )
	cursor = db.cursor()
	from time import gmtime, strftime
	sql = "SELECT * FROM TweetCount"
	try:
	   cursor.execute(sql)
	   results = cursor.fetchall()
	   for k in results:
		print k

	   db.commit()
	except:
	   print "ERROR"
	   db.rollback()
	db.close()

a = 1
while a != 0:
	a = input("Enter '1' for SiteHits, '2' for TweetCount, '0' to Exit: ")
	print ""
	if a == 1:
		get_sitehits()
	elif a == 2:
		get_tweetcount()
	elif a == 0:
		a = 0
	else:
		print "Error, Try Again"

	print ""

