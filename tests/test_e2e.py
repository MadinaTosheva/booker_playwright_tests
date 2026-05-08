from config.api_data import USERNAME, PASSWORD, BOOKING_DATA, \
    UPDATED_BOOKING_DATA, PARTIAL_UPDATED_BOOKING_DATA
from schemas.booking_schema import GET_BOOKING_SCHEMA
from utils.assertions import assert_status_code, assert_field_contains, \
    assert_key_value, assert_schema


def test_tc_e2e(auth_api, booking_api):

    response = auth_api.create_token(USERNAME, PASSWORD)
    assert_status_code(response, 200)
    assert_field_contains(response, "token")
    token = response.json()["token"]

    create = booking_api.create_booking(BOOKING_DATA)
    assert_status_code(create, 200)
    assert_field_contains(create, "bookingid")

    booking_id = create.json()["bookingid"]

    get = booking_api.get_booking(booking_id)
    assert_status_code(get, 200)
    assert_key_value(get, "firstname", "John")

    assert_schema(get, GET_BOOKING_SCHEMA)

    update = booking_api.update_booking(booking_id, UPDATED_BOOKING_DATA, token)
    assert_status_code(update, 200)
    assert_key_value(update, "firstname", "Саша")
    assert_key_value(update, "lastname", "Мирнов")
    assert_key_value(update, "totalprice", 200)
    assert_key_value(update, "depositpaid", False)

    get = booking_api.get_booking(booking_id)
    assert get.json() == UPDATED_BOOKING_DATA

    patch = booking_api.partial_update_booking(booking_id, PARTIAL_UPDATED_BOOKING_DATA, token)
    assert_status_code(patch, 200)
    assert_key_value(patch, "firstname", "James")
    assert_key_value(patch, "lastname", "Smith")

    delete = booking_api.delete_booking(booking_id, token)
    assert_status_code(delete, 201)

    get = booking_api.get_booking(booking_id)
    assert_status_code(get, 404)

    assert response.elapsed.total_seconds() < 2.0
    assert "application/json" in response.headers["Content-Type"]
