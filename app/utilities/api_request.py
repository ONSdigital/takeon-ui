import json
import requests
import requests_mock
from kubernetes.client.rest import ApiException
from app.mock_suite import mock_suite
from app.utilities.kubernetes_config import KubernetesConfig


localhost_url = "http://localhost:8090/"
mocked_validation_output = "mock_validation_outputs.json"
json_application = "Application/Json"


class ApiRequest:
    def __init__(self, log, service="business-layer", mocking=True):
        self.log = log
        self.mock = mocking
        # print('Mocking status: {}'.format(self.mock))
        if not self.mock:
            self.kube = KubernetesConfig(log, service)

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

    def request_post(self, endpoint, parameters, data, headers):
        return requests.post(self.build_endpoint(endpoint, parameters), data=data, headers=headers)

    def request_post_api_gateway(self, endpoint, data, headers):
        return requests.post(endpoint, data=data, headers=headers)

    def view_form_responses(self, parameters):
        if self.mock:
            return mock_view_form_responses(url_connect=parameters).text
        return self.request_get(endpoint="/viewform/responses", parameters=parameters).text

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
            headers={"Content-Type": json_application},
            parameters=parameters).text

    def save_response(self, parameters, data):
        if self.mock:
            return None
        return self.request_put(
            endpoint="/response/save",
            data=bytes(json.dumps(data), encoding="utf-8"),
            headers={"Content-Type": json_application},
            parameters=parameters).text

    def graphql_post(self, parameters):
        if self.mock:
            return mock_next_page(url_connect=parameters).text
        return self.request_get(endpoint="/contributor/qlSearch", parameters=parameters).text

    def validation_outputs(self, parameters):
        if self.mock:
            return mock_get_validation(url_connect=parameters).text
        return self.request_get(endpoint="/validation/validationoutput", parameters=parameters).text

    def validation_overrides(self, parameters, data):
        # self.request_post(endpoint="/validation/saveOverrides", parameters=parameters, data=data, headers=headers)
        return self.request_post(endpoint="/validation/saveOverrides", parameters=parameters, data=data, headers={"Content-Type": json_application}).text

    def run_validation(self, endpoint, data, headers):
        return self.request_post_api_gateway(endpoint=endpoint, data=data, headers=headers).text

    def get_historic_data(self, parameters):
        if self.mock:
            return mock_historic_data(url_connect=parameters).text
        return self.request_get(endpoint="/viewform/historydata", parameters=parameters).text


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
    url = localhost_url + url_connect
    mock.get(url, text=mocked_up_data)
    return requests.get(url)


@requests_mock.Mocker()
def mock_form_definition(mock=None, url_connect=None):
    mocked_up_data = mock_suite.MockSuite("mock_form_definition.json").get_data()
    url = localhost_url + url_connect
    mock.get(url, text=mocked_up_data)
    return requests.get(url)


@requests_mock.Mocker()
def mock_contributor_search(mock=None, url_connect=None):
    mocked_up_data = mock_suite.MockSuite("mock_contributor_search.json").get_data()
    url = localhost_url + url_connect
    mock.get(url, text=mocked_up_data)
    return requests.get(url)


@requests_mock.Mocker()
def mock_contributor_search_screen(mock=None, url_connect=None):
    mocked_up_data = mock_suite.MockSuite("mock_contributor_search.json").get_data()
    url = localhost_url + url_connect
    mock.get(url, text=mocked_up_data)
    return requests.get(url)


@requests_mock.Mocker()
def mock_form_response(mock=None, url_connect=None):
    mocked_up_data = mock_suite.MockSuite("mock_form_response.json").get_data()
    url = localhost_url + url_connect
    mock.get(url, text=mocked_up_data)
    return requests.get(url)


@requests_mock.Mocker()
def mock_get_validation(mock=None, url_connect=None):
    mocked_up_data = mock_suite.MockSuite("mock_validations.json").get_data()
    url = localhost_url + url_connect
    mock.get(url, text=mocked_up_data)
    return requests.get(url)


@requests_mock.Mocker()
def mock_contributor_search_no_error(mock=None, url_connect=None):
    mocked_up_data = mock_suite.MockSuite(mocked_validation_output).get_data()
    url = localhost_url + url_connect
    mock.get(url, text=mocked_up_data)
    return requests.get(url)


@requests_mock.Mocker()
def mock_contributor_search_error_blank(mock=None, url_connect=None):
    mocked_up_data = mock_suite.MockSuite(mocked_validation_output).get_data()
    url = localhost_url + url_connect
    mock.get(url, text=mocked_up_data)
    return requests.get(url)


@requests_mock.Mocker()
def mock_contributor_search_error_populated(mock=None, url_connect=None):
    mocked_up_data = mock_suite.MockSuite(mocked_validation_output).get_data()
    url = localhost_url + url_connect
    mock.get(url, text=mocked_up_data)
    return requests.get(url)


@requests_mock.Mocker()
def mock_historic_data(mock=None, url_connect=None):
    mocked_up_data = mock_suite.MockSuite("mock_historic_data.json").get_data()
    url = localhost_url + url_connect
    mock.get(url, text=mocked_up_data)
    return requests.get(url)


@requests_mock.Mocker()
def mock_view_form_responses(mock=None, url_connect=None):
    mocked_up_data = mock_suite.MockSuite("mock_view_form_responses.json").get_data()
    url = localhost_url + url_connect
    mock.get(url, text=mocked_up_data)
    return requests.get(url)