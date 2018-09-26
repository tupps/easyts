import requests
import json

import easyts.user
import easyts.tasks


def send_request(api_key, date, minutes, task_id, comment, user_id, project_id):
    try:
        response = requests.post(
            url="https://api.timestamp.io/api/timeEntries",
            params={
                "userId": user_id,
            },
            headers={
                "X-API-Key": api_key,
                "Content-Type": "application/json",
            },
            data=json.dumps({
                "taskId": task_id,
                "userId": user_id,
                "object": "timeEntry",
                "timeValue": str(minutes),
                "day": date.isoformat(),
                "timeUnit": "minutes",
                "createdBy": user_id,
                "comment": comment,
                "minutes": minutes,
                "projectId": 81129428
            })
        )
        if response.status_code == 200:
            print('Added {minutes} to {date} for task {task} on {project} project'.format(
                minutes=minutes,
                date=date,
                task=task_id,
                project=project_id
            ))
        else:
            print('Response HTTP Status Code: {status_code}'.format(
                status_code=response.status_code))
            print('Response HTTP Response Body: {content}'.format(
                content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


def add_time_entries(api_key, dates, minutes, task_id, comment):
    print('Dates: {dates}'.format(
        dates=dates
    ))
    print('Getting User Id...')
    user_id = easyts.user.get_user_id(api_key)
    print('User Id {user_id}'.format(user_id=user_id))
    print('Getting project id')
    project_id = easyts.tasks.get_project_id_for_task(api_key, task_id)
    print('Getting project id: {project_id}'.format(project_id=project_id))

    for date in dates:
        send_request(api_key, date, minutes, task_id, comment, user_id, project_id)
