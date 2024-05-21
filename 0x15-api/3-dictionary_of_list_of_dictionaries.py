#!/usr/bin/python3
"""
   Script that returns information about an employees TO DO LIST progress,
   given their employee ID, using REST API
   Creates a dictionary list of dictionaries
"""
import json
import requests
import sys


if __name__ == "__main__":

    url = 'https://jsonplaceholder.typicode.com/'

    users = requests.get(url + "users").json()
    to_dos = requests.get(url + "todos").json()
    all_todos = {}

    for user in users:
        tasks = []
        for task in to_dos:
            if task.get('userId') == user.get('id'):
                dict_task = {"username": user.get('username'),
                             "task": task.get('title'),
                             "completed": task.get('completed'),
                             }
                tasks.append(dict_task)
        all_todos[user.get('id')] = tasks

    fileJSON = 'todo_all_employees.json'

    with open(fileJSON, 'w') as f:
        json.dump(all_todos, f)
