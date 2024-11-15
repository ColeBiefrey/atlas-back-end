#!/usr/bin/python3

""" Rest API to engage in fetchs """
import csv
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


def get_username(employee_id):
    """ fetchs username of employee via ID """
    url = "https://jsonplaceholder.typicode.com/users/"
    response = requests.get(url, params={'id': employee_id})
    if response.status_code == 200:
        users = response.json()
        for user in users:
            if user['id'] == employee_id:
                return user.get('username', 'No username found')
    return ('Failed to fetch name')


def get_todos(employee_id):
    """ fetchs employee list and returns task list """
    url = "https://jsonplaceholder.typicode.com/todos/"
    response = requests.get(url, params={'userId': employee_id})
    if response.status_code == 200:
        todo_list = response.json()
        tasks = []
        for task in todo_list:
            tasks.append({"title": task["title"],
                          "completed": task["completed"]})
        return tasks
    return []


def export_to_csv(employee_id, name, tasks):
    """ exports task data to CSV """
    filename = f"{employee_id}.csv"
    with open(filename, 'w', newline='') as csvfile:
        for task in tasks:
            row = (f'"{employee_id}","{name}","'
                   f'{"True" if task["completed"] else "False"}",'
                   f'"{task["title"]}"\n')
            csvfile.write(row)


def get_employee_todo(employee_id):
    """ fetchs totals and completes of a user """
    name = get_name(employee_id)
    tasks = get_todos(employee_id)
    username = get_username(employee_id)
    print(f"Employee {name} has {len(tasks)} tasks:")
    for task in tasks:
        print(f"\t {task['title']} - "
              f"{'Completed' if task['completed'] else 'Incomplete'}")
    export_to_csv(employee_id, username, tasks)


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    get_employee_todo(employee_id)
