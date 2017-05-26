#!/usr/bin/python3
import re
import requests


def count_words(subreddit, word_list):
    """
    GET the word count for each word in word_list.
    Print results in descending order by the count, not the title.
    If no posts match or subreddit is invalid, print a newline.
    If a word has no matches, skip and do not print it.
    """
    storage = {word.lower(): 0 for word in word_list}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'user-agent': 'philsrequest'}

    r = requests.get(url, headers=headers)
    if (r.status_code == 404 or 'data' not in r.json()):
        return None
    else:
        while (1):
            r = r.json()
            for post in r['data']['children']:
                tmp = post['data']['title'].split()
                for word in tmp:
                    if word.lower() in storage.keys():
                        storage[word.lower()] += 1

            after = r['data']['after']
            if (after is None):
                break
            r = requests.get("{}?after={}".format(url, after), headers=headers)

    storage = [(k, storage[k]) for k in
               sorted(storage, key=storage.get, reverse=True)]

    if len(storage) == 0:
        print("")
    else:
        for k, v in storage:
            if (v > 0):
                print("{}: {:d}".format(k, v))
