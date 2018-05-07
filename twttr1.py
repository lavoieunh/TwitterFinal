import json
#import oauth2 as oauth
import oauth2 as oauth
class Auth(object):

    def runauth(self, API_KEY, API_SECRET, CONSUMER_KEY, CONSUMER_SECRET):
        consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
        access_token = oauth.Token(key=API_KEY, secret=API_SECRET)
        client = oauth.Client(consumer, access_token)
        return(client)

#if __name__ == "__main__":
#    Auth()
