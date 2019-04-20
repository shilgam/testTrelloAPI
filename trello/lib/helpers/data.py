def get_subset_dict(dict, attributes):
    return {key: value for key, value in dict.items() if key in attributes}
