#!/usr/bin/python3
'''function to query subreddit'''
import requests


def number_of_subscribers(subreddit):

    # url = "https://www.reddit.com/r/{:s}/about.json".format(subreddit)
    # headers = {'User-Agent': 'MyBot/0.0.1'}

    req = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers={"User-Agent": "Custom"}
    )

    if req.status_code == 200:
        return req.json().get("data").get("subscribers")
    else:
        return 0

    # try:
    #     response = requests.get(url, headers=headers, allow_redirects=False)
    #     if response.status_code == 200:
    #         data = response.json()
    #         subscribers = data['data']['subscribers']
    #         return subscribers
    #     return 0  # Invalid subreddit or other error
    # except Exception as e:
    #     print(f"Error: {e}")
    #     return 0  # Return 0 if an exception occurs
