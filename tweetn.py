from twython import Twython
import requests

from auth0 import(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret)

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret)

url = 'https://icanhazdadjoke.com/'
headers = {'Accept': 'application/json'}
hashtags = ' #dadjoke #joke #funny #icanhazdadjoke'
joke_msg = requests.get(url, headers=headers).json().get('joke') + hashtags
twitter.update_status(status=joke_msg)
print('Tweeted: '+joke_msg)
