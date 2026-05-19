import pytest
import allure

from config.api_data import BOOKING_ID, INVALID_BOOKING_ID
from schemas.booking_schema import GET_BOOKING_SCHEMA, GET_ALL_BOOKINGS_SCHEMA
from utils.assertions import assert_status_code, assert_key_value, \
    assert_schema, assert_header, assert_response_time


@allure.epic("Booking API")
@allure.feature("Get Booking")
class TestGetBooking:

    @allure.story("Get all bookings")
    @allure.title("Get all bookings without any filters")
    def test_tc_get_001(self, booking_api):
        response = booking_api.get_all_bookings()
        assert_status_code(response, 200)
        assert response.json() != []


    @allure.story("Get list of bookings")
    @allure.title("Get all bookings with some params")
    @pytest.mark.parametrize( "params", [
                                        {"firstname": "John"},
                                        {"lastname": "Doe"},
                                        {
                                         "checkin": "2026-01-01",
                                         "checkout": "2026-01-05" }])
    def test_tc_get_002_003_004(self, booking_api, params):
        response = booking_api.get_all_bookings(params)
        assert_status_code(response, 200)

    @allure.story("Get booking")
    @allure.title("Get booking with a valid booking_id")
    def test_tc_get_005(self, booking_api):
        response = booking_api.get_booking(BOOKING_ID)
        assert_status_code(response, 200)

    @allure.story("Get booking")
    @allure.title("Get booking with an invalid booking_id")
    def test_tc_get_006(self, booking_api):
        response = booking_api.get_booking(INVALID_BOOKING_ID)
        assert_status_code(response, 404)

    @allure.story("Get all bookings")
    @allure.title("Get all bookings and validate schema")
    def test_tc_get_007(self, booking_api):
        response = booking_api.get_all_bookings()
        assert_status_code(response, 200)
        assert_schema(response, GET_ALL_BOOKINGS_SCHEMA)

    @allure.story("Get booking")
    @allure.title("Get booking and validate schema")
    def test_tc_get_008(self, booking_api):
        response = booking_api.get_booking(BOOKING_ID)
        assert_status_code(response, 200)
        assert_schema(response, GET_BOOKING_SCHEMA)

    @allure.story("Get booking")
    @allure.title("Get booking and validate header")
    def test_tc_get_009(self, booking_api):
        response = booking_api.get_booking(BOOKING_ID)
        assert_status_code(response, 200)
        assert_header(response)

    @allure.story("Get booking")
    @allure.title("Get booking and validate response_time")
    def test_tc_get_010(self, booking_api):
        response = booking_api.get_booking(BOOKING_ID)
        assert_status_code(response, 200)
        assert_response_time(response)