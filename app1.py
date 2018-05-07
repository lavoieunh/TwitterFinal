import os
import time
import classinput
import twttr1
import flask

app = flask.Flask(__name__)   # create our flask app

# configure Twitter API
#3twitter = twttr1(
#            auth=OAuth(os.environ.get('APIKEY'), os.environ.get('APISECRET'),
#                       os.environ.get('CONSUMERKEY'), os.environ.get('CONSUMERSECRET'))
#
#           )

@app.route('/')
def main():

    APIKEY='455215929-Exmhl2w5l1LdckIkFWRoiahwmrawltGzwWQ1Mffs'

    APISECRET ='elIv4IjcH9IuJNYUWwh7zbzsJJ83P5mIOEsqoQfaJ4Ri9'

    CONSUMERKEY ='LmsuQDk0UNVEk0BzXDEMXVyHw'

    CONSUMERSECRET='J5QTV4bELgTH6PemoXeVkpw8y2AktHClcAVvUB27pM6NGAFbr3'

    aut = twttr1.Auth()
    client = aut.runauth(APIKEY, APISECRET, CONSUMERKEY, CONSUMERSECRET)

    ci = classinput.UserReq()

    input11 = raw_input("For home timeline, type home: ")
    input22 = raw_input("Type something to search for, no # needed")

    print(ci.home_timeline(input11, client))
    print(ci.tweet_search(input22, client))


#return render_template('index.html', **templateData)

if __name__ == "__main__":
	#app.debug = True
    app.run(host='0.0.0.0', port=5000, debug=True)
