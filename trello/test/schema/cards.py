from schema import Schema


def card_schema():
    return Schema({
        'badges': {
            'attachments': int,
            'attachmentsByType': {
                'trello': {
                    'board': int,
                    'card': int
                }
            },
            'checkItems': int,
            'checkItemsChecked': int,
            'comments': int,
            'description': bool,
            'due': object,
            'dueComplete': bool,
            'fogbugz': str,
            'location': object,
            'subscribed': bool,
            'viewingMemberVoted': bool,
            'votes': int,
        },
        'checkItemStates': object,
        'closed': bool,
        'dateLastActivity': str,
        'desc': str,
        'descData': object,
        'due': object,
        'dueComplete': bool,
        'dueReminder': object,
        'id': str,
        'idAttachmentCover': object,
        'idBoard': str,
        'idChecklists': list,
        'idLabels': list,
        'idList': object,
        'idMembers': list,
        'idMembersVoted': list,
        'idShort': object,
        'labels': list,
        'manualCoverAttachment': object,
        'name': str,
        'pos': object,
        'shortLink': str,
        'shortUrl': str,
        'subscribed': bool,
        'url': str
    })
