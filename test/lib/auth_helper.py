from rauth import OAuth1Service


def setup_service_wrapper(consumer_key, consumer_secret, configs):
    '''
    Set up a OAuth 1.0 service wrapper
    '''
    return OAuth1Service(
        name=configs["trello_service_name"],
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        request_token_url=configs["request_token_url"],
        access_token_url=configs["access_token_url"],
        authorize_url=configs["authorize_url"],
        base_url=configs["base_url"])


def get_request_token(session):
    '''
    Return a request token pair.
    '''
    request_token, request_token_secret = session.get_request_token()
    return request_token, request_token_secret


def get_authorize_url(session):
    '''
    Returns a formatted authorize URL.
    '''
    request_token = get_request_token(session)[0]
    params = {'expiration': 'never'}
    authorize_url = session.get_authorize_url(request_token, **params)
    return authorize_url


def get_oauth_verifier(session):
    '''
    Go through the authentication flow. Trello will give you a PIN to enter.
    '''
    authorize_url = get_authorize_url(session)
    print('STEP 1. Visit this URL in your browser: {url}'.format(url=authorize_url))
    pin = input('STEP 2. Enter PIN from browser: ')
    return pin


def generate_access_tokens(session, consumer_key, consumer_secret):
    '''
    Generate new set of access tokens and print them out
    '''
    oauth_verifier = get_oauth_verifier(session)

    print("\n  >>>>>>>> Here is the new set of access tokens: <<<<<<<<<")
    print("API_KEY=", consumer_key, sep="")
    print("API_SECRET=", consumer_secret, sep="")
    request_token, request_token_secret = session.get_request_token()
    print("REQUEST_TOKEN=", request_token, sep="")
    print("REQUEST_TOKEN_SECRET=", request_token_secret, sep="")
    print("OAUTH_VERIFIER=", oauth_verifier, sep="")
    print("\nSTEP 3. Copy-paste access tokens above into your '.env' file or pass them as env variables separately")


def get_auth_session(session, oauth_verifier):
    '''
    Intialize a new authenticated session with the access tokens.
    '''
    request_token, request_token_secret = session.get_request_token()
    data = {'oauth_verifier': oauth_verifier}

    return session.get_auth_session(
        request_token,
        request_token_secret,
        method='POST',
        data=data)
