"""
Module for using the web interface of Twitter's search.
"""

import tweepy
import requests

bearer_token = 'AAAAAAAAAAAAAAAAAAAAAOUX8gEAAAAAAMmhZDykj3k4o4vC0Nh7FIXWCoE%3DedqCn7hOBAOcFTGJprY4mbg5hx0uZuWFHEPDv7UZKYS9NnDpv7'

headers = {"Authorization": f"Bearer {bearer_token}"}
url = "https://api.x.com/2/users/by/username/xdevelopers"
response = requests.get(url, headers=headers)
print(response.json())