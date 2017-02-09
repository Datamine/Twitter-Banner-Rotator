# Twitter-Banner-Rotator
Rotates your Twitter banner picture every 24 hours!

## Instructions 

1. Go on Heroku, make a new app.
2. On app addons, add the `scheduler`. Set it to schedule `python run.py` once a day.
3. Go on Twitter. Make a new app. Obtain: 
    - `consumer_key`
    - `consumer_secret` 
    - `access_token_key`
    - `access_token_secret`
4. On the Heroku Dashboard for your app, set four config variables for the credentials
    obtained above. (It may be worth opening up the Python REPL and using the `twitter`
    library to authenticate with those credentials, just to make sure that it works.)
5. Download the pictures you like, and put them in the `Banners/` folder.
6. Write `ls Banners/ > banner_list.txt` to store the filenames for 
    your banners in the `banner_list` file.

## Extensions

The following are all quite straight-forwardly possible:

- If you want to rotate among lots of images, you don't need to store them all
    in a `Banners/` folder. That can get cumbersome. Instead, you can upload them
    to an external image host, e.g. [imgur](www.imgur.com), and let `banners_list.txt`
    be a list of URLs to your banner images. Then you can use `urllib.urlretrieve`
    to download the image to a temporary file, upload the file to Twitter, and 
    delete the file afterwards.

- In line with the suggestion above, you could even randomly retrieve nice images
    to use as backgrounds. I am reminded of Adam 
    Cadre's [stochastic planet](http://stochasticplanet.tumblr.com/)
    project.

## Issues

- `.gif` files currently fail when you try to upload them. 
    This appears to be a problem in the `python-twitter` library.
    See the [issue here](https://github.com/bear/python-twitter/issues/435).
    You can correct this in the meantime by using ImageMagic to convert any gifs to jpg.
