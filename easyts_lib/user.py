import requests
import json


def extract_user_id(data):
    user_data = json.loads(data)
    return user_data['id']


def get_user_id(api_key):
    try:
        response = requests.get(
            url="https://api.timestamp.io/api/users/me",
            headers={
                "X-API-Key": api_key,
                "Content-Type": "application/json",
            },
        )

        if response.status_code == 200:
            return extract_user_id(response.content)
        else:
            print('User Response HTTP Status Code: {status_code}'.format(
                status_code=response.status_code))
            print('User Response HTTP Response Body: {content}'.format(
                content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')

