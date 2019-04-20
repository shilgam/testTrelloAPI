from schema import Schema


def board_schema():
    return Schema({
        'closed': bool,
        'desc': str,
        'descData': object,
        'id': str,
        'idOrganization': object,
        'labelNames': {
            'black': str,
            'green': str,
            'yellow': str,
            str: object},  # don't care about other str keys
        'name': str,
        'pinned': object,
        'prefs': {
            'comments': str,
            'invitations': str,
            'permissionLevel': str,
            'selfJoin': bool,
            'voting': str,
            str: object},  # don't care about other str keys
        'shortUrl': str,
        'url': str
    })
