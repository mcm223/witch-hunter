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




# Grab an image from Bing API
def getImage():
    # Fetch results of search
    s = b.images.search(SEARCH_TERM)

    # Pick a random result 
    pic = s.value[random.randint(1,len(s.value))]

    # Return the thumbnail path
    return pic.thumbnail_url

# Do the stuff
print(getImage())
