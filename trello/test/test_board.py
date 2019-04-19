from trello.test.helpers.comm_steps import get_first_board


class TestBoard:

    def test_boards(self, api):
        '''
        GET /boards/
        '''
        response = api.get('/1/members/me/boards')
        assert response.json()[0]["name"] == "Untitled board"

    def test_get_boards_by_id(self, api):
        '''
        GET /boards/{id}
        '''
        board = get_first_board(api)
        response = api.get(f'/1/boards/{board["id"]}')
        # print(">>>>>>>>> JSON output: ")
        # print("json: ", response.json())
        # print(">>>>>>>>> Prettifield output: ")
        # print(json.dumps(response.json(), indent=4))
        assert response.json()["name"] == "Untitled board"
