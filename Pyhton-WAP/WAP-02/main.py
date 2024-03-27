# Function to load data
def load_data():
    return [
        {"Employee ID": 1, "Employee Name": "Will Smith", "Department": "Marketing", "Salary": 52000.0, "Years of Experience": 5},
        {"Employee ID": 2, "Employee Name": "Justin Beiber", "Department": "IT", "Salary": 60000.0, "Years of Experience": 6},
        {"Employee ID": 3, "Employee Name": "Taylor Swift", "Department": "IT", "Salary": 66000.0, "Years of Experience": 8},
        {"Employee ID": 4, "Employee Name": "Selena Gomez", "Department": "Marketing", "Salary": 75000.0, "Years of Experience": 10},
        {"Employee ID": 5, "Employee Name": "Chrish Brown", "Department": "Physics", "Salary": 85000.0, "Years of Experience": 12},
    ]

# Function to display employee information
def display_employee_info(employee_id, dataset):
    for employee in dataset:
        if employee["Employee ID"] == employee_id:
            print("Employee ID:", employee["Employee ID"])
            print("Employee Name:", employee["Employee Name"])
            print("Department:", employee["Department"])
            print("Salary:", employee["Salary"])
            print("Years of Experience:", employee["Years of Experience"])
            return
    print("Employee not found.")

# Algorithm 1: Calculate Average Salary
def calculate_average_salary(dataset):
    total_salary = sum(employee["Salary"] for employee in dataset)
    average_salary = total_salary / len(dataset)
    print("Average Salary:", average_salary)

# Algorithm 2: Department-wise Salary Distribution
def department_salary_distribution(dataset):
    department_salary_distribution = {}
    for employee in dataset:
        if employee["Department"] not in department_salary_distribution:
            department_salary_distribution[employee["Department"]] = {"total_employees": 0, "total_salary": 0}
        department_salary_distribution[employee["Department"]]["total_employees"] += 1
        department_salary_distribution[employee["Department"]]["total_salary"] += employee["Salary"]

    for department, info in department_salary_distribution.items():
        average_salary = info["total_salary"] / info["total_employees"]
        print("Department:", department)
        print("Total Employees:", info["total_employees"])
        print("Average Salary:", average_salary)

# Function to identify high experience employees
def identify_high_experience_employees(dataset):
    high_experience_employees = []
    for employee in dataset:
        if employee["Years of Experience"] > 10:
            high_experience_employees.append((employee["Employee Name"], employee["Department"]))
    if high_experience_employees:
        print("High Experience Employees:")
        for employee in high_experience_employees:
            print("Name:", employee[0], "| Department:", employee[1])
    else:
        print("No high experience employees found.")

# Function to update employee salary
def update_employee_salary(employee_id, new_salary, dataset):
    for employee in dataset:
        if employee["Employee ID"] == employee_id:
            employee["Salary"] = new_salary
            print("Salary updated successfully for Employee ID:", employee_id)
            return
    print("Employee not found.")

# Main program
if __name__ == "__main__":
    dataset = load_data()
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
            display_employee_info(employee_id,
 dataset)
        elif choice == "2":
            calculate_average_salary(dataset)
        elif choice == "3":
            department_salary_distribution(dataset)
        elif choice == "4":
            identify_high_experience_employees(dataset)
        elif choice == "5":
            employee_id = int(input("Enter Employee ID: "))
            new_salary = float(input("Enter new salary: "))
            update_employee_salary(employee_id, new_salary, dataset)
        elif choice == "6":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
