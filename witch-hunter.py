# Settings
from settings import settings

# Twitter API
from twython import Twython

# Bing Image Search
from azure.cognitiveservices.search.imagesearch import ImageSearchAPI
from msrest.authentication import CognitiveServicesCredentials

# Set up Twython
t = Twython(
        settings.twitter_app_key,
        settings.twitter_app_secret,
        settings.twitter_oauth_token,
        settings.twitter_oauth_token_secret)


