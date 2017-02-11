# Twitter-Banner-Rotator

This project contains a Python script for updating your Twitter banner picture. By deploying this script (and a set of
images) to Heroku, and setting a scheduler to run the script once a day, your Twitter banner picture will get 
automatically updated once a day --  selecting one at random from a set of images you provided.

## Instructions 

0. Clone this repository: in your terminal, type `git clone https://github.com/Datamine/Twitter-Banner-Rotator` and `cd` into it.
1. Go on [Heroku](www.heroku.com), make an account if necessary, and make a new app. 
    Your app has a URL. For example, on your app dashboard, if you hit `open app`, it'll take you to a website: 
    `https://example.herokuapp.com`. The part between the `https://` and `.herokuapp.com` is your app's name 
    (in this case, that's "example"). It's a unique identifier.
2. Download the [Heroku Toolbelt](https://devcenter.heroku.com/articles/getting-started-with-python#set-up)
    and log in on the terminal.
3. In your local repository, type `heroku git:remote -a <your app name here>`. 
    See [instructions](https://devcenter.heroku.com/articles/git#creating-a-heroku-remote) for adding a heroku remote
    to your git repository.
4. Back on the Heroku app dashboard, on app addons, add the `scheduler`. 
    Set it to schedule `python run.py` once a day. (Or hourly/every 10 minutes depending on the level of skittish pizzazz that you want.)
3. Go on Twitter. [Make a new app](https://apps.twitter.com/) or use one that you've created previously. Obtain: 
    - `consumer_key`
    - `consumer_secret` 
    - `access_token_key`
    - `access_token_secret`
4. On the Heroku Dashboard for your app, set four config variables for the credentials
    obtained above. (It may be worth opening up the Python REPL and using the `twitter`
    library to authenticate with those credentials, just to make sure that it works.
    Note, as per `requirements.txt`, that this app uses the `python-twitter` library,
    not the `twitter` library. You'll want to `pip install python-twitter`. If you run
    into a naming conflict, I suggest you use a [virtual environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/).)
5. Download the pictures you like, and put them in the `Banners/` folder.
6. To deploy your application to heroku, type:
    
    ```
    git add .
    git commit -m "<your commit message here>"
    git push heroku master
    ```
    
7. You can then view the logs either on app dashboard, or using `heroku logs --app <your app name here> --tail` from the command line.
    Check the logs to make sure everyhing works as desired. 

I suggest changing your scheduled task's frequency to every 10 minutes in the start, so you can easily verify that it works,
then changing it to daily thereafter.

## Extensions

The following are all quite straight-forwardly possible:

- If you want to rotate among lots of images, you don't need to store them all
    in a `Banners/` folder. That can get cumbersome. Instead, you can upload them
    to an external image host, e.g. [imgur](www.imgur.com), and let some file, e.g. `banners_list.txt`
    be a list of URLs to your banner images. Then you can use `urllib.urlretrieve`
    to download the image to a temporary file, upload the file to Twitter, and 
    delete the file afterwards.

- In line with the suggestion above, you could even randomly retrieve nice images
    to use as backgrounds. I am reminded of Adam 
    Cadre's [stochastic planet](http://stochasticplanet.tumblr.com/)
    project.

## Issues & Notes

- `.gif` files currently fail when you try to upload them. 
    This appears to be a problem in the `python-twitter` library.
    See the [issue here](https://github.com/bear/python-twitter/issues/435).
    You can correct this in the meantime by using ImageMagic to convert any gifs to jpg.

- At first this script was written to cycle through a set of images. However, this relied on 
    the script being able to write to a file to denote the current position in the cycle,
    which is not possible because Heroku's filesystem is read-only. I have been led
    to believe that the best alternative is to attach a small database to store
    that index, but this seems like a cumbersome solution, especially if I'm releasing
    this as a tool for other people to use. It'd be better to migrate
    the entire setup to AWS.

- Since the script selects a banner from a set of pictures at random, it's currently
    possible for the new banner to be the same as the one currently already chosen.
    This happens on an update with probability 1/n, where n is the number of pictures
    in the `Banners` directory. There are some tricks that could be employed to
    prevent this, but I've currently deemed this nonessential.

-----

You can also read about this project on [my blog](http://johnloeber.com/docs/twitter-rotate.html).
