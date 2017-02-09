#!/usr/bin/env python2.7

import twitter
from os import environ

api = None

def authenticate():
    consumer_key        = environ['twitter_consumer_key']
    consumer_secret     = environ['twitter_consumer_secret']
    access_token_key    = environ['twitter_access_token_key']
    access_token_secret = environ['twitter_access_token_secret']

    global api
    api = twitter.Api(consumer_key=consumer_key,
                      consumer_secret=consumer_secret,
                      access_token_key=access_token_key,
                      access_token_secret=access_token_secret)

    print "Authentication successful!"
    return None



def main():
    print "Starting run.py."
    authenticate()



if __name__=='__main__':
    main()
