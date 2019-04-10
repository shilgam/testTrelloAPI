from sum import sum
import pytest


@pytest.fixture
def get_sum_test_data():
    return [(1, 2, 3), (3, 5, 8), (-2, 2, 0)]


def test_sum_output_type():
    assert type(sum(1, 2)) is int


def test_sum(get_sum_test_data):
    for data in get_sum_test_data:
        num1 = data[0]
        num2 = data[1]
        expected = data[2]
        assert sum(num1, num2) == expected
