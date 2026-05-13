import requests


class BaseApi:

    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

    def get(self, endpoint, params= None):
        return self.session.get(self.base_url + endpoint, params = params)

    def post(self, endpoint, json=None):
        return self.session.post(self.base_url + endpoint, json=json)

    def put(self, endpoint, json=None, headers=None):
        return self.session.put(self.base_url + endpoint, json=json, headers=headers)

    def patch(self, endpoint, json=None, headers=None):
        return self.session.patch(self.base_url + endpoint, json=json, headers=headers)

    def delete(self, endpoint, headers=None):
        return self.session.delete(self.base_url + endpoint, headers=headers)