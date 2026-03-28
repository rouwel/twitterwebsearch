"""
Module for using the web interface of Twitter's search.
"""

import tweepy

consumer_key = 'dw7FYgyhnDM4UlY8QT'
consumer_secret = 'IzoPhiSd4b0Z66bbN0mlzBnjTzrzySm'
access_token = '2036531793CPTkCojuU'
access_token_secret = 'hmfPu'
bearer_token = 'AAAAAAAAAAAAAAAAA'

auth = tweepy.OAuth1UserHandler(consumer_key , consumer_secret, access_token, access_token_secret)
api =  tweepy.API(auth)

try: 
    api.verify_credentials()
except Exception as e:
    print(f"Error {e}")

    # Fetch the 5 most recent tweets from your timeline
public_tweets = api.home_timeline(count=5)
for tweet in public_tweets:
    print(f"{tweet.user.screen_name}: {tweet.text}\n")

"""
Output
tweepy.errors.Forbidden: 403 Forbidden
453 - You currently have access to a subset of X API V2 endpoints and limited v1.1 endpoints (e.g. media post, oauth) only. If you need access to this endpoint, you may need a different access level. You can learn more here: https://developer.x.com/en/portal/product


"""
