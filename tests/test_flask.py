from app.forms.contributor_search_form import build_uri, clean_search_parameters


def test_build_url_one_param():
    vaules_passed = {"Period": "201812"}
    result = build_uri(vaules_passed)
    assert result == "Period=201812"


def test_build_url_two_params():
    values_passed = {"Period": "201812", "Survey": "111"}
    result = build_uri(values_passed)
    assert result == "Period=201812;Survey=111"


def test_build_url_three_params_one_blank():
    values_passed = {"Period": "", "Survey": "222", "Reference": "49900001"}
    result = build_uri(values_passed)
    assert result == "Survey=222;Reference=49900001"


def test_clean_search_parameters_two_params_one_with_interstital_space():
    values_passed = {"Period": "2018 12", "Survey": "111"}
    result = clean_search_parameters(values_passed)
    assert result == {"Period": "201812", "Survey": "111"}


def test_clean_search_parameters_two_params_one_with_interstitial_and_trailing_space():
    values_passed = {"Period": "2018 12   ", "Survey": "111"}
    result = clean_search_parameters(values_passed)
    assert result == {"Period": "201812", "Survey": "111"}


def test_clean_search_parameters_two_params_both_with_interstitial_and_trailing_and_leading_space():
    values_passed = {"Period": " 2018 12   ", "Survey": "   11   1  "}
    result = clean_search_parameters(values_passed)
    assert result == {"Period": "201812", "Survey": "111"}


# def test_landing_page_exists():
#     assert eureka_config.mock_contributor_search(url_connect='/').status_code == 200


# def test_main_page_exists():
#     assert eureka_config.mock_contributor_search(url_connect='/Contributor/GeneralSearch').status_code == 200
