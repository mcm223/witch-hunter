# Settings
from settings import settings

# Twitter API
from twython import Twython

# Bing Image Search
from azure.cognitiveservices.search.imagesearch import ImageSearchAPI
from msrest.authentication import CognitiveServicesCredentials

# Other stuff
import json
import random

# Declare constants
SEARCH_TERM = 'witch face'

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
            count='5',
            tweet_mode='extended')

    # WITCH HUNT
    for tweet in tl:
        # If it is a retweet, use the original untruncated text
        if 'retweeted_status' in tweet.keys():
            tweet["full_text"] = tweet["retweeted_status"]["full_text"]
        text = tweet["full_text"]
        text = text.lower()
        if text.find("witch") == -1:
            continue
        else:
            print("Found one!")
            respondToTweet(tweet)
            break # Only respond to one tweet to prevent spamming
        
def respondToTweet(tweet):
    print(tweet["full_text"])

# Grab an image from Bing API
def getImage():
    # Fetch results of search
    s = b.images.search(SEARCH_TERM)

    # Pick a random result 
    pic = s.value[random.randint(1,len(s.value))]

    # Return the thumbnail path
    return pic.thumbnail_url

# Do the stuff
witchHunt()
