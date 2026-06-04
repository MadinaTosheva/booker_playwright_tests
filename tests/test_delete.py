import allure

from config.api_data import BOOKING_ID, INVALID_BOOKING_ID, INVALID_TOKEN, \
    BOOKING_DATA
from utils.assertions import assert_status_code, assert_field_contains


@allure.epic("Booking API")
@allure.feature("Delete Booking")
class TestDelete:

    # Так как встроенные буккинги обновлялись каждые 10 мин, использовала разных
    # айдишек для получении успешных результатов

    @allure.title("Delete existing booking with token")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_tc_delete_001(self, auth_booking_api):

        delete = auth_booking_api.delete_booking(BOOKING_ID + 1)
        assert_status_code(delete, 201)

    @allure.title("Validate deleted booking not exists")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_tc_delete_002(self, auth_booking_api):
        create = auth_booking_api.create_booking(BOOKING_DATA)
        booking_id = create.json()["bookingid"]

        delete = auth_booking_api.delete_booking(booking_id)
        assert_status_code(delete, 201)

        get = auth_booking_api.get_booking(booking_id)
        assert_status_code(get, 404)

    @allure.title("Delete not existed booking")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_tc_delete_003(self, auth_booking_api):

        delete = auth_booking_api.delete_booking(INVALID_BOOKING_ID)
        assert_status_code(delete, 405)

    @allure.title("Delete booking without token")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_tc_delete_004(self, booking_api):

        delete = booking_api.delete_booking(BOOKING_ID)
        assert_status_code(delete, 403)

    @allure.title("Delete booking with invalid token")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_tc_delete_005(self, booking_api):

        delete = booking_api.delete_booking(BOOKING_ID, INVALID_TOKEN)
        assert_status_code(delete, 403)

    @allure.title("Delete same booking 2 times")
    @allure.severity(allure.severity_level.NORMAL)
    def test_tc_delete_006(self, auth_booking_api):
        create = auth_booking_api.create_booking(BOOKING_DATA)
        booking_id = create.json()["bookingid"]

        delete = auth_booking_api.delete_booking(booking_id)
        assert_status_code(delete, 201)

        delete2 = auth_booking_api.delete_booking(booking_id)
        assert_status_code(delete2, 404)

    @allure.title("Validate delete response")
    @allure.severity(allure.severity_level.NORMAL)
    def test_tc_delete_007(self, auth_booking_api):
        create = auth_booking_api.create_booking(BOOKING_DATA)
        booking_id = create.json()["bookingid"]

        delete = auth_booking_api.delete_booking(booking_id)
        assert_status_code(delete, 201)
        assert_field_contains(delete, "")
