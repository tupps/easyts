import requests
import json

import easyts.clients


def extract_task_info(task):
    print('\t\tId: {task_id} \t{task_name}'.format(
        task_name=task['name'],
        task_id=task['id']
    ))


def parse_tasks(data):
    return json.loads(data)


def available_projects(tasks):
    project_set = set()
    result = []
    for task in tasks:
        if task['projectName'] not in project_set:
            project_set.add(task['projectName'])
            result.append(task['projectName'])
    return result


def pretty_print_tasks(clients, tasks):
    for client in clients:
        print("===== {client_name} =====".format(
            client_name=client['name']
        ))
        client_tasks = list(filter(lambda task: task['clientId'] == client['id'], tasks))
        projects = available_projects(client_tasks)
        for project in projects:
            print("\t----- {project_name} -----".format(
                project_name=project
            ))
            project_tasks = list(filter(lambda task: task['projectName'] == project, tasks))
            for task in project_tasks:
                extract_task_info(task)
        print("")


def download_tasks(api_key):
    try:
        response = requests.get(
            url="https://api.timestamp.io/api/tasks",
            params={
                "view": "all",
            },
            headers={
                "X-API-Key": api_key,
                "Content-Type": "application/json"
            },
        )

        if response.status_code == 200:
            return parse_tasks(response.content)
        else:
            print('Response HTTP Status Code: {status_code}'.format(
                status_code=response.status_code))
            print('Response HTTP Response Body: {content}'.format(
                content=response.content))

    except requests.exceptions.RequestException:
        print('HTTP Request failed')


def get_tasks(api_key):
    tasks = download_tasks(api_key)
    clients = easyts.clients.get_clients(api_key)
    pretty_print_tasks(clients, tasks)


def get_project_id_for_task(api_key, task_id):
    tasks = download_tasks(api_key)
    matching_tasks = list(filter(lambda task: task['id'] == task_id, tasks))
    if len(matching_tasks) == 1:
        print('Found {task} in {project}'.format(
            task=matching_tasks[0]['name'],
            project=matching_tasks[0]['projectName']
        ))
        return matching_tasks[0]['projectId']
    print('Expected one project for task. Found: {found_tasks}'.format(
        found_tasks=matching_tasks
    ))
