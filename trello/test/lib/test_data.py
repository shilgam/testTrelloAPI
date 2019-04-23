from trello.lib.helpers.data import subtract_dict


class TestSubstractDict:

    def test_include_extra_keys_in_dict(self):
        sub_dict = {'a': 1, 'b': 2}
        dict_ext = {'a': 1, 'b': 3, 'c': []}
        assert subtract_dict(dict_ext, sub_dict) == {'c': []}

    def test_exclude_extra_keys_in_sub_dict(self):
        sub_dict = {'a': 1, 'b': 2}
        dict_ext = {'a': 1, 'b': 3, 'c': 5}
        assert subtract_dict(dict_ext, sub_dict) == {'c': 5}
