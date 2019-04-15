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


request_token = env("REQUEST_TOKEN")
request_token_secret = env("REQUEST_TOKEN_SECRET")
pin = env("PIN")


# Exchange the authorized request token for an authenticated OAuth1Session:
session = trello.get_auth_session(
    request_token,
    request_token_secret,
    method='POST',
    data={'oauth_verifier': pin})


def test_board_name():
    r = session.get('/1/members/me/boards')
    print(">>>>>>>>> JSON output: ")
    print("json: ", r.json())

    print(">>>>>>>>> Prettifield output: ")
    print(json.dumps(r.json(), indent=4))
    assert r.json()[0]["name"] == "Untitled board"
