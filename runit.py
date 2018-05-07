import classinput
import twttr1

APIKEY='455215929-Exmhl2w5l1LdckIkFWRoiahwmrawltGzwWQ1Mffs'

APISECRET ='elIv4IjcH9IuJNYUWwh7zbzsJJ83P5mIOEsqoQfaJ4Ri9'

CONSUMERKEY ='LmsuQDk0UNVEk0BzXDEMXVyHw'

CONSUMERSECRET='J5QTV4bELgTH6PemoXeVkpw8y2AktHClcAVvUB27pM6NGAFbr3'

aut = twttr1.Auth()
client = aut.runauth(APIKEY, APISECRET, CONSUMERKEY, CONSUMERSECRET)

ci = classinput.UserReq()

input11 = raw_input("For home timeline, type home: ")
input22 = raw_input("Type something to search for, no # needed")
input33 = raw_input("Please enter a user to search for")

print(ci.home_timeline(input11, client))
print(ci.tweet_search(input22, client))
