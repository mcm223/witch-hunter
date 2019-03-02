# Settings
from settings import settings

# Twitter API
from twython import Twython

# Bing Image Search
from azure.cognitiveservices.search.imagesearch import ImageSearchAPI
from msrest.authentication import CognitiveServicesCredentials

# Other stuff
import json

# Set up Twython
t = Twython(
        settings.twitter_app_key,
        settings.twitter_app_secret,
        settings.twitter_oauth_token,
        settings.twitter_oauth_token_secret)

# Set up Bing API
b = ImageSearchAPI(CognitiveServicesCredentials(settings.bing_key_one))

# Test out image search
res = b.images.search(query='witch')
first = res.value[0]
print("Total number of images: {}".format(len(res.value)))
print("First image thumbnail url: {}".format(first.thumbnail_url))
print("First image content url: {}".format(first.content_url))
