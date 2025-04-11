from employee import Employee

class EmployeeManager:
    def __init__(self):
        self.employees = {}

    def add_employee(self, name, department, designation, gross_salary):
        employee = Employee(name, department, designation, gross_salary)
        self.employees[str(employee.id)] = employee
        return employee

    def view_all_employees(self):
        if not self.employees:
            print("No employees found in the system.")
            return
        print("\n--- All Employees ---")
        for employee_id, employee in self.employees.items():
            print(employee)
            print("-" * 30)

    def search_employee(self, employee_id):
        return self.employees.get(employee_id)

    def delete_employee(self, employee_id):
        if employee_id in self.employees:
            del self.employees[employee_id]
            print(f"Employee with ID {employee_id} has been successfully removed.")
            return True
        print(f"Employee with ID {employee_id} not found.")
        return False

    def get_all_employees_data(self):
        return [employee.to_dict() for employee in self.employees.values()]

    def load_employees(self, data):
        self.employees = {emp['id']: Employee.from_dict(emp) for emp in data}
        print("Employee data loaded successfully.")