#!/usr/bin/python3
""" API getter that fetchs and utilizes information from a url """
import requests
import sys


def get_employee_todo_progress(employee_id):
    """ fetchs API information """
    employee_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    todo_url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'

    employee_response = requests.get(employee_url)
    if employee_response.status_code != 200:
        print(f"Employee with ID {employee_id} not found.")
        return

    employee_data = employee_response.json()
    employee_name = employee_data['name']
    
    todo_response = requests.get(todo_url)
    if todo_response.status_code != 200:
        print(f"Couldn't fetch todo list for employee ID {employee_id}.")
        return

    todo_data = todo_response.json()

    total_tasks = len(todo_data)
    completed_tasks = [task for task in todo_data if task['completed']]
    num_done_tasks = len(completed_tasks)

    print(f"Employee {employee_name} is done with tasks
            ({num_done_tasks}/{total_tasks}):")

    for task in completed_tasks:
        print(f"\t {task['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("EMPLOYEE_ID")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an valid number")
        sys.exit(1)

    get_employee_todo_progress(employee_id)
