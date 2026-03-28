"""
Module for using the web interface of Twitter's search.
"""

import tweepy
import requests

consumer_key = 'dwRRlaVZj7FYgyhnDM4UlY8QT'
consumer_secret = 'IzoPhQvaGpn5d05OsHVFvyoiSd4b0PZ66bbN0mlzBnjTzrzySm'
access_token = '2036531799300644864-bPqj6wL4G1vgUCpqiBDX3CPTkCojuU'
access_token_secret = 'hmfPuAupb6AYq3L70uEti7DyWqKcKKjlrRiZygE9uNhyH'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAOUX8gEAAAAAAMmhZDykj3k4o4vC0Nh7FIXWCoE%3DedqCn7hOBAOcFTGJprY4mbg5hx0uZuWFHEPDv7UZKYS9NnDpv7'

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
