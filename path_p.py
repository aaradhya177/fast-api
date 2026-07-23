# Import FastAPI so we can create an API.
from fastapi import FastAPI

# Create the FastAPI app.
app = FastAPI()

# Sample employee data.
# The employee number is the key, and the employee details are the value.
employees = {
    101: {"name": "Alice", "role": "Manager", "department": "HR"},
    102: {"name": "Bob", "role": "Developer", "department": "IT"},
    103: {"name": "Charlie", "role": "Designer", "department": "UI/UX"},
}

# This route accepts an employee number in the URL.
# Example: http://127.0.0.1:8000/employees/101
@app.get("/employees/{employee_number}")
def get_employee(employee_number: int):
    # Find the employee using the employee number from the URL.
    employee = employees.get(employee_number)

    # If the employee exists, return their details.
    if employee:
        return {
            "employee_number": employee_number,
            "details": employee
        }

    # If the employee number is not found, return an error message.
    return {
        "error": "Employee not found"
    }

# This route uses a query parameter instead of a path parameter.
# Example: http://127.0.0.1:8000/employees?employee_number=101
@app.get("/employees")
def search_employee(employee_number: int):
    # FastAPI gets employee_number from the query string.
    # In this URL, employee_number is 101:
    # /employees?employee_number=101
    employee = employees.get(employee_number)

    # If the employee exists, return their details.
    if employee:
        return {
            "employee_number": employee_number,
            "details": employee
        }

    # If the employee number is not found, return an error message.
    return {
        "error": "Employee not found"
    }
