MIN_SALARY = 10000
MAX_SALARY = 1000000

# Take user input with error handling
def take_input(label, data_type):
    while True:
        try:
            user_input = data_type(input(label))
            return user_input
        except ValueError:
            print("Please enter a valid ", data_type.__name__.lower())
# Display specific employee's information
def display_info(employees):
    emp_id = take_input("Enter the employee ID: ", int)
    for employee in employees:
        if employee["employee_id"] == emp_id:
            print("\n")
            print("Employee Id:\t\t", employee["employee_id"])
            print("Employee Name:\t\t", employee["employee_name"])
            print("Department:\t\t", employee["department"])
            print("Salary:\t\t\t", employee["salary"])
            print("Years of Experience:\t", employee["years_of_experience"])
            return
    print("Employee doesn't exist!")

# Calculate average salary of employees
def algorithm1(employees):
    total_salary = sum(employee["salary"] for employee in employees)
    avg_salary = total_salary / len(employees)
    print("Average salary is:\t", avg_salary)

# Display salary distribution for each department
def algorithm2(employees):
    dist_result = {}
    for employee in employees:
        # Insert the department if it doesn't exist using nested dictionary
        if employee["department"] not in dist_result:
            dist_result[employee["department"]] = {"total_emp": 0, "total_sal": 0}
        # Add up the counts if department already exist
        dist_result[employee["department"]]["total_emp"] += 1
        dist_result[employee["department"]]["total_sal"] += employee["salary"]
    # Iterate key value pairs through each distribution
    print("\n")
    print("|  Department  |  Total Employees  |  Average Salary  |")
    for department, info in dist_result.items():
        avg_salary = info["total_sal"] / info["total_emp"]
        # Print table format output by allocating whitespace with 'ljust()' method 
        print("| ",department.ljust(11), "| ", str(info["total_emp"]).ljust(16), "| ", str(avg_salary).ljust(13), "  |")

# Find high experience employees 
def high_exp_emp(employees):
    exp_employees = []
    for employee in employees:
        if employee["years_of_experience"] > 10:
            exp_employees.append((employee["employee_name"], employee["department"]))
    if exp_employees:
        print("Employees with more than 10 years of experience:")
        print("|  Name          |  Department  |")
        for employee in exp_employees:
            print("| ", employee[0].ljust(13), "| ", employee[1].ljust(11), "|")
    else:
        print("There are no any highly experienced employees!")

# Update employee salary
def change_salary(employees):
    emp_id = take_input("Enter the employee ID: ", int)
    # Out of range handling for salary
    new_salary = 0.0
    while not (MIN_SALARY <= new_salary <= MAX_SALARY):
        new_salary = take_input(f"Enter new salary within {MIN_SALARY} and {MAX_SALARY}: ", float)
    # Search for employee and set new salary
    for employee in employees:
        if employee["employee_id"] == emp_id:
            employee["salary"] = new_salary
            print("Salary updated for Employee ID: ", emp_id)
            print("New salary is:\t\t\t", new_salary)
            return
    print("Employee doesn't exist!")

# Main program
if __name__ == "__main__":		
    # Load employee data
    employees = [
        {"employee_id": 1, "employee_name": "Will Smith", "department": "Marketing", "salary": 52000.0, "years_of_experience": 5},
        {"employee_id": 2, "employee_name": "Justin Beiber", "department": "IT", "salary": 60000.0, "years_of_experience": 6},
        {"employee_id": 3, "employee_name": "Taylor Swift", "department": "IT", "salary": 66000.0, "years_of_experience": 8},
        {"employee_id": 4, "employee_name": "Selena Gomez", "department": "Marketing", "salary": 75000.0, "years_of_experience": 11},
        {"employee_id": 5, "employee_name": "Chrish Brown", "department": "Physics", "salary": 85000.0, "years_of_experience": 12},
    ]						
    while True:
        print("\n")
        print("1. Display Employee Info")
        print("2. Calculate Average Salary")
        print("3. Department-wise Salary Distribution")
        print("4. Find High Experience Employees")
        print("5. Update Employee Salary")
        print("6. Exit")
        choice = input("Enter your choice: ")

        match choice:
            case "1":
                display_info(employees)
            case "2":
                algorithm1(employees)
            case "3":
                algorithm2(employees)
            case "4":
                high_exp_emp(employees)
            case "5":
                change_salary(employees)
            case "6":
                break
            case _:
                print("Invalid choice!")
