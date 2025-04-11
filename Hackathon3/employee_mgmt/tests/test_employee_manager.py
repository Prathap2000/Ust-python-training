import unittest
from employee_manager import EmployeeManager
from employee import Employee
import uuid
from io import StringIO
import sys

class TestEmployeeManager(unittest.TestCase):

    def setUp(self):
        self.manager = EmployeeManager()
        self.employee1 = Employee("Deepika Patel", "HR", "Manager", 80000)
        self.employee2 = Employee("Arjun Singh", "Finance", "Senior Analyst", 95000)
        self.manager.employees[str(self.employee1.id)] = self.employee1
        self.manager.employees[str(self.employee2.id)] = self.employee2

    def test_add_employee(self):
        employee3 = self.manager.add_employee("Sneha Reddy", "Sales", "Associate", 60000)
        self.assertIn(str(employee3.id), self.manager.employees)
        self.assertEqual(len(self.manager.employees), 3)

    def test_view_all_employees(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        self.manager.view_all_employees()
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        self.assertIn("Deepika Patel", output)
        self.assertIn("Arjun Singh", output)

    def test_view_all_employees_empty(self):
        empty_manager = EmployeeManager()
        captured_output = StringIO()
        sys.stdout = captured_output
        empty_manager.view_all_employees()
        sys.stdout = sys.__stdout__
        self.assertEqual("No employees found in the system.\n", captured_output.getvalue())

    def test_search_employee_found(self):
        employee = self.manager.search_employee(str(self.employee1.id))
        self.assertEqual(employee.name, "Deepika Patel")

    def test_search_employee_not_found(self):
        employee = self.manager.search_employee(str(uuid.uuid4()))
        self.assertIsNone(employee)

    def test_delete_employee_success(self):
        initial_count = len(self.manager.employees)
        captured_output = StringIO()
        sys.stdout = captured_output
        result = self.manager.delete_employee(str(self.employee1.id))
        sys.stdout = sys.__stdout__
        self.assertTrue(result)
        self.assertEqual(len(self.manager.employees), initial_count - 1)
        self.assertNotIn(str(self.employee1.id), self.manager.employees)
        self.assertIn("Employee with ID", captured_output.getvalue())

    def test_delete_employee_not_found(self):
        initial_count = len(self.manager.employees)
        captured_output = StringIO()
        sys.stdout = captured_output
        result = self.manager.delete_employee(str(uuid.uuid4()))
        sys.stdout = sys.__stdout__
        self.assertFalse(result)
        self.assertEqual(len(self.manager.employees), initial_count)
        self.assertIn("not found.", captured_output.getvalue())

    def test_get_all_employees_data(self):
        data = self.manager.get_all_employees_data()
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]['name'], "Deepika Patel")
        self.assertEqual(data[1]['department'], "Finance")

    def test_load_employees(self):
        new_manager = EmployeeManager()
        data_to_load = [
            {'id': str(uuid.uuid4()), 'name': 'Vikram Joshi', 'department': 'Tech', 'designation': 'Lead Engineer', 'gross_salary': 120000},
            {'id': str(uuid.uuid4()), 'name': 'Aishwarya Nair', 'department': 'Admin', 'designation': 'Officer', 'gross_salary': 55000}
        ]
        captured_output = StringIO()
        sys.stdout = captured_output
        new_manager.load_employees(data_to_load)
        sys.stdout = sys.__stdout__
        self.assertEqual(len(new_manager.employees), 2)
        self.assertEqual(list(new_manager.employees.values())[0].name, 'Vikram Joshi')
        self.assertIn("loaded successfully.", captured_output.getvalue())

if __name__ == '__main__':
    unittest.main()