#!/usr/bin/python3
"""
    Fetches and displays employee's TODO list progress.

    Args:
        employee_id (int): Employee's ID.

    Prints:
        Employee's name, completed tasks, and total tasks.
"""

import requests


def get_employee_todo_progress(employee_id):
    # Make a GET request to get employee data
    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    response = requests.get(url)
    employee_data = response.json()

    # Get employee name
    employee_name = employee_data.get('name', 'Unknown')

    # Make a GET request to get TODO list
    url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    response = requests.get(url)
    todos = response.json()

    # Count total and completed tasks
    total_tasks = len(todos)
    completed_tasks = sum(1 for todo in todos if todo['completed'])

    # Print first line of output
    print(f"Employee {employee_name} is done "
          f"with tasks ({completed_tasks}/{total_tasks}):")
    # Print completed tasks
    for todo in todos:
        if todo['completed']:
            print(f'\t{todo["title"]}')


if __name__ == "__main__":
    import sys

    # Check if correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python script_name.py employee_id")
        sys.exit(1)

    # Get employee ID from command-line argument
    employee_id = sys.argv[1]

    # Call the function with the provided employee ID
    get_employee_todo_progress(employee_id)
