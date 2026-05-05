from api.base_api import BaseApi
from config.api_data import USERNAME, PASSWORD
from config.api_urls import AUTH_ENDPOINT


class AuthApi(BaseApi):

    def create_token(self, USERNAME, PASSWORD):
        payload = {
            "username": USERNAME,
            "password": PASSWORD
        }

        response = self.post(AUTH_ENDPOINT, json=payload)
        return response.json()["token"]