import pytest
from app.utilities.notify_baw import build_notify_data_to_send


valid_input_data = {
    "reference": "12000534932",
    "survey": "023",
    "period": "201904",
    "status": "CLEAR",
    "error": None,
    "selective_editing_flag": "PASSED"
  }


missing_key_data = {
        "reference": "12000534932",
        "survey": "023",
        "period": "201904",
        "error": None,
        "selective_editing_flag": "PASSED"
  }


def test_build_notify_data_to_send_returns_expected():
    assert build_notify_data_to_send(valid_input_data) == valid_input_data


def test_build_notify_data_to_send_raises_key_error_missing_key():
    ''' No invalid JSON should reach this function so testing missing key only'''
    with pytest.raises(KeyError):
        build_notify_data_to_send(missing_key_data)
