#!/usr/bin/python3
"""
   Script that returns information about an employees TO DO LIST progress,
   given their employee ID, using REST API
   Exports to CSV format
"""
import csv
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

    CSVfile = userId + '.csv'

    with open(CSVfile, "w", newline='') as fileCSV:
        write = csv.writer(fileCSV, delimiter=',', quoting=csv.QUOTE_ALL)
        for item in to_do:
            write.writerow([userId, name, item.get('completed'),
                            item.get('title')])
