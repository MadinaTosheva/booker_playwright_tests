import allure
import pytest

from config.api_data import USERNAME, PASSWORD, WRONG_PASSWORD, WRONG_USERNAME, \
    BOOKING_DATA, UPDATED_BOOKING_DATA, BOOKING_ID, VALID_TOKEN, INVALID_TOKEN
from utils.assertions import assert_status_code, assert_field_contains, \
    assert_key_value, assert_token


@allure.epic("Booking API")
@allure.feature("Authorization")
class TestAuth:

    @allure.story("Create token")
    @allure.title("Authorize with different credentials('username' and 'password')")
    @pytest.mark.parametrize("username, password",
                             [(USERNAME, PASSWORD),
                             (USERNAME, WRONG_PASSWORD),
                             (WRONG_USERNAME, PASSWORD)])

    def test_tc_auth_001_002_003(self, auth_api, username, password):

        response = auth_api.create_token(username, password)
        assert_status_code(response, 200)
        assert_field_contains(response, "token")
        token = response.json()["token"]

    @allure.story("Update booking")
    @allure.title("Update booking with valid token")
    def test_tc_auth_004(self, auth_booking_api):

        update = auth_booking_api.update_booking(BOOKING_ID, UPDATED_BOOKING_DATA,
                                            VALID_TOKEN)
        assert_status_code(update, 200)
        assert_key_value(update, "firstname", "Саша")

    @allure.story("Update booking")
    @allure.title("Update booking with invalid token")
    def test_tc_auth_005(self, booking_api):

        update = booking_api.update_booking(BOOKING_ID, UPDATED_BOOKING_DATA,
                                            INVALID_TOKEN)
        assert_status_code(update, 403)

    @allure.story("Update booking")
    @allure.title("Update booking without token")
    def test_tc_auth_006(self, booking_api):

        update = booking_api.update_booking(BOOKING_ID, UPDATED_BOOKING_DATA)
        assert_status_code(update, 403)

    @allure.story("Create token")
    @allure.title("Authorize with valid credentials and validate token")
    def test_tc_auth_007(self, auth_api):

        response = auth_api.create_token(USERNAME, PASSWORD)
        assert_status_code(response, 200)
        assert_field_contains(response, "token")
        token = response.json()["token"]
        assert_token(token)

    @allure.story("Create token")
    @allure.title("Send multiple authorization requests")
    def test_tc_auth_008(self, auth_api):

        for i in range(2):
            self.test_tc_auth_007(auth_api)
