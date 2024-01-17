#!/usr/bin/env python3
import requests
"""this is my import"""


def number_of_subscribers(subreddit):
    """
    my function to count subscribers
    """
    api_url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'MyBot/1.0'}

    try:
        response = requests.get(api_url, headers=headers)

        if response.status_code == 200:
            subreddit_data = response.json()
            return subreddit_data['data']['subscribers']
        else:
            return 0
    except requests.RequestException as e:
        print(f"Error: {e}")
        return 0
