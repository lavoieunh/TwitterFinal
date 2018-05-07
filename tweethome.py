import os
import time
from classinput import *
import twttr1
import flask

app = flask.Flask(__name__)   # create our flask app

APIKEY='455215929-Exmhl2w5l1LdckIkFWRoiahwmrawltGzwWQ1Mffs'

APISECRET ='elIv4IjcH9IuJNYUWwh7zbzsJJ83P5mIOEsqoQfaJ4Ri9'

CONSUMERKEY ='LmsuQDk0UNVEk0BzXDEMXVyHw'

CONSUMERSECRET='J5QTV4bELgTH6PemoXeVkpw8y2AktHClcAVvUB27pM6NGAFbr3'

aut = twttr1.Auth()
client = aut.runauth(APIKEY, APISECRET, CONSUMERKEY, CONSUMERSECRET)

@app.route('/')
def main():

    ci = classinput.UserReq()

    input1 = raw_input("For home timeline, type home: ")
    input2 = raw_input("Type something to search for, no # needed")

    print(ci.home_timeline(input1, client))
    print(ci.tweet_search(input2, client))

if __name__ == "__main__":
	#app.debug = True
    app.run(host='0.0.0.0', port=5000, debug=True)

#return render_template('index.html', **templateData)

#if __name__ == "__main__":
	#app.debug = True
#    app.run(host='0.0.0.0', port=5000, debug=True)
