def get_subset_dict(dict, keys):
    '''
    Returns sub dictionary with requested keys. i.e.:

    > dict = {'a': 1, 'b': 2, 'c': 3}
    > keys = ['a', 'b']
    > get_subset_dict(dict, keys)
    {'a': 1, 'b': 2}
    '''
    return {key: value for key, value in dict.items() if key in keys}


def subtract_dict(dict, sub_dict):
    '''
    Returns a dict by removing the elements belonging to another dict. i.e.:

    > sub_dict = {'a': '1', 'b': '2'}
    > dict =     {'a': '1', 'b': '3', 'c': '5'}
    > subtract_dict(dict, sub_dict)
    {'c': '5'}
    '''
    remaining_keys = dict.keys() - sub_dict.keys()
    return get_subset_dict(dict, remaining_keys)
