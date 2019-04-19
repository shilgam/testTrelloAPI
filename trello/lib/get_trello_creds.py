from helpers.auth import setup_service_wrapper, generate_access_tokens
from helpers.steps import get_secrets, get_configs, write_file


env = get_secrets()
api_key = env("API_KEY")
api_secret = env("API_SECRET")

trello = setup_service_wrapper(api_key, api_secret, get_configs())

secrets = generate_access_tokens(trello, api_key, api_secret)

# update '.env' file with new secrets
write_file('.env', "\n".join(secrets))
