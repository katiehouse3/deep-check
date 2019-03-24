# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

# Import the tweepy library
import tweepy
import pprint

pp = pprint.PrettyPrinter(indent=4)

# Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = '2620473211-RWN2g8omy31oxu7xu0b03fxSQ2rH2HrTMcgjAJL'
ACCESS_SECRET = 'dySWOs8voQTlN9uaLOJNuN32v7QdQwMfNcNDCXV8O6Ku9'
CONSUMER_KEY = '7KOV5jhvAty3QtBJurrllMggy'
CONSUMER_SECRET = 'oSTU2ViKAuUHPZxRZ1Ha6OGv6jU8eXk5VGcc7N4wx6nxuYyH1l'

# Setup tweepy to authenticate with Twitter credentials:

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

# Create the api to connect to twitter with your creadentials
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)


status_cursor = tweepy.Cursor(api.user_timeline, screen_name="dishsrivastava", count=100)
status_list = status_cursor.iterator.next()
for i in range(len(status_list)):
	print(status_list[i].text)
	#print(status_list[0].text)