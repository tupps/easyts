import requests
import json


def parse_clients(data):
    return json.loads(data)


def get_clients(api_key):
    try:
        response = requests.get(
            url="https://api.timestamp.io/api/clients/",
            headers={
                "X-API-Key": api_key,
                "Content-Type": "application/json",
            },
        )

        if response.status_code == 200:
            return parse_clients(response.content)
        else:
            print('Response HTTP Status Code: {status_code}'.format(
                status_code=response.status_code))
            print('Response HTTP Response Body: {content}'.format(
                content=response.content))

    except requests.exceptions.RequestException:
        print('HTTP Request failed')