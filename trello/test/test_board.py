from trello.lib.helpers.data import get_subset_dict
from trello.test.helpers.comm_steps import get_first_board
# import json
import requests


class TestGetBoardById:
    '''
    GET /boards/{id}
    Request a single board.
    '''

    def test_status_code(self, api):
        board = get_first_board(api)
        response = api.get(f'/1/boards/{board["id"]}')
        assert response.status_code == requests.codes['ok']

    def test_fetches_requested_data(self, api):
        '''
        Board attributes should has correct values.
        '''
        board = get_first_board(api)
        response = api.get(f'/1/boards/{board["id"]}')
        # print(">>>>>>>>> Prettifield output: ")
        # print(json.dumps(response.json(), indent=4))
        attrs = {
            'id',
            'name',
            'shortUrl',
            'url',
        }
        short_board = get_subset_dict(board, attrs)
        short_resp = get_subset_dict(response.json(), attrs)
        assert short_board == short_resp


class TestGetBoardCardsIndex:
    '''
    GET /boards/{id}/cards
    '''

    def test_get_cards(self, api):
        '''
        GET /boards/{id}/cards
        '''
        board = get_first_board(api)
        response = api.get(f'/1/boards/{board["id"]}/cards')
        assert response.json()[0]["name"] == "Untitled card"
