from base64 import b64decode as ck
def tweetcall(name,ipaddr,defaulttweet,modifiedtweet):
	import pymysql
	from time import gmtime, strftime
	db = pymysql.connect("52.66.7.114", "root", ck('V2VsY29tZUAxMjM0'), "tweetbotpv")
	cursor = db.cursor()
	sql = "INSERT INTO TweetCount (Name,TimeStamp,ipaddr,DefaultTweet,ModifiedTweet) VALUES ('%s', '%s', '%s', '%s', '%s')" % (name, strftime("%a, %d %b %Y %X +0000", gmtime()), ipaddr, defaulttweet, modifiedtweet)
	try:
	   cursor.execute(sql)
	   db.commit()
	except:
	   db.rollback()
	db.close()

def antiabuse(tweet):
	database = ['fuck', 'asshole', 'shit', 'fucker', 'ass', 'prateek','chut','bhosadiwale', "abuse", "behenchod","bhenchod","bancho","bhadve",'betichod']
	final = ""
	tweet=tweet.split()
	for k in tweet:
		print k.lower()
		if k.lower() in database:
			final += k[0]
			final += "*" * (len(k)-2)
			final += k[-1]
		else:
			final += k
		final += " "

	return final[:-1]

def antiname(name):
	database = ['prateek','vachher']
	name = name.split()
	for k in name:
		if k.lower() in database:
			return True
		else:
			return False

