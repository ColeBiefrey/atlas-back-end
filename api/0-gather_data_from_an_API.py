#!/usr/bin/python3
""" API getter that fetchs and utilizes information from a url """
import requests
import sys


def fetch_user_data(user_id):
    """ fetchs API information """
    user_url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    response = requests.get(user_url)
    return response.json()


def fetch_user_tasks(user_id):
    """ fetchs user tasks """
    todo_url = f'https://jsonplaceholder.typicode.com/todos/?userId={user_id}'
    response = requests.get(todo_url)
    return response.json()


def get_completed_tasks(tasks):
    """ extract tasks from main list """
    return [task['title'] for task in tasks if task['completed']]


def print_completed_tasks(user_name, completed_tasks, total_tasks):
    """ prints tasks """
    print(f'Employee {user_name} is done with tasks({len(completed_tasks)}/{total_tasks}):')
    for task in completed_tasks:
        print(f'\t {task}')


def employee_todo(user_id):
    """ function that gathers and utilizes information """
    user_data = fetch_user_data(user_id)
    user_name = user_data.get('name')
    tasks = fetch_user_tasks(user_id)
    completed_tasks = get_completed_tasks(tasks)
    print_completed_tasks(user_name, completed_tasks, len(tasks))


if __name__ == "__main__":
    if len(sys.argv) == 2:
        try:
            user_id = int(sys.argv[1])
            employee_todo(user_id)
        except ValueError:
            print("Please provide a valid number user ID.")
