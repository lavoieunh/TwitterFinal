import json
#import oauth2 as oauth
import requests
import oauth2 as oauth
class UserReq():
#    @classmethod
#    def input1(self):
#        in1 = input("For statuses on home timeline, type home: ")
#        return(in1)

#    @classmethod
#    def input2(self):
#        in2 = input("Please enter a search term")
#        return(in2)


    def home_timeline(self, input1, client):
        if input1 == "home":
            url_home = "https://api.twitter.com/1.1/statuses/home_timeline.json"
            responses, searchin = client.request(url_home)
            searchtest = json.loads(searchin)
            #for key, value in searchtest.items():
            return(searchtest)
                #print(url_home)

    def tweet_search(self, input2, client):
        upin2 = "{}&result_type=popular".format(input2)
        search = "https://api.twitter.com/1.1/search/tweets.json?q={}".format(upin2)
        responses, searched = client.request(search)
        searchresults = json.loads(searched)
        return(searchresults)

    def user_timeline(self, input3, client):
        upin2 = "{}&result_type=popular".format(input2)
        search = "https://api.twitter.com/1.1/search/tweets.json?q={}".format(upin2)
        responses, searched = client.request(search)
        searchresults = json.loads(searched)
        return(searchresults)

        #return(search)



"""

#tweets = json.loads(data)
#for tweet in tweets:
#    print(tweet['text'])


url2_home = ] ""

searchtest = json.loads(searchin)
#search = searchtest{ }
for key, value in searchtest.items():
    print(key, value)
#for tweet in searchtest:
#    print(tweet['text'])

"""
