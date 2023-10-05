"""module imports.
"""
import requests
import sys


def get_employee_todo_progress(employee_id):
    # Define the API endpoints
    base_url = "https://jsonplaceholder.typicode.com"
    user_endpoint = f"{base_url}/users/{employee_id}"
    todos_endpoint = f"{base_url}/users/{employee_id}/todos"

    try:
        # Fetch employee details
        user_response = requests.get(user_endpoint)
        user_data = user_response.json()
        employee_name = user_data["name"]

        # Fetch TODO list
        todos_response = requests.get(todos_endpoint)
        todos_data = todos_response.json()

        # Calculate progress
        total_tasks = len(todos_data)
        done_tasks = sum(1 for todo in todos_data if todo["completed"])

        # Print output
        print(
            f"Employee {employee_name} is done with tasks ({done_tasks}/{total_tasks}):")
        for todo in todos_data:
            if todo["completed"]:
                print(f"\t{todo['title']}")

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py employee_id")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Error: Employee ID must be an integer.")
