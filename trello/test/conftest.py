from trello.lib.helpers.auth import get_auth_session, setup_service_wrapper
from trello.lib.helpers.steps import get_secrets, get_configs
import pytest


@pytest.fixture(scope="session")
def trello_session(request):
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
