import json
import re
import requests

HEADERS = {"Content-type": "application/json; charset=utf-8"}


def load_file_config() -> dict:
    with open("config.json", "r") as file_:
        data = json.load(file_)
    return data


def clear_url(url: str) -> str:
    segments = url.split('/')
    for segment in segments:
        if re.search('\\d', segment):
            url = url.replace(segment, "?")
    return url


def validate_grant(endpoint: str, method: str, id_rol: int) -> bool:
    has_grant = False
    data_config = load_file_config()
    url = data_config.get("url-backend-security") + f'/rol/validate/{id_rol}'
    body = {
        "url": endpoint,
        "method": method
    }
    response = requests.get(url, headers=HEADERS, json=body)
    if response.status_code == 200:
        has_grant = True
    return has_grant

