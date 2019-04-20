from trello.lib.helpers.data import get_subset_dict
from trello.test.helpers.comm_steps import get_first_board
from trello.test.schema.board import board_schema
from trello.test.schema.cards import card_schema
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

    def test_schema(self, api):
        '''
        All attributes should be presented in response and have valid types.
        '''
        board = get_first_board(api)
        response = api.get(f'/1/boards/{board["id"]}')
        assert board_schema().validate(response.json())

    def test_values(self, api):
        '''
        Specified attributes should have correct values.
        '''
        board = get_first_board(api)
        response = api.get(f'/1/boards/{board["id"]}')
        # print(">>>>>>>>> Prettifield output: ")
        # print(json.dumps(response.json(), indent=4, sort_keys=True))
        attrs = {
            'id',
            'name',
            'shortUrl',
            'url',
        }
        short_board = get_subset_dict(board, attrs)
        short_resp = get_subset_dict(response.json(), attrs)
        assert short_board == short_resp

    def test_value_with_field_option(self, api):
        '''
        GET /boards/{id}/{field}
        Where {field} - the field you'd like to receive.

        EXPECTED: only specified attribute should be in respond. I.e.:
        {
            "_value": "https://trello.com/b/9clNtU6v"
        }
        '''
        board = get_first_board(api)
        response = api.get(f'/1/boards/{board["id"]}/url')
        assert response.json()["_value"] == board["url"]


class TestGetBoardCardsIndex:
    '''
    GET /boards/{id}/cards

    This resource is a nested card resource.
    '''

    def test_status_code(self, api):
        board = get_first_board(api)
        response = api.get(f'/1/boards/{board["id"]}/cards')
        assert response.status_code == requests.codes['ok']

    def test_schema(self, api):
        '''
        All attributes should be presented in response and have valid types.
        '''
        board = get_first_board(api)
        response = api.get(f'/1/boards/{board["id"]}/cards')
        assert card_schema().validate(response.json()[0])

    def test_get_cards(self, api):
        board = get_first_board(api)
        response = api.get(f'/1/boards/{board["id"]}/cards')
        assert response.json()[0]["name"] == "Untitled card"
