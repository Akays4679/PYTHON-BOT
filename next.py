import tweepy

# Authentication keys and tokens
api_key = "4GAoRYlZV6sqZRirgM4uG4JNs"
api_secret_key = "dtAuIKFASmyhrHyr56YFIdauin3hyg2q2QJWIQOWlrPnWr0YGd"
access_token = "1812379971832164352-dXHHuZ2mqGR1jJWUvpelOBMNIHx43Z"
access_token_secret = "F6m6eFLbudOD9oeFTToXf91QsA6Ai1bxJHkWMXjVMj8np"

# Authenticate with Twitter API
auth = tweepy.OAuth1UserHandler(
    consumer_key=api_key,
    consumer_secret=api_secret_key,
    access_token=access_token,
    access_token_secret=access_token_secret
)

# Create API object with wait_on_rate_limit enabled
api = tweepy.API(auth, wait_on_rate_limit=True)

try:
    # Attempt to fetch tweets, checking for errors
    tweets = api.user_timeline(count=5, tweet_mode='extended')  # Fetch the latest 5 tweets
    
    if not tweets:
        print("No tweets found.")
    
    # Loop through the tweets and print their full text
    for tweet in tweets:
        print(f"Tweet: {tweet.full_text}\n")
    
except tweepy.errors.Forbidden as e:
    # If there's an error, print the error message
    print(f"Error occurred: {e}")
    
    # To debug, print out the error response code
    if hasattr(e, 'response') and e.response is not None:
        print(f"Error response: {e.response}")
    
except Exception as ex:
    # Catch any unexpected errors
    print(f"An unexpected error occurred: {ex}")
