import requests
import json
from requests.auth import HTTPBasicAuth
from settings import get_value_setting


def send_customer_message(phone_number: str, message: str):
    headers = {
        "Content-Type": "application/json",
    }
    r = requests.post(
        f"https://iqwhatsapp.airtel.in:443/gateway/airtel-xchange/basic/whatsapp-manager/v1/session/send/text",
        auth=HTTPBasicAuth(
            get_value_setting("KONG_USERNAME"), get_value_setting("KONG_PASSWORD")
        ),
        headers=headers,
        json={
            "sessionId": "23132",
            "to": phone_number,
            "from": "918904584263",
            "message": {"text": message},
        },
    )
    return r.json()


# print(get_tokens())
