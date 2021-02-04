import json
import os
import time
from flask import render_template, Blueprint, redirect, url_for
from requests.exceptions import HTTPError, ConnectionError, Timeout, RequestException
from app.utilities.filter_validations import filter_validations
from app.utilities.notify_baw import send_notification_to_queue
from app.setup import log, api_caller
from app.utilities.helpers import get_user
# from app.forms import view_form

view_form_blueprint = Blueprint(
    name='view_form', import_name=__name__, url_prefix='/contributor_search')
url = os.getenv('API_URL')
api_key = os.getenv('API_KEY')
form_view_template_HTML = "./view_form/FormView.html"

def extract_responses(data) -> dict:
    output = []
    for key in data.keys():
        if key != "action" and key != "override-checkbox":
            output.append({'question': key, 'response': data[key], 'instance': 0})
    return output

def save_form(parameters, requestform, inqcode, period, ruref):
    try:
        response_data = extract_responses(requestform)
        log.info('Response data: %s', response_data)
        # Build up JSON structure to save
        json_output = {}
        json_output["responses"] = response_data
        json_output["user"] = get_user()
        json_output["reference"] = ruref
        json_output["period"] = period
        json_output["survey"] = inqcode

        # Send the data to the business layer for processing
        log.info("Output JSON: %s", str(json_output))
        response = api_caller.save_response(parameters=parameters, data=json_output)
        log.info("Response from save request: %s", response)
        if not response == "{\"continue\":\"No question responses to save\"}":
            log.info("Data edited. Sending notification to BAW...")
            (ruref, period, inqcode)
        status_message = 'Responses saved successfully'
        return status_message
    except HTTPError as http_error:
        status_message = 'There was a problem with the HTTP call ' + http_error
        log.info('HTTP Error %s', http_error)
    except ConnectionError as connection_error:
        status_message = 'There was a problem with the connection ' + connection_error
        log.info('Connection Error %s', connection_error)
    except Timeout as timeout_error:
        status_message = 'Timeout error ' + timeout_error
        log.info('Timeout Error %s', timeout_error)
    except RequestException as requests_error:
        status_message = 'There was a problem with your request ' + requests_error + 'Please contact Data Clearing Support Team'
        log.info('Requests Error: %s', requests_error)

def validate(inqcode, period, ruref):
    log.info('save validation button pressed')
    json_data = {"survey": inqcode, "period": period,
                 "reference": ruref, "BPMvalidationCallId": "0"}
    header = {"x-api-key": api_key}
    status_message = 'Validation Run Successfully'
    try:
        response = api_caller.run_validation(
            url, json.dumps(json_data), header)
        log.info("Response from SQS: %s", response)
    except HTTPError as http_err:
        status_message = "Http Error. Unable to call URL"
        log.info('URL error occurred: %s', http_err)
    except ConnectionError as connection_err:
        status_message = "Connection Error. Unable to Connect to API Gateway"
        log.info('API request error occured: %s', connection_err)
    except Exception as e:
        status_message = 'Validation Error. Kubernetes secret does not exist or is incorrect'
        log.info('Validation Error Occurred: %s', e)
        return render_template(
            template_name_or_list="./error_templates/validate_error.html",
            error=e
        )
    return status_message
