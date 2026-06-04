import pytest
from api.auth_api import AuthApi
from api.booking_api import BookingApi
from config.api_data import USERNAME, PASSWORD
from config.api_urls import BASE_URL


@pytest.fixture
def auth_session(auth_api):

    # 1. получаем респонс и извлекаем токен
    response = auth_api.create_token(USERNAME, PASSWORD)
    token = response.json()['token']

    # 2. кладём его в session
    auth_api.session.cookies.set("token", token)

    # 3. возвращаем session
    yield auth_api.session

    auth_api.session.close()


@pytest.fixture
def auth_api():
    api = AuthApi(BASE_URL)
    api.session.verify = False  # чтобы сертификаты не проверялись
    return api


@pytest.fixture
def booking_api():
    api =  BookingApi(BASE_URL)
    api.session.verify = False  # чтобы сертификаты не проверялись
    return api


@pytest.fixture
def auth_booking_api(auth_session):
    api = BookingApi(BASE_URL)
    api.session = auth_session
    return api
