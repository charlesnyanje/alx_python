# Import requests module
import requests

# Define the base URL for the API
base_url = "https://jsonplaceholder.typicode.com/users/"

# Define a function that takes an employee ID as a parameter and returns the TODO list progress
def get_todo_progress(employee_id):
  # Get the employee details from the API
  employee_response = requests.get(base_url + str(employee_id))
  # Check if the response is valid
  if employee_response.status_code == 200:
    # Parse the JSON data
    employee_data = employee_response.json()
    # Get the employee name
    employee_name = employee_data["name"]
    # Get the TODO items for the employee from the API
    todo_response = requests.get(base_url + str(employee_id) + "/todos")
    # Check if the response is valid
    if todo_response.status_code == 200:
      # Parse the JSON data
      todo_data = todo_response.json()
      # Initialize the variables for counting the tasks
      total_tasks = 0
      done_tasks = 0
      # Loop through the TODO items
      for item in todo_data:
        # Increment the total tasks
        total_tasks += 1
        # Check if the item is completed
        if item["completed"]:
          # Increment the done tasks
          done_tasks += 1
      # Print the first line of the output
      print(f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):")
      # Loop through the TODO items again
      for item in todo_data:
        # Check if the item is completed
        if item["completed"]:
          # Print the title of the completed task with a tabulation and a space before it
          print(f"\t {item['title']}")
    else:
      # Print an error message if the TODO response is invalid
      print(f"Error: Could not get TODO items for employee {employee_id}")
  else:
    # Print an error message if the employee response is invalid
    print(f"Error: Could not get employee details for ID {employee_id}")

# Get the employee ID from the command line argument
employee_id = int(input("Enter an employee ID: "))

# Call the function with the employee ID
get_todo_progress(4)
