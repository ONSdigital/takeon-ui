import json
import os
import boto3
from app.setup import log, api_caller
# from flask import render_template, Blueprint
# from requests.exceptions import HTTPError, ConnectionError, Timeout, RequestException
# from app.utilities.filter_validations import filter_validations
# from app.setup import log, api_caller
# from app.utilities.helpers import get_user

baw_notify_url = os.getenv('BAW_NOTIFY_URL')
baw_notify_key = os.getenv('BAW_NOTIFY_KEY')

def send_notification_to_queue(reference, period, survey):
    # save_notify_queue_url = 'https://sqs.eu-west-2.amazonaws.com/226575302242/dev-baw-save-notify'
    notification_to_send = {"reference": reference, "period": period, "survey": survey}
    # log.info("Send to Queue URL: %s", save_notify_queue_url)
    # #sqs = boto3.client("sqs", aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'), aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'), region_name=os.getenv('AWS_DEFAULT_REGION'))
    # sqs = boto3.client('sqs')
    # log.info("Sending message to notify queue...")
    # response = sqs.send_message(QueueUrl=save_notify_queue_url, MessageBody=json.dumps(notification_to_send))
    # log.info("Message sent to queue")
    # return response['MessageId']
    header = {"x-api-key": baw_notify_key}
    response = api_caller.run_validation(
        baw_notify_url, json.dumps(notification_to_send), header)
    log.info("Response from BAW SQS: %s", response)
