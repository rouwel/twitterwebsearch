"""
Module for using the web interface of Twitter's search.
"""

import tweepy

consumer_key = 'dwRRlaVZj7FYgyhnDM4UlY8QT'
consumer_secret = 'IzoPhQvaGpn5d05OsHVFvyoiSd4b0PZ66bbN0mlzBnjTzrzySm'
access_token = '2036531799300644864-bPqj6wL4G1vgUCpqiBDX3CPTkCojuU'
access_token_secret = 'hmfPuAupb6AYq3L70uEti7DyWqKcKKjlrRiZygE9uNhyH'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAOUX8gEAAAAAAMmhZDykj3k4o4vC0Nh7FIXWCoE%3DedqCn7hOBAOcFTGJprY4mbg5hx0uZuWFHEPDv7UZKYS9NnDpv7'

client =  tweepy.Client(
    bearer_token=bearer_token,
    consumer_key=consumer_key,
    consumer_secret= consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

test_test = "Hello world? "

try:
    response = client.create_tweet(test_test)
    print(f"Tweet posted successfully! URL: https://twitter.com/user/status/{response.data['id']}")
except tweepy.errors.Forbidden as e:
    print(f"Error posting tweet: {e}")
    print("Check if your Access Token has 'Read and Write' permissions.")
except Exception as e:
    print(f"An error occurred: {e}")



