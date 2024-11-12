#!/usr/bin/python3
""" API to engage in fetchs """
import requests
import sys


def TODO_list_progress(employee_id):
""" fetchs employee data """
    api_url = "https://jsonplaceholder.typicode.com"
    users_url = f"{api_url}/users/{employee_id}"
    todos_url = f"{api_url}/todos"

    get_employee_name = requests.get(users_url)
    employee_name = get_employee_name.json().get('name')

    params = {'userId': employee_id}
    todos_total = requests.get(todos_url, params=params)
    todos = todos_total.json()
    finished_tasks = [todo for todo in todos if todo['completed']]

    print(
        f"Employee {employee_name} is done with tasks"
        f"({len(finished_tasks)}/{len(todos)}):"
    )
    for task in finished_tasks:
        print(f"\t {task['title']}")


if __name__ == "__main__":

    TODO_list_progress(int(sys.argv[1]))
