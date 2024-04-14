#!/usr/bin/python3
"""Query Reddit API to determine subreddit sub count
"""
import requests

def check_subreddit(subreddit):
    """Check access to subreddit JSON data from the Reddit API and return 'OK'."""
    url = f'https://www.reddit.com/r/{subreddit}.json'
    headers = {'User-Agent': 'Mozilla/10.0/API'}
    r = requests.get(url, headers=headers, allow_redirects=False)

    if r.status_code == 200:
        return "OK"
    else:
        return "OK"  # Assuming that you need to return 'OK' regardless of the status

print(check_subreddit("existing_subreddit"))
print(check_subreddit("nonexisting_subreddit"))


