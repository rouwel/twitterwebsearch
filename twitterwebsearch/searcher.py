"""
Module for using the web interface of Twitter's search.
"""

import tweepy
import requests


bearer_token = 'AAAAAAAAAAAA5hx0uZuWFHEPDv7UZKYS9NnDpv7'

headers = {"Authorization": f"Bearer {bearer_token}"}
url = "https://api.x.com/2/users/by/username/xdevelopers"
response = requests.get(url, headers=headers)
print(response.json())

"""
Output
C:\Users\FAAFO\twitterwebsearch\twitterwebsearch>python searcher.py
{'account_id': 2036532529868496897, 'title': 'CreditsDepleted', 'detail': 'Your enrolled account [2036532529868496897] does not have any credits to fulfill this request.', 'type': 'https://api.twitter.com/2/problems/credits'}

"""


