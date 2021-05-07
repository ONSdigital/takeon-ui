import json
import os
import requests
from uuid import uuid1
from app.setup import log, api_caller
from app.utilities.helpers import validate_json


baw_notify_url = os.getenv('BAW_NOTIFY_URL')
baw_notify_key = os.getenv('BAW_NOTIFY_KEY')
baw_notify_override_url = os.getenv('BAW_NOTIFY_OVERRIDE_URL')
baw_notify_override_key = os.getenv('BAW_NOTIFY_OVERRIDE_KEY')


def send_notification_to_queue(reference, period, survey):

    notification_to_send = [{
        "response": str(uuid1()),
        "reference": reference,
        "period": period,
        "survey": survey,
        "duplicateFlag": False}]
    header = {"x-api-key": baw_notify_key}
    response = api_caller.run_validation(
        baw_notify_url, json.dumps(notification_to_send), header)
    log.info("Response from BAW Notify Queue: %s", response)


def send_override_notification_to_queue(override_data):
    try:
        override_json_data = validate_json(override_data)
        header = {"x-api-key": baw_notify_override_key}
        notification_to_send = build_notify_data_to_send(override_json_data=override_json_data)
        response = api_caller.notify_override(baw_notify_override_url, json.dumps(notification_to_send), header)
        log.info("Response from BPM Notify Queue: %s", response)

        ''' raise exceptions up the stack '''
    except KeyError as error:
        log.error(f'Error with override JSON data {error}')
        raise KeyError(error)
    except ValueError as error:
        log.error(f"Invalid JSON: {error}")
        raise ValueError(error)
    except requests.exceptions.RequestException as error:
        log.error(f'Error with call to Override endpoint {error}')
        raise requests.exceptions.RequestException(error)
    except Exception as error:
        raise Exception(error)


def build_notify_data_to_send(override_json_data):
    try:
        notification_to_send = {
                                "reference": override_json_data['reference'],
                                "survey": override_json_data['survey'],
                                "period": override_json_data['period'],
                                "status": override_json_data['status'],
                                "error": None,
                                "selective_editing_flag": None}
    except KeyError as error:
        raise KeyError(error)
    return notification_to_send
