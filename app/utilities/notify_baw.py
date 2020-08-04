import json
import os
#import boto3
from app.setup import log, api_caller

baw_notify_url = os.getenv('BAW_NOTIFY_URL')
baw_notify_key = os.getenv('BAW_NOTIFY_KEY')

def send_notification_to_queue(reference, period, survey):
    # #sqs = boto3.client("sqs", aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'), aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'), region_name=os.getenv('AWS_DEFAULT_REGION'))
    # sqs = boto3.client('sqs')
    # response = sqs.send_message(QueueUrl=save_notify_queue_url, MessageBody=json.dumps(notification_to_send))
    # return response['MessageId']
    
    notification_to_send = {"reference": reference, "period": period, "survey": survey}
    log.info("BAW URL: %s", baw_notify_url)
    header = {"x-api-key": baw_notify_key}
    response = api_caller.run_validation(
        baw_notify_url, json.dumps(notification_to_send), header)
    log.info("Response from BAW Notify Queue: %s", response)
