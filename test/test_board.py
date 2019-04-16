from lib.auth_helper import get_auth_session, setup_service_wrapper
from lib.test_helper import get_secrets, get_configs
import json

env = get_secrets()

trello = setup_service_wrapper(
    env("API_KEY"),
    env("API_SECRET"),
    get_configs())

session = get_auth_session(trello, env("OAUTH_VERIFIER"))


def test_board_name():
    r = session.get('/1/members/me/boards')
    print(">>>>>>>>> JSON output: ")
    print("json: ", r.json())

    print(">>>>>>>>> Prettifield output: ")
    print(json.dumps(r.json(), indent=4))
    assert r.json()[0]["name"] == "Untitled board"
