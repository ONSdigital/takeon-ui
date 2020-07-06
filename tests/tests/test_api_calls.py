import pytest
import requests
from app.kubernetes_discovery import kubernetes_config
from requests.exceptions import HTTPError

class TestClass(object):
    # def test_call_api(self):
    #     # Define mocked data
    #     discovery_service = kubernetes_config.KubernetesConfig("take-on", mocking=True)
    #     response_data = discovery_service.contributor_search("http://dummyURL:4040/test", "persistence-layer")
    #     assert response_data == None

    def test_call_define(self):
        invalidURL = 'http://echo.jsontest.com/key/value/one/two'
        expected_error = HTTPError('404 Client Error: Not Found for url:py ' + invalidURL)
        try:
            response = requests.get(invalidURL)
            response.raise_for_status()
        except HTTPError as http_err:
            response = http_err
            print(f'HTTP error occurred: {http_err}')  # Python 3.6
        except Exception as err:
            response = err
            print(f'Other error occurred: {err}')  # Python 3.6
        else:
            print('Success!')
        assert response.text == False
