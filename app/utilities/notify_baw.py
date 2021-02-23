import json
import os
from uuid import uuid1
from app.setup import log, api_caller


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
        override_json_data = json.loads(override_data)
    except ValueError as error:
        log.info(f"Error with override JSON data: {error}, {override_data}")
        raise ValueError
    
    notification_to_send = [{
        "reference": override_json_data['reference'],
        "BPMvalidationCallID": "0",
        "survey": override_json_data['survey'],
        "period": override_json_data['period'],
        "status": override_json_data['status'],
        "validationPassed": override_json_data['validationPassed'],
        "selective_editing_flag": override_json_data['selective_editing_flag']}]
    header = {"x-api-key": baw_notify_override_key}
    response = api_caller.notify_override(baw_notify_override_url, json.dumps(notification_to_send), header)
    log.info("Response from BPM Notify Queue: %s", response)
