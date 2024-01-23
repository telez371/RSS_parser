import requests
from django.conf import settings


def gql(file_path):
    with open(file_path, 'r') as file:
        return file.read()


def send_fibery_message(title, price, description, fibery_config):
    if price is None:
        return None

    token = settings.FIBERY_API_KEY
    url = fibery_config.fibery_url
    query = gql("sending_messages/queryFibery.gql")

    variables = {
        "name": title,
        "value": price,
        "comment": description,
    }

    headers = {
        "Authorization": f"Token {token}",
        "Content-Type": "application/json"
    }

    payload = {
        "query": query,
        "variables": variables
    }

    requests.post(url, headers=headers, json=payload)





