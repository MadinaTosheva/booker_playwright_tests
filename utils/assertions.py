from jsonschema import validate


def assert_status_code(response, expected_code = 200):
    assert response.status_code == expected_code, \
        f"Expected {expected_code}, got {response.status_code}"


def assert_field_contains(response, field):
    assert field in response.json(), f"{field} not in response"


def assert_key_value(response, key, value):
    assert response.json()[key] == value


def assert_schema(response, schema):
    validate(instance=response.json(), schema=schema)


def assert_token(token):
    assert isinstance(token, str) and len(token) > 0