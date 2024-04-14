#!/usr/bin/python3
"""Script that queries subscribers on a given Reddit subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """Returns subscriber count of subreddit or 0
    """
    # set custom user-agent
    url = 'https://www.reddit.com/r/{}.json'.format(subreddit)

    # custom user-agent avoids request limit
    headers = {'User-Agent':"Mozilla/5.0"}

    r = requests.get(url, headers=headers, allow_redirects=False)

    if r.status_code != 200:
        return 0

    # load response unit from json
    data = r.json()['data']
    # extract list of pages
    pages = data['children']
    # extract data from first page
    page_data = pages[0]['data']
    # return number of subreddit subs
    return page_data['subreddit_subscribers']
