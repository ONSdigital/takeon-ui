import json
import os
import boto3
# from flask import render_template, Blueprint
# from requests.exceptions import HTTPError, ConnectionError, Timeout, RequestException
# from app.utilities.filter_validations import filter_validations
# from app.setup import log, api_caller
# from app.utilities.helpers import get_user

def send_notification_to_queue(reference, period, survey):
    # session = boto3.Session(
    #     aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'), 
    #     aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'), 
    #     region_name=os.getenv('AWS_DEFAULT_REGION'))
    save_notify_queue_url = 'https://sqs.eu-west-2.amazonaws.com/226575302242/dev-baw-save-notify'
    notification_to_send = {"reference": reference, "period": period, "survey": survey}

    sqs = boto3.client("sqs", aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'), aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'), region_name=os.getenv('AWS_DEFAULT_REGION'))
    # sqs = session.resource('sqs')
    response = sqs.send_message(QueueUrl=save_notify_queue_url, MessageBody=json.dumps(notification_to_send))
    return response