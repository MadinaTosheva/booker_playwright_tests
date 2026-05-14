import pytest

from config.api_data import BOOKING_ID, INVALID_BOOKING_ID
from schemas.booking_schema import GET_BOOKING_SCHEMA, GET_ALL_BOOKINGS_SCHEMA
from utils.assertions import assert_status_code, assert_key_value, \
    assert_schema, assert_header, assert_response_time


class TestGetBooking:

    def test_tc_get_001(self, booking_api):
        response = booking_api.get_all_bookings()
        assert_status_code(response, 200)
        assert response.json() != []


    @pytest.mark.parametrize( "params", [
                                        {"firstname": "John"},
                                        {"lastname": "Doe"},
                                        {
                                         "checkin": "2026-01-01",
                                         "checkout": "2026-01-05" }])

    def test_tc_get_002_003_004(self, booking_api, params):
        response = booking_api.get_all_bookings(params)
        assert_status_code(response, 200)

    def test_tc_get_005(self, booking_api):
        response = booking_api.get_booking(BOOKING_ID)
        assert_status_code(response, 200)

    def test_tc_get_006(self, booking_api):
        response = booking_api.get_booking(INVALID_BOOKING_ID)
        assert_status_code(response, 404)

    def test_tc_get_007(self, booking_api):
        response = booking_api.get_all_bookings()
        assert_status_code(response, 200)
        assert_schema(response, GET_ALL_BOOKINGS_SCHEMA)

    def test_tc_get_008(self, booking_api):
        response = booking_api.get_booking(BOOKING_ID)
        assert_status_code(response, 200)
        assert_schema(response, GET_BOOKING_SCHEMA)

    def test_tc_get_009(self, booking_api):
        response = booking_api.get_booking(BOOKING_ID)
        assert_status_code(response, 200)
        assert_header(response)
        assert_response_time(response)

    def test_tc_get_010(self, booking_api):
        response = booking_api.get_booking(BOOKING_ID)
        assert_status_code(response, 200)
        assert_response_time(response)