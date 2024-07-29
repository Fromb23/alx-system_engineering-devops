#!/usr/bin/python3
"""
    gather employee data from API
"""
import requests
import sys

REST_API = "https://jsonplaceholder.typicode.com"


def get_employee_todo_progress(employee_id):
    # Fetch employer details
    employee_url = f'{REST_API}/users/{employee_id}'
    employee_response = requests.get(employee_url)
    employee = employee_response.json()
    employee_name = employee.get('name')

    # Get all TODO task to fetch user by ID
    todos_url = f'{REST_API}/todos'
    todos_response = requests.get(todos_url)
    todos = todos_response.json()
    tasks = [task for task in todos if task.get('userId') == employee_id]
    completed_tasks = [task for task in tasks if task.get('completed')]

    # Print the progress
    total_tasks = len(tasks)
    number_of_done_tasks = len(completed_tasks)
    print(
        f'Employee {employee_name} is done with '
        f'tasks({number_of_done_tasks}/{total_tasks}):'
    )

    # Print the title of completed tasks
    for task in completed_tasks:
        print(f'\t {task["title"]}')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1].isdigit():
            employee_id = int(sys.argv[1])
            get_employee_todo_progress(employee_id)
        else:
            print("Employee id must be an integer")
            sys.exit(1)
    else:
        print('Usage: python script.py <employee_id>')
        sys.exit(1)
