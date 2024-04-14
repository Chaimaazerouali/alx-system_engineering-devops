#!/usr/bin/python3
""" How many subs? """
import requests


def number_of_subscribers(subreddit):
""" Returns subscriber count of subreddit or 0 """
user_agent = '0x16-api_advanced'
url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": user_agent}
    response = requests.get(url, headers=headers, allow_redirects=False)
     response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
