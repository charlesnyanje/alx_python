"""module imports.
"""
import csv
import requests
import sys

def get_employee_todo_progress(employee_id):
    # Define the API endpoints
    base_url = "https://jsonplaceholder.typicode.com"
    user_endpoint = f"{base_url}/users/{employee_id}"
    todos_endpoint = f"{base_url}/users/{employee_id}/todos"

    # Fetch employee details
    user_response = requests.get(user_endpoint)
    user_data = user_response.json()
    employee_name = user_data["name"]

    # Fetch TODO list
    todos_response = requests.get(todos_endpoint)
    todos_data = todos_response.json()

    # Calculate progress
    total_tasks = len(todos_data)
    done_tasks = sum(1 for task in todos_data if task["completed"])

    # Create CSV file
    csv_filename = f"{employee_id}.csv"
    with open(csv_filename, "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in todos_data:
            csv_writer.writerow([employee_id, employee_name, task["completed"], task["title"]])

    print(f"CSV file '{csv_filename}' created successfully!")

# Example usage: Replace 1 with the desired employee ID
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py employee_id")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Error: Employee ID must be an integer.")

