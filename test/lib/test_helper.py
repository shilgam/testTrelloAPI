from environs import Env
import json


def get_secrets():
    '''
    Get secrets from '.env' file or environment variables (if available)
    '''
    env = Env()
    env.read_env()  # read .env file, if it exists
    return env


def get_configs():
    '''
    Get configs from json file
    '''
    configs_filename = 'app_configs.json'
    f = open(configs_filename)
    return json.loads(f.read())
