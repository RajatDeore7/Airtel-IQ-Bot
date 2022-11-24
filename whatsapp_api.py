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
            get_value_setting("KONG_USERNAME"), get_value_setting(
                "KONG_PASSWORD")
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


def send_customer_media(phone_number: str, message: str):
    headers = {
        "Content-Type": "application/json",
    }
    r = requests.post(
        f"https://iqwhatsapp.airtel.in:443/gateway/airtel-xchange/basic/whatsapp-manager/v1/session/send/media",
        auth=HTTPBasicAuth(
            get_value_setting("KONG_USERNAME"), get_value_setting(
                "KONG_PASSWORD")
        ),
        headers=headers,
        json={
            "sessionId": "23132",
            "to": phone_number,
            "from": "918904584263",
            "mediaAttachment": {
                "type": "IMAGE",
                "id": "651983073260004",  # putmedia id;###
                "caption": message
            },
        },
    )
    return r.json()


def send_template(phone_number: str, url: str, temp_id: str):
    headers = {
        "Content-Type": "application/json",
    }
    r = requests.post(
        f"https://iqwhatsapp.airtel.in:443/gateway/airtel-xchange/basic/whatsapp-manager/v1/template/send",
        auth=HTTPBasicAuth(
            get_value_setting("KONG_USERNAME"), get_value_setting(
                "KONG_PASSWORD")
        ),
        headers=headers,
        json={
            "sessionId": "23132",
            "templateId": temp_id,
            "to": phone_number,
            "from": "918904584263",
            "message": {
                "payload": [
                    "5bbeb275-4bb5-4d11-9e61-fbf433d5c97a"
                ]
            },
            "mediaAttachment": {
                "type": "IMAGE",
                "url": url
            },
        }
    )
    return r.json()


# print(get_tokens())
