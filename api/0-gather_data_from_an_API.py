#!/usr/bin/python3

""" Rest API to engage in fetchs """
import requests
import sys


def get_name(employee_id):
    """ fetchs employee names via ID """
    url = "https://jsonplaceholder.typicode.com/users/"
    response = requests.get(url, params={'id': employee_id})
    if response.status_code == 200:
        users = response.json()
        for user in users:
            if user['id'] == employee_id:
                return user.get('name', 'No name found')
    return ('Failed to fetch name')


def get_todos(employee_id):
    """ fetchs employee list """
    url = "https://jsonplaceholder.typicode.com/todos/"
    response = requests.get(url, params={'userId': employee_id})
    if response.status_code == 200:
        todo_list = response.json()
        completed_tasks = []
        for task in todo_list:
            if task["completed"]:
                completed_tasks.append(task["title"])
        total_done = len(completed_tasks)
        total_todo = len(todo_list)

        return (total_done, total_todo, completed_tasks)
    return []


def get_employee_todo(employee_id):
    """ fetchs totals and completes of a user """
    name = get_name(employee_id)
    todos = get_todos(employee_id)
    print(
        f"Employee {name} is done with tasks("
        f"{todos[0]}/{todos[1]}):"
        )
    completed_tasks = todos[2]
    for completed_task in completed_tasks:
        print(f"\t {completed_task}")


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    get_employee_todo(employee_id)
