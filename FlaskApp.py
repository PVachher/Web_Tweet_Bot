def tweeter(value,name):
    CONSUMER_KEY = "ewbwEAacaqCZaBDxFCUWbuDqX"
    CONSUMER_SECRET = "5aKXgyU3mYZdoLJUtNJs72uu1U29W4Zj0wlEa7sjPEKeBN5T5i"
    ACCESS_KEY = "750375044363087872-nBWa34rZnsnMJ5qbdlGpfUd9gjiunvB"
    ACCESS_SECRET = "naE0AFdEzRyOAnMbw1G8ZcfQS5qkJymyr3OhFSjpwCa3p"
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
SITE_KEY = '6Lds9yQTAAAAAGCVEffBIsTvC7BFzBIcSQ65fOis'
SECRET_KEY = '6Lds9yQTAAAAAHyh20hvdKWcuspU9orZqYShR0Z2'
@app.route('/', methods=['GET', 'POST'])
def login():
    from Sample import tweetcall, antiabuse, antiname
    error = ""
    if request.method == 'POST':
	import urllib2
	msg = ''
	showalert = False
	response = request.form.get('g-recaptcha-response')
	if checkRecaptcha(response,SECRET_KEY):
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
	else:
		error = "INVALID CAPTCHA"

    return render_template('index.html', error=error)

def checkRecaptcha(response, secretkey):
    import urllib2
    url = 'https://www.google.com/recaptcha/api/siteverify?'
    url = url + 'secret=' +secretkey
    url = url + '&response=' +response
    try:
        jsonobj = json.loads(urllib2.urlopen(url).read())
	print jsonobj
        if jsonobj['success']:
            return True
        else:
            return False
    except Exception as e:
        print e
        return False


if __name__ == '__main__':
	app.run(host='0.0.0.0',debug=True)
