import requests

import app.auth as auth

MOCK_TOKEN_ENDPOINT = "http://apigw/oauth/foobar/token"
MOCK_CLIENT_ID = "abc-def-ghi-jkl"
MOCK_CLIENT_SECRET = "testPass"
FAKE_TOKEN = {
    "access_token": "foo-bar-one",
    "token_type": "Bearer",
    "expires_in": 3600,
    "refresh_token": "foo-bar-two",
    "scope": "oob"
}


def test_build_headers():
    result = auth.build_headers(MOCK_CLIENT_ID, MOCK_CLIENT_SECRET)
    assert isinstance(result, dict)
    assert result == {
        'content-type': "application/x-www-form-urlencoded",
        'authorization': "Basic YWJjLWRlZi1naGktamtsOnRlc3RQYXNz",
        'cache-control': "no-cache"
    }


def test_build_payload():
    result = auth.build_payload('smithj', 'chickpea')
    assert isinstance(result, str)
    assert result == 'grant_type=password&username=smithj&password=chickpea'


def test_encode_client_details():
    result = auth.encode_client_details(MOCK_CLIENT_ID, MOCK_CLIENT_SECRET)
    assert isinstance(result, str)
    assert result == 'YWJjLWRlZi1naGktamtsOnRlc3RQYXNz'


def test_get_token(requests_mock):
    requests_mock.post(MOCK_TOKEN_ENDPOINT, json=FAKE_TOKEN, status_code=200)  # mock endpoint response
    payload = {}
    headers = {}
    result = auth.get_token(MOCK_TOKEN_ENDPOINT, payload, headers)
    assert isinstance(result, requests.models.Response)
    assert result.json() == FAKE_TOKEN
