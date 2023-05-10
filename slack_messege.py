import requests
import json

def send_slack_message(payload, webhook):
    """Send a Slack message to a channel via a webhook. 
    
    Args:
        payload (dict): Dictionary containing Slack message, i.e. {"text": "This is a test"}
        webhook (str): Full Slack webhook URL for your chosen channel. 
    
    Returns:
        HTTP response code, i.e. <Response [503]>
    """

    return requests.post(webhook, json.dumps(payload))

webhook = "https://hooks.slack.com/services/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"

messege = input("Enter a messege : ")
payload = {"text": messege}
send_slack_message(payload, webhook)