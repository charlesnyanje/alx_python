#!/usr/bin/python3
"""Module importation.
"""
import json
import requests
import sys


def get_employee_todo_progress(employee_id):
    # Define the base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"

    # Send a GET request to get employee details
    employee_url = f"{base_url}/users/{employee_id}"
    response_employee = requests.get(employee_url)

    if response_employee.status_code != 200:
        print(f"Error: Could not fetch employee details for ID {employee_id}")
        return

    employee_data = response_employee.json()
    employee_name = employee_data['name']

    # Send a GET request to get the TODO list for the employee
    todo_url = f"{base_url}/users/{employee_id}/todos"
    response_todo = requests.get(todo_url)

    if response_todo.status_code != 200:
        print(f"Error: Could not fetch TODO list for employee {employee_name}")
        return

    todo_data = response_todo.json()

    # Calculate the number of completed tasks
    completed_tasks = [task for task in todo_data if task['completed']]
    num_completed_tasks = len(completed_tasks)
    total_tasks = len(todo_data)

    # Print employee TODO list progress
    print(f"Employee {employee_name} is done with tasks ({num_completed_tasks}/{total_tasks}):")

    # Print the titles of completed tasks
    for task in completed_tasks:
        print(f"\t{task['title']}")

    # Export data to JSON file
    json_filename = f"{employee_id}.json"
    json_data = {
        "USER_ID": [{"task": task['title'], "completed": task['completed'], "username": employee_name} for task in todo_data]
    }

    with open(json_filename, 'w') as json_file:
        json.dump(json_data, json_file, indent=4)

    print(f"Data exported to {json_filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py employee_id")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Error: Employee ID must be an integer.")
