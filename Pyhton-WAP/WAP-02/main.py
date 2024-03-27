# Function to create a list of disctionaries
def load_data():
    return [
        {"Employee ID": 1, "Employee Name": "Will Smith", "Department": "Marketing", "Salary": 52000.0, "Years of Experience": 5},
        {"Employee ID": 2, "Employee Name": "Justin Beiber", "Department": "IT", "Salary": 60000.0, "Years of Experience": 6},
        {"Employee ID": 3, "Employee Name": "Taylor Swift", "Department": "IT", "Salary": 66000.0, "Years of Experience": 8},
        {"Employee ID": 4, "Employee Name": "Selena Gomez", "Department": "Marketing", "Salary": 75000.0, "Years of Experience": 10},
        {"Employee ID": 5, "Employee Name": "Chrish Brown", "Department": "Physics", "Salary": 85000.0, "Years of Experience": 12},
    ]

# Function to display specific employee's information
def display_info(emp_id, employees):
    for employee in employees:
        if employee["Employee ID"] == emp_id:
            print("Employee ID: ", employee["Employee ID"])
            print("Employee Name: ", employee["Employee Name"])
            print("Department: ", employee["Department"])
            print("Salary: ", employee["Salary"])
            print("Years of Experience: ", employee["Years of Experience"])
            return
    print("Employee doesn't exist!")

# Algorithm 1: Calculate average salary of employees
def avg_salary(employees):
    total = sum(employee["Salary"] for employee in employees)
    avg_salary = total / len(employees)
    print("Average Salary: ", avg_salary)

# Algorithm 2: Salary distribution for each department
def salary_dist(employees):
    distribution = {}
    for employee in employees:
        # Insert the department if it doesn't exist 
        if employee["Department"] not in distribution:
            distribution[employee["Department"]] = {"total_emp": 0, "total_sal": 0}
        # Add up the counts if department already exist
        distribution[employee["Department"]]["total_emp"] += 1
        distribution[employee["Department"]]["total_sal"] += employee["Salary"]
    # Iterate through each distribution
    for department, info in distribution.items():
        avg_salary = info["total_sal"] / info["total_emp"]
        print("Department:", department)
        print("Total Employees:", info["total_emp"])
        print("Average Salary:", avg_salary)

# Function to identify high experience employees
def high_exp_emp(employees):
    high_experience_employees = []
    for employee in employees:
        if employee["Years of Experience"] > 10:
            high_experience_employees.append((employee["Employee Name"], employee["Department"]))
    if high_experience_employees:
        print("High Experience Employees:")
        for employee in high_experience_employees:
            print("Name:", employee[0], "| Department:", employee[1])
    else:
        print("No high experience employees found.")

# Function to update employee salary
def change_salary(employee_id, new_salary, employees):
    for employee in employees:
        if employee["Employee ID"] == employee_id:
            employee["Salary"] = new_salary
            print("Salary updated successfully for Employee ID:", employee_id)
            return
    print("Employee not found.")

# Main program
if __name__ == "__main__":
    employees = load_data()
    while True:
        print("\nMenu:")
        print("1. Display Employee Information")
        print("2. Calculate Average Salary")
        print("3. Department-wise Salary Distribution")
        print("4. Identify High Experience Employees")
        print("5. Update Employee Salary")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            employee_id = int(input("Enter Employee ID: "))
            display_info(employee_id,
 employees)
        elif choice == "2":
            avg_salary(employees)
        elif choice == "3":
            salary_dist(employees)
        elif choice == "4":
            high_exp_emp(employees)
        elif choice == "5":
            employee_id = int(input("Enter Employee ID: "))
            new_salary = float(input("Enter new salary: "))
            change_salary(employee_id, new_salary, employees)
        elif choice == "6":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
