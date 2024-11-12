#!/usr/bin/python3
""" Rest API to engage in fetch """

import csv
import requests
import sys


args = sys.argv
if len(args) != 2:
    print("Usage: python script_name.py USER_ID")
    sys.exit(1)


user_id = int(args[1])
url = 'https://jsonplaceholder.typicode.com/'


user_result = requests.get(url + "users/" + str(user_id))
todos_result = requests.get(url + "todos")
user_json = user_result.json()
todos_json = todos_result.json()


EMPLOYEE_NAME = user_json["username"]


user_tasks = [task for task in todos_json
              if task["userId"] == user_id]


fields = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']

csv_file_path = f'{user_id}.csv'
with open(csv_file_path, 'w', newline='') as file:
    writer = csv.writer(file, quoting=csv.QUOTE_ALL)

    for task in user_tasks:
        completed_status = "True" if task["completed"] else "False"
        writer.writerow([user_id,
                         EMPLOYEE_NAME, completed_status, task["title"]])


class Get_Todo():
    """ condensed class that handles employee info """

    def employee_list(self):
        """ employee data getter """
        args = sys.argv
        user_id = args[1]

        url = 'https://jsonplaceholder.typicode.com/'

        user_result = requests.get(url + "users/" + user_id)
        todos_result = requests.get(url + "todos")

        user_json = user_result.json()
        todos_json = todos_result.json()

        EMPLOYEE_NAME = user_json["name"]

        NUMBER_OF_DONE_TASKS = sum(1 for task in todos_json
                                   if str(task["userId"]) == user_id
                                   and task["completed"] is True)

        TOTAL_NUMBER_OF_TASKS = sum(1 for task in todos_json
                                    if str(task["userId"]) == user_id)


        print(f"Employee {EMPLOYEE_NAME} is done with tasks"
              f"({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")

        for task in todos_json:
            if str(task["userId"]) == user_id and task["completed"] is True:
                print(f"\t {task['title']}")

if __name__ == "__main__":
    Get_Todo().employee_list()