#!/usr/bin/python3
"""
   Script that returns information about an employees TO DO LIST progress,
   given their employee ID, using REST API
"""
import json
import requests
import sys


if __name__ == "__main__":

    url = 'https://jsonplaceholder.typicode.com/'

    # get id
    userId = sys.argv[1]
    # get information about the user
    user_info = requests.get(url + 'users/{}'.format(userId)).json()
    # turn into json string
    name = user_info.get('name')

    # get task information
    to_do = requests.get(url + '/users/{}/todos'.format(userId)).json()

    score = 0
    num_to_do = 0

    for task in to_do:
        num_to_do += 1
        if task['completed']:
            score += 1
    # print task list
    print("Employee {} is done with tasks({}/{}):".
          format(name, score, num_to_do))

    # print name of task
    for task in to_do:
        if task['completed']:
            print("\t {}".format(task.get('title')))

    user_dict = {}
    task_info = []

    for task in to_do:
        task_info.append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": task.get('username'),
            })
    user_dict[userId] = task_info

    fileJSON = userId + ".json"
    with open(fileJSON, "w") as Jfile:
        json.dump(user_dict, Jfile)
