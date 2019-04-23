import json


def get_first_board(session):
    response = session.get('/1/members/me/boards')
    # print(">>>>>>>>> Prettifield output: ")
    # print(json.dumps(response.json(), indent=4, sort_keys=True))
    board = response.json()[0]
    return board


def get_board_by_id(session, id):
    '''
    Peform GET request to fetch existing board by board's {id}
    '''
    url = f'/1/boards/{id}'
    response = session.get(url)
    return response


def post_board(session, board_attrs):
    '''
    Peform POST request to create new board
    '''
    url = "/1/boards"
    return session.post(url, data=board_attrs)


def put_board_by_id(session, board_id, board_attrs):
    '''
    Peform PUT request to update existing board
    '''
    url = f'/1/boards/{board_id}'
    return session.put(url, data=board_attrs)


def delete_board_by_id(session, board_id):
    '''
    Peform PUT request to destroy existing board
    '''
    url = f'/1/boards/{board_id}'
    return session.delete(url)
