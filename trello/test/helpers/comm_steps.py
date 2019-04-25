import json
import logging

LOGGER = logging.getLogger(__name__)


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


def search(session, query):
    '''
    Search among boards, cards and members
    '''
    url = f'/1/search'
    querystring = {"query": f"{query}", "idBoards": "mine", "board_fields": "name,id", "boards_limit": "10", "card_fields": "all", "cards_limit": "10", "card_list": "false", "member_fields": "avatarHash,fullName,initials,username,confirmed"}
    response = session.get(url, params=querystring)
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


def find_board_or_create(session, board_name):
    '''
    Search for board with specified board {name} or create new one if not exist
    '''
    search_result = search(session, board_name).json()
    boards = search_result["boards"]

    if boards:
        board_id = boards[0]["id"]
        LOGGER.debug(f'>>> existing board was used')
        return get_board_by_id(session, board_id)
    else:
        LOGGER.debug(f'>>> new board was created')
        return post_board(session, {'name': board_name})
