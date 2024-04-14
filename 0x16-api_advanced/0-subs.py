#!/usr/bin/python3
""" How many subs? """
import requests

def number_of_subscribers(subreddit):
 """ Returns subscriber count of subreddit or 0 """
url = 'https://www.reddit.com/r/{}.json'.format(subreddit)
headers = {'User-Agent': 'Mozilla/10.0/API'}
r = requests.get(url, headers=headers, allow_redirects=False)

if r.status_code == 200:
data = r.json().get('data', {})
pages = data.get('children', [])
if pages:
page_data = pages[0]['data']
return page_data.get('subreddit_subscribers', 0)
return 0

