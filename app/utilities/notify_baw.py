import json
import os
from app.setup import log, api_caller

baw_notify_url = os.getenv('BAW_NOTIFY_URL')
baw_notify_key = os.getenv('BAW_NOTIFY_KEY')

def send_notification_to_queue(reference, period, survey):

    notification_to_send = {"reference": reference, "period": period, "survey": survey}
    header = {"x-api-key": baw_notify_key}
    response = api_caller.run_validation(
        baw_notify_url, json.dumps(notification_to_send), header)
    log.info("Response from BAW Notify Queue: %s", response)
