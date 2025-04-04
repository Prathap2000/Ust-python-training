import json

class Person(object):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"


class Employee(Person):
    def __init__(self, name, age, gender, emp_id, department, salary):
        super().__init__(name, age, gender)
        self.emp_id = emp_id
        self.department = department
        self.salary = salary

    def get_details(self):
        return f"{super().get_details()}, Emp ID: {self.emp_id}, Department: {self.department}, Salary: {self.salary}"

    def is_eligible_for_bonus(self):
        return self.salary < 50000

    @classmethod
    def from_string(cls, data_string):
        name, age, gender, emp_id, department, salary = data_string.split(',')
        return cls(name, int(age), gender, emp_id, department, int(salary))

    @staticmethod
    def bonus_policy():
        print("Employees with salary less than 50000 are eligible for a bonus.")
        


class Department(object):
    def __init__(self, name, employees=None):
        self.name = name
        self.employees = employees if employees is not None else []

    def add_employee(self, employee):
        self.employees.append(employee)

    def get_average_salary(self):
        if not self.employees:
            return 0
        total_salary = sum(employee.salary for employee in self.employees)
        return total_salary / len(self.employees)

    def get_all_employees(self):
        return [employee.get_details() for employee in self.employees]


def save_to_json(employees, filename="employees.json"):
    data = {"employees": []}
    for emp in employees:
        data["employees"].append({
            "name": emp.name,
            "age": emp.age,
            "gender": emp.gender,
            "emp_id": emp.emp_id,
            "department": emp.department,
            "salary": emp.salary
        })
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


def load_from_json(filename="employees.json"):
    employees = []
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
            for emp_data in data["employees"]:
                emp = Employee(
                    emp_data["name"],
                    emp_data["age"],
                    emp_data["gender"],
                    emp_data["emp_id"],
                    emp_data["department"],
                    emp_data["salary"]
                )
                employees.append(emp)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.  Returning an empty list.")
    return employees