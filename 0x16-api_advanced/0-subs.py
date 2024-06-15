#!/usr/bin/python3
'''function to query subreddit'''
import requests


def number_of_subscribers(subreddit):

    # # url = "https://www.reddit.com/r/{:s}/about.json".format(subreddit)
    # # headers = {'User-Agent': 'MyBot/0.0.1'}

    # req = requests.get(
    #     "https://www.reddit.com/r/{:s}/about.json".format(subreddit),
    #     headers={"User-Agent": "Custom"}, timeout=10, allow_redirects=False
    # )

    # if req.status_code == 200:
    #     return req.json().get("data").get("subscribers")
    # return 0
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = "https://www.reddit.com/r/{:s}/about.json".format(subreddit)

    try:
        # Make a GET request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)
        # Check if the response status code is 200 (OK)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            # Return the number of subscribers
            return data['data']['subscribers']
        else:
            # If the subreddit is invalid or other errors occur, return 0
            return 0
    except requests.RequestException:
        # In case of network errors or other request issues, return 0
        return 0
