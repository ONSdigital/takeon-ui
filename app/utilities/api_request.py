import json
import requests
import requests_mock
from kubernetes.client.rest import ApiException
from app.mock_suite import mock_suite
from app.utilities.kubernetes_config import KubernetesConfig

class ApiRequest:
    def __init__(self, service="business-layer", mocking=True):
        self.mock = mocking
        #print('Mocking status: {}'.format(self.mock))
        if not self.mock:
            self.kube = KubernetesConfig(service)

    def build_endpoint(self, endpoint, parameters):
        return "http://" + self.kube.get_ip() + ":" + self.kube.get_port() + endpoint + "/{}".format(parameters)

    def request_get(self, endpoint, parameters):
        try:
            return requests.get(self.build_endpoint(endpoint, parameters))
        except ApiException as error:
            raise TakeonApiException(error.body, status_code=410)
        # except ConnectionError as error:
            # raise TakeonApiException(error.args, status_code=410)
        except requests.RequestException as error:
            raise TakeonApiException(error.args, status_code=410)

    def request_put(self, endpoint, parameters, data, headers):
        return requests.put(self.build_endpoint(endpoint, parameters), data=data, headers=headers)


    def contributor_search(self, parameters):
        if self.mock:
            return mock_contributor_search_screen(url_connect=parameters).text
        return self.request_get(endpoint="/contributor/qlSearch", parameters=parameters).text

    def form_definition(self, parameters):
        if self.mock:
            return mock_form_definition(url_connect=parameters).text
        return self.request_get(endpoint="/FormDefinition/GetFormDefinition", parameters=parameters).text

    def contributor_search_without_paging(self, parameters):
        if self.mock:
            return mock_contributor_search(url_connect=parameters).text
        return self.request_get(endpoint="/contributor/search", parameters=parameters).text

    def form_response(self, parameters):
        if self.mock:
            return mock_form_response(url_connect=parameters).text
        return self.request_get(endpoint="/Response/QuestionResponse", parameters=parameters).text

    def update_response(self, parameters, data):
        if self.mock:
            return None
        return self.request_put(
            endpoint="/Upsert/CompareResponses",
            data=bytes(json.dumps(data), encoding="utf-8"),
            headers={"Content-Type": "Application/Json"},
            parameters=parameters
            ).text

    def save_response(self, parameters, data):
        if self.mock:
            return None
        return self.request_put(
            endpoint="/response/save",
            data=bytes(json.dumps(data), encoding="utf-8"),
            headers={"Content-Type": "Application/Json"},
            parameters=parameters
            ).text

    def graphql_post(self, parameters):
        if self.mock:
            return mock_next_page(url_connect=parameters).text
        return self.request_get(endpoint="/contributor/qlSearch", parameters=parameters).text

    def validation_outputs(self, parameters):
        if self.mock:
            return mock_get_validation(url_connect=parameters).text
        return self.request_get(endpoint="/validation/validationoutput", parameters=parameters).text



class TakeonApiException(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        output = dict(self.payload or ())
        output['message'] = self.message
        return output





@requests_mock.Mocker()
def mock_next_page(mock=None, url_connect=None):
    mocked_up_data = mock_suite.MockSuite("mock_graphql_api.json").get_data()
    url = "http://localhost:8090/" + url_connect
    mock.get(url, text=mocked_up_data)
    return requests.get(url)


@requests_mock.Mocker()
def mock_form_definition(mock=None, url_connect=None):
    mocked_up_data = mock_suite.MockSuite("mock_form_definition.json").get_data()
    url = "http://localhost:8090/" + url_connect
    mock.get(url, text=mocked_up_data)
    return requests.get(url)


@requests_mock.Mocker()
def mock_contributor_search(mock=None, url_connect=None):
    mocked_up_data = mock_suite.MockSuite("mock_contributor_search.json").get_data()
    url = "http://localhost:8090/" + url_connect
    mock.get(url, text=mocked_up_data)
    return requests.get(url)


@requests_mock.Mocker()
def mock_contributor_search_screen(mock=None, url_connect=None):
    mocked_up_data = mock_suite.MockSuite("mock_contributor_search.json").get_data()
    url = "http://localhost:8090/" + url_connect
    mock.get(url, text=mocked_up_data)
    return requests.get(url)


@requests_mock.Mocker()
def mock_form_response(mock=None, url_connect=None):
    mocked_up_data = mock_suite.MockSuite("mock_form_response.json").get_data()
    url = "http://localhost:8090/" + url_connect
    mock.get(url, text=mocked_up_data)
    return requests.get(url)


@requests_mock.Mocker()
def mock_get_validation(mock=None, url_connect=None):
    mocked_up_data = mock_suite.MockSuite("mock_validation_outputs.json").get_data()
    url = "http://localhost:8090/" + url_connect
    mock.get(url, text=mocked_up_data)
    return requests.get(url)


@requests_mock.Mocker()
def mock_contributor_search_no_error(mock=None, url_connect=None):
    mocked_up_data = mock_suite.MockSuite("mock_validation_outputs.json").get_data()
    url = "http://localhost:8090/" + url_connect
    mock.get(url, text=mocked_up_data)
    return requests.get(url)


@requests_mock.Mocker()
def mock_contributor_search_error_blank(mock=None, url_connect=None):
    mocked_up_data = mock_suite.MockSuite("mock_validation_outputs.json").get_data()
    url = "http://localhost:8090/" + url_connect
    mock.get(url, text=mocked_up_data)
    return requests.get(url)


@requests_mock.Mocker()
def mock_contributor_search_error_populated(mock=None, url_connect=None):
    mocked_up_data = mock_suite.MockSuite("mock_validation_outputs.json").get_data()
    url = "http://localhost:8090/" + url_connect
    mock.get(url, text=mocked_up_data)
    return requests.get(url)
