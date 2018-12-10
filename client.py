import requests


class Client:
    def __init__(self, search_server, api_key):
        self.search_server = search_server
        self.api_key = api_key

    def index(self, dtype, did, title, document):
        response = requests.post(self.search_server + '/index', json={
            'id': did,
            'type': dtype,
            'body': {
                'title': title,
                'document': document
            }
        })
