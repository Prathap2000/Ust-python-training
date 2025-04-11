import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.employee = Employee("Priya Sharma", "Marketing", "Executive", 75000)

    def test_employee_creation(self):
        self.assertIsNotNone(self.employee.id)
        self.assertEqual(self.employee.name, "Priya Sharma")
        self.assertEqual(self.employee.department, "Marketing")
        self.assertEqual(self.employee.designation, "Executive")
        self.assertEqual(self.employee.gross_salary, 75000)

    def test_calculate_net_salary(self):
        # Tax = 75000 * 0.1 = 7500
        # Bonus = 75000 * 0.05 = 3750
        # Net Salary = 75000 - 7500 + 3750 = 71250
        self.assertAlmostEqual(self.employee.calculate_net_salary(), 71250.0)

    def test_employee_to_dict(self):
        employee_dict = self.employee.to_dict()
        self.assertEqual(employee_dict['name'], "Priya Sharma")
        self.assertEqual(employee_dict['gross_salary'], 75000)
        self.assertIn('id', employee_dict)

    def test_employee_from_dict(self):
        employee_dict = {
            'name': 'Rahul Verma',
            'department': 'Engineering',
            'designation': 'Team Lead',
            'gross_salary': 90000
        }
        new_employee = Employee.from_dict(employee_dict)
        self.assertEqual(new_employee.name, 'Rahul Verma')
        self.assertEqual(new_employee.department, 'Engineering')
        self.assertEqual(new_employee.gross_salary, 90000)

if __name__ == '__main__':
    unittest.main()