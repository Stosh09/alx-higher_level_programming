#!/usr/bin/python3
"""Sends a POST request to a given URL with a given email.

Usage: ./6-post_email.py <URL> <email>
  - Displays the body of the response.
"""
import sys
import requests


if __name__ == '__main__':

    vals = {"email": sys.argv[2]}
    url = sys.argv[1]
    res = requests.post(url, data=vals)
    print(res.text)
