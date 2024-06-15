#!/usr/bin/python3
'''function to query subreddit'''
import requests


def number_of_subscribers(subreddit):

    # url = "https://www.reddit.com/r/{:s}/about.json".format(subreddit)
    # headers = {'User-Agent': 'MyBot/0.0.1'}

    req = requests.get(
        "https://www.reddit.com/r/{:s}/about.json".format(subreddit),
        headers={"User-Agent": "Custom"}, timeout=10, allow_redirects=False
    )

    if req.status_code == 200:
        return req.json().get("data").get("subscribers")
    return 0
