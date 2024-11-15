#!/usr/bin/python3
""" API getter that fetchs and utilizes information from a url """
import requests
import sys


def fetch_data(url):
    """ geter for API information """
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def get_user_name(user_id):
    """ API handler for usernames """
    user_url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    user_data = fetch_data(user_url)
    return user_data.get('name')

def get_completed_tasks(user_id):
    """ API Handler for tasks """
    todo_url = f'https://jsonplaceholder.typicode.com/todos?userId={user_id}'
    todos = fetch_data(todo_url)
    return [task.get('title') for task in todos if task.get('completed')]

def employee_todo():
    """ lists todo of the employees and compeltions """
    try:
        user_id = sys.argv[1]
        name = get_user_name(user_id)
        tasks = get_completed_tasks(user_id)
        print(f'Employee {name} is done with tasks({len(tasks)}/{len(tasks)}):')
        print('\n'.join(f'\t {task}' for task in tasks))
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
    except IndexError:
        print("Please provide a user ID as a command-line argument.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    """ usage handler """
    if len(sys.argv) == 2:
        employee_todo()
    else:
        print("Usage: ./script_name.py <user_id>")
