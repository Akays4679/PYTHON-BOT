from tweepy import*
from tweepy import TweepError
#creating the api creadentials
api_keys="4GAoRYlZV6sqZRirgM4uG4JNs"
api_secret_key="dtAuIKFASmyhrHyr56YFIdauin3hyg2q2QJWIQOWlrPnWr0YGd"
ACCESS_token="1812379971832164352-dXHHuZ2mqGR1jJWUvpelOBMNIHx43Z"
ACCESS_token_secret="F6m6eFLbudOD9oeFTToXf91QsA6Ai1bxJHkWMXjVMj8np"
#authenticate with Twitter API
authflow=OAuth1UserHandler(
    consumer_key=api_keys,
    consumer_secret=api_secret_key,
access_token=ACCESS_token,
access_token_secret=ACCESS_token_secret
)
Api=API(authflow)
#tweet content
tweet_content="Hi i am bot writing this tweet"

try:
    Api.update_status(tweet_content)
    print("Tweet sent successfully!")
except TweepError as e:
    print(f"Error it is not working:{e}")
