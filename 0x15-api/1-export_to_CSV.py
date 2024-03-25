#!/usr/bin/python3
"""
    A Script that, uses a REST API, for exporting data in the CSV format.
"""
import csv
import requests
import sys

if __name__ == '__main__':
    user = sys.argv[1]
    url_user = 'https://jsonplaceholder.typicode.com/users/' + user
    reqs = requests.get(url_user)
    """ANYTHING"""
    user_name = reqs.json().get('username')
    task = url_user + '/todos'
    reqs = requests.get(task)
    tasks = reqs.json()

    with open('{}.csv'.format(user), 'w') as csvfile:
        for task in tasks:
            completed = task.get('completed')
            """Complete"""
            title_task = task.get('title')
            """Done"""
            csvfile.write('"{}","{}","{}","{}"\n'.format(
                user, user_name, completed, title_task))
