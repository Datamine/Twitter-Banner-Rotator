#!/usr/bin/env python2.7
"""
authenticates with twitter and updates the user's twitter banner
according to the current top item in a banner-queue stored in a text file.
"""

import twitter
import logging
from os import environ, listdir
from sys import stdout
from random import choice

logging.basicConfig(stream=stdout, level=logging.DEBUG)

def authenticate():
    """
    fetches the credentials stored in heroku config variables,
    uses them to authenticate with twitter
    """
    logging.info("Attempting to Authenticate!")

    consumer_key        = environ['twitter_consumer_key']
    consumer_secret     = environ['twitter_consumer_secret']
    access_token_key    = environ['twitter_access_token_key']
    access_token_secret = environ['twitter_access_token_secret']

    api = twitter.Api(consumer_key=consumer_key,
                      consumer_secret=consumer_secret,
                      access_token_key=access_token_key,
                      access_token_secret=access_token_secret)

    # this only executes if the above does not throw an error & crash
    logging.info("Authentication Successful!")
    return api

def main():
    logging.info("Starting run.py")

    logging.info("Selecting banner at random.")
    path_to_new_banner = choice(listdir("Banners/"))
    logging.info("Selected banner: " + path_to_new_banner)

    api = authenticate()

    logging.info("Attempting to Update Banner!")
    api.UpdateBanner(path_to_new_banner)

    # Again, this only executes if the above did not throw an error & crash
    logging.info("Banner updated successfully!")

if __name__ == '__main__':
    main()
