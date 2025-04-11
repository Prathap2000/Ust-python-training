from employee_manager import EmployeeManager
from storage import Storage

def display_menu():
    print("\n--- Employee Management CLI ---")
    print("1. Add New Employee")
    print("2. View All Employees")
    print("3. Search Employee by ID")
    print("4. Delete Employee")
    print("5. Save Data to File")
    print("6. Load Data from File")
    print("7. Exit Application")
    print("Enter your choice:")

def get_employee_details():
    name = input("Enter employee's full name: ")
    department = input("Enter department: ")
    designation = input("Enter their role: ")
    while True:
        try:
            gross_salary = float(input("Enter gross monthly salary (in ₹): "))
            if gross_salary >= 0:
                break
            else:
                print("Salary cannot be negative. Please enter a valid amount.")
        except ValueError:
            print("Invalid salary input. Please enter a numerical value.")
    return name, department, designation, gross_salary

def main():
    employee_manager = EmployeeManager()
    storage = Storage()

    # Load initial data if available
    loaded_data = storage.load_data()
    employee_manager.load_employees(loaded_data)

    while True:
        display_menu()
        choice = input("> ")

        if choice == '1':
            name, department, designation, gross_salary = get_employee_details()
            employee = employee_manager.add_employee(name, department, designation, gross_salary)
            print(f"New employee '{employee.name}' added with ID: {employee.id}")
        elif choice == '2':
            employee_manager.view_all_employees()
        elif choice == '3':
            employee_id = input("Enter the Employee ID to search: ")
            employee = employee_manager.search_employee(employee_id)
            if employee:
                print("\n--- Employee Details ---")
                print(employee)
            else:
                print(f"No employee found with ID: {employee_id}")
        elif choice == '4':
            employee_id = input("Enter the ID of the employee to delete: ")
            employee_manager.delete_employee(employee_id)
        elif choice == '5':
            employee_data = employee_manager.get_all_employees_data()
            storage.save_data(employee_data)
        elif choice == '6':
            loaded_data = storage.load_data()
            employee_manager.load_employees(loaded_data)
        elif choice == '7':
            print("Exiting the Employee Management Application. Namaste!")
            break
        else:
            print("Invalid choice. Please select a valid option from the menu.")

if __name__ == "__main__":
    main()