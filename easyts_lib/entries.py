import requests
import json
import datetime

from . import user


def pretty_print_entry(entry):
    print('{day}\t{client_name}\t{project_name}\t{task_name}'.format(
        day=entry['day'],
        client_name=entry['clientName'],
        project_name=entry['projectName'],
        task_name=entry['taskName']
    ))


def print_entries(entries):
    for entry in entries:
        pretty_print_entry(entry)
    print('\nCount: {entry_count}'.format(
        entry_count=len(entries)
    ))


def filter_entries(entries, start, end):
    if start is None and end is None:
        return entries
    if start is None:
        return list(filter(lambda entry: datetime.date.fromisoformat(entry['day']) <= end, entries))
    if end is None:
        return list(filter(lambda entry: datetime.date.fromisoformat(entry['day']) >= start, entries))
    else:
        return list(filter(lambda entry: start <= datetime.date.fromisoformat(entry['day']) <= end, entries))


def parse_entries(data):
    return json.loads(data)


def send_request(api_key, start, end):
    user_id = user.get_user_id(api_key)

    try:
        response = requests.get(
            url="https://api.timestamp.io/api/timeEntries",
            params={
                "userId": user_id,
            },
            headers={
                "X-API-Key": api_key,
                "Content-Type": "application/json",
            },
        )

        if response.status_code == 200:
            entries = parse_entries(response.content)
            filtered_entries = filter_entries(entries, start, end)
            print_entries(filtered_entries)
        else:
            print('Response HTTP Status Code: {status_code}'.format(
                status_code=response.status_code))
            print('Response HTTP Response Body: {content}'.format(
                content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')