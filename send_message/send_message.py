import json
import os
import requests
import sys
from datetime import datetime

API_URL = os.environ['API_URL']
API_KEY = os.environ['API_KEY']

DEFAULT_MESSAGE = "Generated message at " + datetime.now().strftime("%x %X")

QUERY = """
mutation createMessage($message: String!) {
  createMessage(input: {message: $message}) {
    __typename
    id
    message
    createdAt
  }
}"""

def send_message(message):
    data = {
        'message': message,
    }
    #print(data)
    headers = {
        "Content-Type": "application/graphql",
        "x-api-key": API_KEY,
    }
    req = requests.post(
        url=API_URL,
        json={"query": QUERY, "variables": data},
        headers=headers)
    result = req.json()
    print(f"Response [{req.status_code}]: {result}")
    return req.status_code, result

def lambda_handler(event, context):
    message = event.get("message", DEFAULT_MESSAGE)
    status_code, result = send_message(message)
    return {
        'statusCode': status_code,
        'body': json.dumps(result)
    }

if __name__ == "__main__":
    if len(sys.argv) > 1:
        message = sys.argv[1]
    else:
        message = DEFAULT_MESSAGE
    send_message(message)
