#!/usr/bin/python3

import requests
import csv


def get_employee_todo_progress(employee_id):
    """
    Fetches and displays employee's TODO list progress.

    Args:
        employee_id (int): Employee's ID.

    Prints:
        Employee's name, completed tasks, and total tasks.
    """
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
    completed_tasks = sum(1 for todo in todos if todo.get('completed', False))

    # Export data to CSV
    export_to_csv(employee_id, employee_name, todos)


def export_to_csv(employee_id, employee_name, todos):
    """
    Exports tasks data to a CSV file.

    Args:
        employee_id (int): Employee's ID.
        employee_name (str): Employee's name.
        todos (list): List of todos.

    Returns:
        None
    """
    file_name = f"{employee_id}.csv"
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([employee_id, employee_name,
                             todo.get('completed', False),
                             todo.get('title', 'No Title')])


if __name__ == "__main__":
    import sys

    # Check if correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python script_name.py employee_id")
        sys.exit(1)

    # Get employee ID from command-line argument
    employee_id = int(sys.argv[1])

    # Call the function with the provided employee ID
    get_employee_todo_progress(employee_id)
