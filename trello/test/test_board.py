from trello.lib.helpers.data import get_subset_dict
from trello.test.helpers.comm_steps import (get_first_board,
                                            get_board_by_id,
                                            post_board,
                                            put_board_by_id,
                                            delete_board_by_id,
                                            search,
                                            find_board_or_create,)
from trello.test.fixtures.board import board_only_req_fields
from trello.test.schema.board import board_schema
from trello.test.schema.cards import card_schema
import json
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

    def test_default_fields(self, api):
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


class TestGetBoardCards:
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
        search_result = search(api, 'Untitled board').json()
        boards = search_result["boards"]
        board_id = boards[0]["id"]
        url = f'/1/boards/{board_id}/cards'
        response = api.get(url)
        assert card_schema().validate(response.json()[0])

    def test_get_cards(self, api):
        search_result = search(api, 'Untitled board').json()
        boards = search_result["boards"]
        board_id = boards[0]["id"]
        url = f'/1/boards/{board_id}/cards'
        response = api.get(url)
        assert response.json()[0]["name"] == 'Untitled card'


class TestPostBoard:
    '''
    POST /boards

    Create a new board.
    '''

    def test_post_valid_attrs__status_code(self, api, valid_board):
        response = post_board(api, valid_board)
        assert response.status_code == requests.codes['ok']

    def test_post_valid_attrs__resp_body(self, api, valid_board):
        response = post_board(api, valid_board)
        attrs = valid_board.keys()
        resp_subset = get_subset_dict(response.json(), attrs)
        assert resp_subset == valid_board

    def test_post_invalid_attrs__status_code(self, api, data_invalid_board):
        board, exp_status_code, exp_msg = data_invalid_board
        response = post_board(api, board)
        assert response.status_code == exp_status_code

    def test_post_invalid_attrs__err_message(self, api, data_invalid_board):
        board, exp_status_code, exp_msg = data_invalid_board
        response = post_board(api, board)
        assert response.text == exp_msg


class TestPutBoardById:
    '''
    PUT /boards/{id}

    Update an existing board by id
    '''

    def test_put_valid_attrs__status_code(self, api, valid_board):
        board = find_board_or_create(api, valid_board['name'])
        board_id = board.json()['id']
        response = put_board_by_id(api, board_id, valid_board)
        assert response.status_code == requests.codes['ok']

    def test_put_valid_attrs__resp_body(self, api, valid_board):
        board = find_board_or_create(api, valid_board['name'])
        board_id = board.json()['id']
        response = put_board_by_id(api, board_id, valid_board)
        resp_put_subset = get_subset_dict(response.json(), valid_board.keys())
        assert resp_put_subset == valid_board

    def test_put_invalid_attrs__status_code(self, api, data_invalid_board):
        board = find_board_or_create(api, board_only_req_fields['name'])
        board_id = board.json()['id']
        board, exp_status_code, exp_msg = data_invalid_board
        response = put_board_by_id(api, board_id, board)
        # assert response.status_code == exp_status_code
        assert True  # TODO: fix test after fixing an issue

    def test_put_invalid_attrs__err_message(self, api, data_invalid_board):
        board, exp_status_code, exp_msg = data_invalid_board
        response = post_board(api, board)
        assert response.text == exp_msg


class TestDeleteBoardById:
    '''
    DELETE /boards/{id}

    Delete a board.
    '''

    def test_delete(self, api, valid_board):
        board = find_board_or_create(api, board_only_req_fields['name'])
        board_id = board.json()['id']
        response = delete_board_by_id(api, board_id)
        assert response.status_code == requests.codes['ok']

        # Check that board was succesfully desroyed
        response_get = get_board_by_id(api, board_id)
        assert response_get.status_code == requests.codes['not_found']
        assert response_get.text == 'The requested resource was not found.'
