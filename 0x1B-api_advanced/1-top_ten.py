#!/usr/bin/python3
import requests


def top_ten(subreddit):
    """ GET subreddit top 10 hot posts """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'user-agent': 'philsrequest'}
    r = requests.get(url, headers=headers)
    if (r.status_code is 404):
        print("None")
    elif 'data' not in r.json():
        print("None")
    else:
        r = r.json()
        for post in r['data']['children']:
            print(post['data']['title'])
