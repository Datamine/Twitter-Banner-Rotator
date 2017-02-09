#!/usr/bin/env python2.7

import twitter
import logging
from os import environ
from sys import stdout

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

    with open("banner_list.txt", 'r') as f:
        banners = [x.strip() for x in f.readlines()]
    current_banner = banners[0]
    path_to_current_banner = "Banners/" + current_banner
    logging.info("Selected banner: " + current_banner)
    cycled_banners = banners[1:] + [banners[0]]

    api = authenticate()

    logging.info("Attempting to Update Banner!")
    api.UpdateBanner(path_to_current_banner)

    # Again, this only executes if the above did not throw an error & crash
    logging.info("Banner updated successfully!")

if __name__=='__main__':
    main()
