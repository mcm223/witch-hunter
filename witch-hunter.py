# Local classes
from settings import settings
from content import content

# Twitter API
from twython import Twython

# Bing Image Search
from azure.cognitiveservices.search.imagesearch import ImageSearchAPI
from msrest.authentication import CognitiveServicesCredentials

# Other stuff
import json
import random
from datetime import datetime
from datetime import timezone
from datetime import timedelta

# Declare constants
SEARCH_TERM = 'witch face'
TIME_WINDOW = 24

# Set up Twython
t = Twython(
        settings.twitter_app_key,
        settings.twitter_app_secret,
        settings.twitter_oauth_token,
        settings.twitter_oauth_token_secret)

# Set up Bing API
b = ImageSearchAPI(CognitiveServicesCredentials(settings.bing_key_one))

# Search recent tweets for spooky content
def witchHunt():
    # Get user's timeline
    tl =  t.get_user_timeline(
            screen_name='realDonaldTrump',
            include_rts='true',
            count='20',
            tweet_mode='extended')

    # HUNT FOR WITCHES
    for tweet in tl:
        # If it is a retweet, use the original untruncated text
        if 'retweeted_status' in tweet.keys():
            tweet["full_text"] = tweet["retweeted_status"]["full_text"]
        
        # Process the text
        text = tweet["full_text"].lower()

        # Log the tweet time
        time = datetime.strptime(tweet["created_at"], '%a %b %d %H:%M:%S %z %Y')

        # First check if the tweet mentions witch
        if text.find("witch") == -1:
            continue
        # Then enforce an hour window so I don't respond to the same tweet twice
        if (datetime.now(timezone.utc) - timedelta(hours=TIME_WINDOW)) > time:
            continue
        # If all the criteria match, then we've found a witch!
        else:
            print("Found one!")
            quoteTweet(tweet)
            break # Only respond to one tweet to prevent spamming
        
def replyToTweet(tweet):
    print(tweet["full_text"])

def quoteTweet(tweet):
    # Create permalink so I can quote the tweet
    link = 'https://twitter.com/' + tweet['user']['screen_name'] + '/status/' + tweet['id_str']
    print("Link to quoted tweet: " + link)

    # Fetch a random phrase for the tweet itself
    tweet_text = content.statuses[random.randint(0,len(content.statuses)-1)]
    print("The tweet text is: " + tweet_text)

    # Send the tweet
    t.update_status(
            status=tweet_text,
            attachment_url=link,
            tweet_mode='extended')

    print('Tweet sent!')

# Grab an image from Bing API
def getImage():
    # Fetch results of search
    s = b.images.search(SEARCH_TERM)

    # Pick a random result 
    pic = s.value[random.randint(0,len(s.value))]

    # Return the thumbnail path
    return pic.thumbnail_url

# Do the stuff
witchHunt()
