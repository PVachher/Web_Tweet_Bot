list1 = []
def tweeter(value,name):

    CONSUMER_KEY = "78HEolMmPKg0rZOXz4scZs44C" #keep the quotes, replace this with your consumer key

    CONSUMER_SECRET = "03AiFgZaIRYXdbACExekxnDZkVPllBWBUv6sI0QYsO28jYkOdH"#keep the quotes, replace this with your consumer secret key

    ACCESS_KEY = " 750375044363087872-PJTB81Eoi10yFQ7oWl9q5oKQE2VkrpI" #keep the quotes, replace this with your access token

    ACCESS_SECRET = "WXadh0HeGGVFfYLBXPs21t9KKmhvRCZfLq4lUtEhblWFv"#keep the quotes, replace this with your access token secret

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

    api = tweepy.API(auth)
    z = "Tweet By " + name + " : " + value
    api.update_status(z)
    print "Tweet By", name, " : ", value

from flask import *
from flask import request
from flask import jsonify
import tweepy, time


app = Flask(__name__)
l = ""

@app.route('/', methods=['GET', 'POST'])
def login():
    from Sample import analytics, tweetcall, antiabuse, antiname
    error = ""
    analytics(request.access_route[0])
    if request.method == 'POST':
	tweetcall(request.form['Name'], request.access_route[0], request.form['Tweet'], antiabuse(request.form['Tweet']))
	if len(request.form['Tweet']) == 0 or len(request.form['Name']) == 0:
		error = "Please enter complete details!"
	else:
		print len(antiabuse(request.form['Tweet']))
		if antiname(request.form['Name']) == True:
			if len(antiabuse(request.form['Tweet'])) > 120: 
				error = "Tweet is above the specified word limit!"			
			else:			
				tweeter(antiabuse(request.form['Tweet']),'NoName')
				error = "Tweet Posted and Good Luck trying to be Prateek!"
		elif antiabuse(request.form['Tweet']) != request.form['Tweet']:	
			if len(antiabuse(request.form['Tweet'])) > 120: 
				error = "Tweet is above the specified character limit!"	
			else:
				tweeter(antiabuse(request.form['Tweet']),request.form['Name'])
				error = "Tweet Posted, but please avoid abusing!"
		else:
			if len(antiabuse(request.form['Tweet'])) > 120: 
				error = "Tweet is above the specified word limit!"	
			else:
				tweeter(antiabuse(request.form['Tweet']), request.form['Name'])			
				error = "Tweet Successfully Posted"
    return render_template('new.html', error=error)

@app.route('/new')
def new():
    return render_template('new.html')

if __name__ == '__main__':
	app.run(debug=True)
