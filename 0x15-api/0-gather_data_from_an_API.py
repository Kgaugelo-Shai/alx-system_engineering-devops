#!/usr/bin/python3
"""
   Script that returns information about an employees TO DO LIST progress,
   given their employee ID, using REST API
"""
import sys
import requests
import json


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

    for task in to_do:
        if task['completed']:
            score += 1

    # print task list
    print("{} is done with tasks({}/{}):".format(name, score, len(user_info)))

    # print name of task
    for task in to_do:
        if task['completed']:
            print("\t {}".format(task.get('title')))
