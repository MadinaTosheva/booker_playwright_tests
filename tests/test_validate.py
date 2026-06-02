from unittest.mock import patch

import allure
import pytest
import requests

from config.api_data import BOOKING_ID, BOOKING_DATA, INVALID_BOOKING_DATA, \
    UPDATED_BOOKING_DATA, INVALID_BOOKING_ID, MINIMUM_BOOKING_DATA
from schemas.booking_schema import GET_BOOKING_SCHEMA, GET_ALL_BOOKINGS_SCHEMA
from utils.assertions import assert_schema, assert_header, \
    assert_response_time, assert_status_code


@allure.epic("Booking API")
@allure.feature("Validate Booking")
class TestValidate:

    @allure.title("Validate booking schema")
    @allure.severity(allure.severity_level.NORMAL)
    def test_tc_val_001(self, booking_api):

        get = booking_api.get_booking(BOOKING_ID)
        assert_schema(get, GET_BOOKING_SCHEMA)

    @allure.title("Validate list of booking schema")
    @allure.severity(allure.severity_level.NORMAL)
    def test_tc_val_002(self, booking_api):

        get = booking_api.get_all_bookings()
        assert_schema(get, GET_ALL_BOOKINGS_SCHEMA)

    @allure.title("Validate header on booking response")
    @allure.severity(allure.severity_level.NORMAL)
    def test_tc_val_003(self, booking_api):

        post = booking_api.create_booking(BOOKING_DATA)
        assert_header(post)

    @allure.title("Validate time of response < 200ms")
    @allure.severity(allure.severity_level.NORMAL)
    def test_tc_val_004(self, booking_api):
        post = booking_api.create_booking(BOOKING_DATA)
        assert_response_time(post)

    @allure.title("Send request with invalid json")
    @allure.severity(allure.severity_level.NORMAL)
    def test_tc_err_001(self, booking_api):
        post = booking_api.create_booking(MINIMUM_BOOKING_DATA)
        assert_status_code(post, 500)

    @allure.title("Update booking without token")
    @allure.severity(allure.severity_level.NORMAL)
    def test_tc_err_002(self, booking_api):
        update = booking_api.update_booking(BOOKING_ID, UPDATED_BOOKING_DATA)
        assert_status_code(update, 403)

    @allure.title("Get not existing booking")
    @allure.severity(allure.severity_level.NORMAL)
    def test_tc_err_003(self, booking_api):
        get = booking_api.get_booking(INVALID_BOOKING_ID)
        assert_status_code(get, 404)

    @allure.title("Get timeout=0.001")
    @allure.severity(allure.severity_level.NORMAL)
    def test_tc_err_004(self, booking_api):
        with patch.object(requests.Session, "get") as mock_get:
            mock_get.side_effect = requests.exceptions.Timeout

            with pytest.raises(requests.exceptions.Timeout):
                booking_api.get_booking(BOOKING_ID)

