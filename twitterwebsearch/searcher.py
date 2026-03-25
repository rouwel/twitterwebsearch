"""
Module for using the web interface of Twitter's search.
"""

import tweepy

consumer_key = 'dwRRlaVZj7FYgyhnDM4UlY8QT'
consumer_secret = 'IzoPhQvaGpn5d05OsHVFvyoiSd4b0PZ66bbN0mlzBnjTzrzySm'
access_token = '2036531799300644864-bPqj6wL4G1vgUCpqiBDX3CPTkCojuU'
access_token_secret = 'hmfPuAupb6AYq3L70uEti7DyWqKcKKjlrRiZygE9uNhyH'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAOUX8gEAAAAAAMmhZDykj3k4o4vC0Nh7FIXWCoE%3DedqCn7hOBAOcFTGJprY4mbg5hx0uZuWFHEPDv7UZKYS9NnDpv7'

auth = tweepy.OAuth1UserHandler(
    f"API /{consumer_key}" , f"API / {consumer_secret}", f"{access_token}", f"{access_token_secret}"
)
try:
    api = tweepy.API(auth)
    print("Achieved login")
except:
    print("login failed")
