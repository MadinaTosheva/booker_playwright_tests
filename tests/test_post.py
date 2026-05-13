from copy import deepcopy

import pytest

from config.api_data import BOOKING_DATA, PARTIAL_UPDATED_BOOKING_DATA, \
    MINIMUM_BOOKING_DATA
from schemas.booking_schema import POST_BOOKING_SCHEMA
from utils.assertions import assert_status_code, assert_field_contains, \
    assert_schema, assert_key_value


class TestPost:

    def test_tc_post_001(self, booking_api):
        response = booking_api.create_booking(BOOKING_DATA)
        assert_status_code(response, 200)
        assert_field_contains(response, "bookingid")

    def test_tc_post_002(self, booking_api):
        # Только firstname, lastname, totalprice, bookingdates
        # Отсутсвует поля - "depositpaid", из-за чего получаем 500
        response = booking_api.create_booking(MINIMUM_BOOKING_DATA)
        assert_status_code(response, 500)

    @pytest.mark.parametrize("updated_fields",[
                            {"depositpaid" : False},
                            {"additionalneeds" : "Breakfast"},
                            {"firstname" : ""},
                            {"lastname": "A"*1000}])

    def test_tc_post_003_004_006_007(self, booking_api, updated_fields):

        payload = deepcopy(BOOKING_DATA)
        payload.update(updated_fields)

        response = booking_api.create_booking(payload)
        assert_status_code(response, 200)
        assert_field_contains(response, "bookingid")

    def test_tc_post_005(self, booking_api):

        payload = deepcopy(BOOKING_DATA)
        payload["bookingdates"] = {"checkin": "2026-05-10",
                                  "checkout": "2026-05-01"}

        response = booking_api.create_booking(payload)
        assert_status_code(response, 200)
        assert_field_contains(response, "bookingid")

    def test_tc_post_008(self, booking_api):
        response = booking_api.create_booking(BOOKING_DATA)
        assert_status_code(response, 200)
        assert_field_contains(response, "bookingid")
        assert_schema(response, POST_BOOKING_SCHEMA)

    def test_tc_post_009(self, booking_api):
        response = booking_api.create_booking(BOOKING_DATA)
        assert_status_code(response, 200)
        id1 = response.json()["bookingid"]

        response = booking_api.create_booking(BOOKING_DATA)
        assert_status_code(response, 200)
        id2 = response.json()["bookingid"]

        assert id1 != id2

    def test_tc_post_010(self, booking_api):
        create = booking_api.create_booking(BOOKING_DATA)
        assert_status_code(create, 200)
        id = create.json()["bookingid"]

        get = booking_api.get_booking(id)
        assert_status_code(get, 200)
        assert_key_value(get, "firstname", "John")
        assert_key_value(get, "lastname", "Doe")