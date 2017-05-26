#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
    """ GET subscriber count of a given subreddit """
    url = "http://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'user-agent': 'philsrequest'}
    r = requests.get(url, headers=headers)
    if (r.status_code is 302 or r.status_code is 404):
        return 0
    r = r.json()
    if ('error' in r):
        return 0
    elif ('subscribers' in r['data']):
        return r['data']['subscribers']
    else:
        return 0
