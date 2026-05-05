import pytest
from api.auth_api import AuthApi
from api.booking_api import BookingApi
from config.api_data import USERNAME, PASSWORD
from config.api_urls import BASE_URL

@pytest.fixture
def auth_session():
    auth_page = AuthApi(BASE_URL)

    # 1. получаем токен
    token = auth_page.create_token(USERNAME, PASSWORD)

    # 2. кладём его в session
    auth_page.session.cookies.set("token", token)

    # 3. возвращаем session
    return auth_page.session


@pytest.fixture
def auth_api():
    return AuthApi(BASE_URL)


@pytest.fixture
def booking_api():
    return BookingApi(BASE_URL)