from environs import Env
from rauth import OAuth1Service
import json


env = Env()
env.read_env()  # read .env file, if it exists


configs_filename = 'app_configs.json'
f = open(configs_filename)
configs = json.loads(f.read())


trello = OAuth1Service(
    name='testTrelloAPI',
    consumer_key=env("API_KEY"),
    consumer_secret=env("API_SECRET"),
    request_token_url=configs["request_token_url"],
    access_token_url=configs["access_token_url"],
    authorize_url=configs["authorize_url"],
    base_url=configs["base_url"])


# get an OAuth 1.0 request token:
request_token, request_token_secret = trello.get_request_token()
print(">>>> request_token:        ", request_token)
print(">>>> request_token_secret: ", request_token_secret)


# Go through the authentication flow. Trello will give you a PIN to enter.
params = {'expiration': 'never'}
authorize_url = trello.get_authorize_url(request_token, **params)

print('Visit this URL in your browser: {url}'.format(url=authorize_url))
pin = input('Enter PIN from browser: ')
print(">>>> pin:                  ", pin)
