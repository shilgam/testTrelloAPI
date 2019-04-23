from trello.lib.helpers.data import get_subset_dict
from trello.test.helpers.comm_steps import (get_first_board,
                                            get_board_by_id,
                                            post_board,
                                            put_board_by_id,
                                            delete_board_by_id)
from trello.test.fixtures.board import board_required_fields
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
        board = get_first_board(api)
        response = api.get(f'/1/boards/{board["id"]}/cards')
        assert card_schema().validate(response.json()[0])

    def test_get_cards(self, api):
        board = get_first_board(api)
        response = api.get(f'/1/boards/{board["id"]}/cards')
        assert response.json()[0]["name"] == "Untitled card"


class TestPostBoard:
    '''
    POST /boards

    Create a new board.
    '''

    def test_post_with_required_fields(self, api):
        board = board_required_fields()
        response = post_board(api, board)
        assert response.status_code == requests.codes['ok']

        # Board has specified fields and proper values
        attrs = board.keys()
        resp_subset = get_subset_dict(response.json(), attrs)
        assert resp_subset == board

        # # All other board attributes should have default values
        # resp_default_attrs = subtract_dict(response.json(), board)
        # print('\n>>>>>>  resp_default_attrs:     ')
        # print(json.dumps(resp_default_attrs, indent=4, sort_keys=True))
        #
        # expected_default_attrs = subtract_dict(board_default_fields(), board)
        # print(">>>>>>>>> expected_default_attrs: ")
        # print(json.dumps(expected_default_attrs, indent=4, sort_keys=True))
        # assert resp_subset == expected_default_attrs


class TestPutBoardById:
    '''
    PUT /boards/{id}

    Update an existing board by id
    '''

    # required fields only
    def test_put_with_required_fields(self, api):
        board_old_attrs = {"name": "created by post request"}
        response_post = post_board(api, board_old_attrs)
        board_id = response_post.json()["id"]

        board_attrs = board_required_fields()
        response_put = put_board_by_id(api, board_id, board_attrs)
        assert response_put.status_code == requests.codes['ok']

        # Board has specified fields and proper values
        resp_put_subset = get_subset_dict(response_put.json(), board_attrs.keys())
        assert resp_put_subset == board_attrs


class TestDeleteBoardById:
    '''
    DELETE /boards/{id}

    Delete a board.
    '''

    def test_delete_board(self, api):
        board_old_attrs = {"name": "created by post request"}
        response_post = post_board(api, board_old_attrs)
        board_id = response_post.json()["id"]
        response_delete = delete_board_by_id(api, board_id)
        assert response_delete.status_code == requests.codes['ok']

        # Board was succesfully desroyed
        response_get = get_board_by_id(api, board_id)
        assert response_get.status_code == requests.codes['not_found']
        assert response_get.text == 'The requested resource was not found.'
