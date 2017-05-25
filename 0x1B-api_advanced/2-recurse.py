#!/usr/bin/python3
import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    GET all titles of hot articles for a given subreddit.
    Store results in hot_list provided as default to method.
    Requires recursive request stores.
    """
    if (after is None):
        return hot_list

    if (len(hot_list) == 0):
        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    else:
        url = "https://www.reddit.com/r/{}/hot.json?after={}".format(
            subreddit, after)
    headers = {'user-agent': 'philsrequest'}

    r = requests.get(url, headers=headers)
    if (r.status_code is 404):
        return None
    elif 'data' not in r.json():
        return None
    else:
        r = r.json()
        for post in r['data']['children']:
            hot_list.append(post['data']['title'])

    after = r['data']['after']
    return recurse(subreddit, hot_list, after)
