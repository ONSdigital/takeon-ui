import pytest
from app.utilities.helpers import validate_json

invalid_json = "[\"reference\": \"test\"]"

blank_json_string = "{}"

non_string_input = {}


def test_validate_json_returns_empty_json():
    assert validate_json(blank_json_string) == {}


def test_validate_json():
    with pytest.raises(ValueError):
        validate_json(invalid_json)


def test_validate_json_returns_type_error():
    with pytest.raises(TypeError):
        validate_json(non_string_input)
