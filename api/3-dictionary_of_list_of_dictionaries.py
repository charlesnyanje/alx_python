#!/usr/bin/python3
"""Module importation.
"""
import json
import requests


def get_todo_data():
    # Define the base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"

    # Send a GET request to get all users
    users_url = f"{base_url}/users"
    response_users = requests.get(users_url)

    if response_users.status_code != 200:
        print("Error: Could not fetch user data")
        return

    users_data = response_users.json()

    # Initialize a dictionary to store data for all employees
    all_data = {}

    for user in users_data:
        employee_id = user['id']
        employee_name = user['name']

        # Send a GET request to get the TODO list for the employee
        todo_url = f"{base_url}/users/{employee_id}/todos"
        response_todo = requests.get(todo_url)

        if response_todo.status_code != 200:
            print(f"Error: Could not fetch TODO list for employee {employee_name}")
            continue

        todo_data = response_todo.json()

        # Store data for this employee
        employee_data = [{"username": employee_name, "task": task['title'], "completed": task['completed']} for task in todo_data]
        all_data[employee_id] = employee_data

    # Export data to JSON file
    json_filename = "todo_all_employees.json"
    with open(json_filename, 'w') as json_file:
        json.dump(all_data, json_file, indent=4)

    print(f"Data exported to {json_filename}")

if __name__ == "__main__":
    get_todo_data()
