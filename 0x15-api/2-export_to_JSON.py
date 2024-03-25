#!/usr/bin/python3
"""
    A sript uses a REST API, for exports data in the JSON format.
"""
import csv
import json
import requests
import sys


if __name__ == '__main__':
    USER_ID = sys.argv[1]
    url_to_user = 'https://jsonplaceholder.typicode.com/users/' + USER_ID
    reqs = requests.get(url_to_user)
    USERNAME = reqs.json().get('username')
    url_to_task = url_to_user + '/todos'
    reqs = requests.get(url_to_task)
    tasks = reqs.json()

    dict_data = {USER_ID: []}
    for task in tasks:
        TASK_COMPLETED_STATUS = task.get('completed')
        TASK_TITLE = task.get('title')
        dict_data[USER_ID].append({
                                  "task": TASK_TITLE,
                                  "completed": TASK_COMPLETED_STATUS,
                                  "username": USERNAME})
    with open('{}.json'.format(USER_ID), 'w') as f:
        json.dump(dict_data, f)
