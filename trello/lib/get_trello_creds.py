from auth_helper import setup_service_wrapper, generate_access_tokens
from test_helper import get_secrets, get_configs


env = get_secrets()
api_key = env("API_KEY")
api_secret = env("API_SECRET")

trello = setup_service_wrapper(api_key, api_secret, get_configs())

generate_access_tokens(trello, api_key, api_secret)
