from trello.test.helpers.comm_steps import get_first_board


class TestBoard:

    def test_boards(self, trello_session):
        '''
        GET /boards/
        '''
        response = trello_session.get('/1/members/me/boards')
        assert response.json()[0]["name"] == "Untitled board"

    def test_get_boards_by_id(self, trello_session):
        '''
        GET /boards/{id}
        '''
        board = get_first_board(trello_session)
        response = trello_session.get(f'/1/boards/{board["id"]}')
        # print(">>>>>>>>> JSON output: ")
        # print("json: ", response.json())
        # print(">>>>>>>>> Prettifield output: ")
        # print(json.dumps(response.json(), indent=4))
        assert response.json()["name"] == "Untitled board"
