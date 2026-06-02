import allure
import requests


class BaseApi:

    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.verify = False

    @allure.step("Отправить GET запрос на роут '{endpoint}'")
    def get(self, endpoint, params=None):
        return self.session.get(self.base_url + endpoint, params=params)

    @allure.step("Отправить POST запрос на роут '{endpoint}'")
    def post(self, endpoint, json=None):
        return self.session.post(self.base_url + endpoint, json=json)

    @allure.step("Отправить PUT запрос на роут '{endpoint}'")
    def put(self, endpoint, json=None, headers=None):
        return self.session.put(self.base_url + endpoint, json=json,
                                headers=headers)

    @allure.step("Отправить PATCH запрос на роут '{endpoint}'")
    def patch(self, endpoint, json=None, headers=None):
        return self.session.patch(self.base_url + endpoint, json=json,
                                  headers=headers)

    @allure.step("Отправить DELETE запрос на роут '{endpoint}'")
    def delete(self, endpoint, headers=None):
        return self.session.delete(self.base_url + endpoint, headers=headers)