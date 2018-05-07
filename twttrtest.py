import twitter

import oauth2



key='455215929-Exmhl2w5l1LdckIkFWRoiahwmrawltGzwWQ1Mffs'

secret='elIv4IjcH9IuJNYUWwh7zbzsJJ83P5mIOEsqoQfaJ4Ri9'

CONSUMER_KEY='LmsuQDk0UNVEk0BzXDEMXVyHw'

CONSUMER_SECRET='J5QTV4bELgTH6PemoXeVkpw8y2AktHClcAVvUB27pM6NGAFbr3'


api = twitter.Api(consumer_key= CONSUMER_KEY,
                  consumer_secret=CONSUMER_SECRET,
                  access_token_key=key,
                  access_token_secret=secret)




home_timeline = api.GetFriends() 

#print(home_timeline)





print(home_timeline)

print([u.screen_name for u in home_timeline])
print([u.id for u in home_timeline])