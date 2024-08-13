#!/usr/bin/python3
"""Queries Reddit API to get the number of subscribers in a subreddit."""

import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "python:subscribers_checker:v1.0 \
            (by /u/yourusername)"}
    try:
        response = requests.get(url, headers=headers, allow_redirect=False)
        if response.status_code == 200:
            data = response.json()
            subscribers = data["data"]["subscribers"]
            return subscribers
        else:
            return 0
    except Exception as e:
        return 0
