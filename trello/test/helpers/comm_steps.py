def get_first_board(session):
    response = session.get('/1/members/me/boards')
    board = response.json()[0]
    return board
