#!/usr/bin/python3
""" Rest API to engage in fetch """

import requests
import sys


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