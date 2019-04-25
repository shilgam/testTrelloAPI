from trello.lib.helpers.auth import get_auth_session, setup_service_wrapper
from trello.lib.helpers.steps import get_secrets, get_configs
from trello.test.fixtures.board import (board_only_req_fields,
                                        board_optional_fields)
# import json
import pytest
import requests


# Session scope fixtures

@pytest.fixture(scope="session")
def api(request):
    '''
    Create one Trello API session per test session.
    '''
    env = get_secrets()
    trello = setup_service_wrapper(
        env("API_KEY"),
        env("API_SECRET"),
        get_configs())
    session = get_auth_session(trello, env("OAUTH_VERIFIER"))
    return session


# VALID CASES

board_w_special_symbols = {'name': '\n !@#$%^&*()_+-= 12 "|\\}]:;.,`~_+-='}
board_w_short_name = {'name': '1'}


# Note: Specifying 'params' option causes multiple invocations of the fixture
# function and all of the tests using it.
@pytest.fixture(params=[
    board_only_req_fields,
    board_optional_fields,
    board_w_special_symbols,
    board_w_short_name])
def valid_board(request):
    '''
    Board fixture with valid attributes
    '''
    return request.param


# INVALID CASES

board_w_o_name_field = {'name': ''}
board_w_o_any_input = {}
board_w_inv_permLevel = {'name': 'invalid prefs_permissionLevel', 'prefs_permissionLevel': 'not_exist'}


@pytest.fixture(params=[
    (board_w_o_name_field,  requests.codes['bad_request'], 'invalid value for name'),
    (board_w_o_any_input,   requests.codes['bad_request'], 'invalid value for name'),
    (board_w_inv_permLevel, requests.codes['bad_request'], 'invalid value for prefs_permissionLevel')])
def data_invalid_board(request):
    '''
    Test data with:
    - board fixture with invalid attributes
    - expected response status_code
    - expected response message
    '''
    return request.param
