#from tweepy import*
#from tweepy import TweepyException
#creating the api creadentials
import tweepy
from tweepy import TweepError
api_key="4GAoRYlZV6sqZRirgM4uG4JNs"
api_secret_key="dtAuIKFASmyhrHyr56YFIdauin3hyg2q2QJWIQOWlrPnWr0YGd"
acess_token="1812379971832164352-dXHHuZ2mqGR1jJWUvpelOBMNIHx43Z"
acess_token_secret="F6m6eFLbudOD9oeFTToXf91QsA6Ai1bxJHkWMXjVMj8np"
#authenticate with Twitter API
authflow=tweepy.OAuth1UserHandler(
    consumer_key=api_key,
    consumer_secret=api_secret_key,
access_token=acess_token,
access_token_secret=acess_token_secret
)
api=tweepy.API(authflow)
tweets=tweepy.api.user_timeline()
for tweet in tweets:
    print(tweets.text,'\n')
