# import json
import pytest
from trello.test.fixtures.board import (board_only_req_fields,
                                        board_optional_fields)


class TestClass:
    @pytest.mark.parametrize("valid_board", [
        board_only_req_fields,
        board_optional_fields,
        {'key': 'val'}
    ])
    def test_something(self, valid_board):
        # print(json.dumps(valid_board, indent=4, sort_keys=True))
        assert 1 == 1

    def test_second_case(self, valid_board):
        # print(json.dumps(valid_board, indent=4, sort_keys=True))
        assert 1 == 1
