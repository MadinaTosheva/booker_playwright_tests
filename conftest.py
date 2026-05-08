import pytest
from api.auth_api import AuthApi
from api.booking_api import BookingApi
from config.api_data import USERNAME, PASSWORD
from config.api_urls import BASE_URL


# @pytest.fixture
# def auth_session(auth_api):
#
#     # 1. получаем респонс и извлекаем токен
#     response = auth_api.create_token(USERNAME, PASSWORD)
#     token = response.json()['token']
#
#     # 2. кладём его в session
#     auth_api.session.cookies.set("token", token)
#
#     # 3. возвращаем session
#     return auth_api.session


@pytest.fixture
def auth_api():
    return AuthApi(BASE_URL)


@pytest.fixture
def booking_api():
    return BookingApi(BASE_URL)