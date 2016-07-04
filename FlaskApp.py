list1 = []
def tweeter(value,name):

    CONSUMER_KEY = "JFiI3kPwe030rdE0J27MSnn1X" #keep the quotes, replace this with your consumer key

    CONSUMER_SECRET = "SQFI63uPiOTmUr1lEpe70IVt0q9z2uI8FTGD6y3mptzSbAhAI5"#keep the quotes, replace this with your consumer secret key

    ACCESS_KEY = "2444077003-YyDmmrzasGsD8jBkWRbQDimoiaapN3JBxS4eGyG" #keep the quotes, replace this with your access token

    ACCESS_SECRET = "g58CKSpwP5MslPVGgLuOAa6kAV1NO2TGTm67nC5b3du28"#keep the quotes, replace this with your access token secret

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

    api = tweepy.API(auth)
    z = "Tweet By " + name + " : " + value
    api.update_status(z)
    print "Tweet By", name, " : ", value

from flask import *
import tweepy, time


app = Flask(__name__)
l = ""

@app.route('/', methods=['GET', 'POST'])
def login():
    from Sample import analytics
    error = None
    analytics()
    if request.method == 'POST':
        tweeter(request.form['Tweet'],request.form['Name'])
    return render_template('new.html', error=error)

@app.route('/new')
def new():
    return render_template('new.html')

if __name__ == '__main__':
	app.run(debug=True)
