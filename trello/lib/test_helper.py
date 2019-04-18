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
    configs_filename = 'trello/app_configs.json'
    f = open(configs_filename)
    content = f.read()
    f.close()
    return json.loads(content)


def write_file(full_filename, text):
    '''
    Create/Update file with the text
    '''
    f = open(full_filename, 'w')
    f.write(text)
    f.close()
    print(f'\n>>> File "{full_filename}" was successfully updated')
