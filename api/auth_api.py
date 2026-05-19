import allure

from api.base_api import BaseApi
from config.api_urls import AUTH_ENDPOINT


class AuthApi(BaseApi):

    @allure.step("Create token with username: '{username}' and password: '{password}'")
    def create_token(self, username, password):

        payload = {
            "username": username,
            "password": password
        }

        response = self.post(AUTH_ENDPOINT, json=payload)
        return response