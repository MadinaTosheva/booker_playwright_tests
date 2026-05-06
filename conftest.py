import pytest
from api.auth_api import AuthApi
from api.booking_api import BookingApi
from config.api_urls import BASE_URL


@pytest.fixture
def auth_api():
    return AuthApi(BASE_URL)


@pytest.fixture
def booking_api():
    return BookingApi(BASE_URL)