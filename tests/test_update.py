from copy import deepcopy

import allure
import urllib3

from schemas.booking_schema import GET_BOOKING_SCHEMA

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from config.api_data import BOOKING_ID, \
    UPDATED_BOOKING_DATA, PARTIAL_UPDATED_BOOKING_DATA, INVALID_BOOKING_ID, \
    INVALID_TOKEN, INVALID_BOOKING_DATA, BOOKING_DATA
from conftest import auth_api, auth_session, booking_api
from utils.assertions import assert_status_code, assert_key_value, \
    assert_schema

@allure.epic("Booking API")
@allure.feature("Update Booking")
class TestUpdate:

    @allure.title("Totally update booking with token")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_tc_put_001(self, auth_session, booking_api):
        booking_api.session = auth_session

        put = booking_api.update_booking(BOOKING_ID, UPDATED_BOOKING_DATA)
        assert_status_code(put, 200)
        assert_key_value(put, "firstname", "Саша")
        assert_key_value(put, "lastname", "Мирнов")
        assert_key_value(put, "totalprice", 200)
        assert_key_value(put, "depositpaid", False)

    @allure.title("Partially update booking with token")
    @allure.severity(allure.severity_level.NORMAL)
    def test_tc_put_002(self, auth_session, booking_api):
        booking_api.session = auth_session

        patch = booking_api.partial_update_booking(BOOKING_ID, PARTIAL_UPDATED_BOOKING_DATA)
        assert_status_code(patch, 200)
        assert_key_value(patch, "firstname", "James")
        assert_key_value(patch, "lastname", "Smith")

    @allure.title("Update not existed booking with token")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_tc_put_003(self, auth_session, booking_api):
        booking_api.session = auth_session

        put = booking_api.update_booking(INVALID_BOOKING_ID, UPDATED_BOOKING_DATA)
        assert_status_code(put, 405)

    @allure.title("Update booking without token")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_tc_put_004(self, booking_api):
        update = booking_api.update_booking(BOOKING_ID, UPDATED_BOOKING_DATA)
        assert_status_code(update, 403)

    @allure.title("Update booking with invalid token")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_tc_put_005(self, booking_api):
        update = booking_api.update_booking(BOOKING_ID, UPDATED_BOOKING_DATA,
                                            INVALID_TOKEN)
        assert_status_code(update, 403)

    @allure.title("Update booking with invalid data")
    @allure.severity(allure.severity_level.NORMAL)
    def test_tc_put_006(self, booking_api, auth_session):
        booking_api.session = auth_session

        update = booking_api.update_booking(BOOKING_ID, INVALID_BOOKING_DATA)
        assert_status_code(update, 405)

    @allure.title("Partially update booking with 'bookingdates'")
    @allure.severity(allure.severity_level.NORMAL)
    def test_tc_put_007(self, booking_api, auth_session):
        booking_api.session = auth_session

        payload = deepcopy(BOOKING_DATA)
        payload["bookingdates"] = {"checkin": "2026-05-01",
                                   "checkout": "2026-05-30"}

        put = booking_api.update_booking(BOOKING_ID, payload)
        assert_status_code(put, 200)

    @allure.title("Validate booking schema after updation")
    @allure.severity(allure.severity_level.NORMAL)
    def test_tc_put_008(self, booking_api, auth_session):
        booking_api.session = auth_session

        put = booking_api.update_booking(BOOKING_ID,UPDATED_BOOKING_DATA)
        assert_status_code(put, 200)
        assert_schema(put, GET_BOOKING_SCHEMA)

    @allure.title("Update single field- totalprice")
    @allure.severity(allure.severity_level.NORMAL)
    def test_tc_patch_001(self, booking_api, auth_session):
        booking_api.session = auth_session

        payload = {"totalprice": 500}

        patch = booking_api.update_booking(BOOKING_ID, payload)
        assert_status_code(patch, 200)
        assert_key_value(patch, "totalprice", 500)

    @allure.title("Update single field- depositpaid")
    @allure.severity(allure.severity_level.NORMAL)
    def test_tc_patch_002(self, booking_api, auth_session):
        booking_api.session = auth_session

        payload =  {"depositpaid": False}

        patch = booking_api.update_booking(BOOKING_ID, payload)
        assert_status_code(patch, 200)
        assert_key_value(patch, "depositpaid", False)
