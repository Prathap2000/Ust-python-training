import unittest
import os
import uuid
from storage import Storage
from io import StringIO
import sys

class TestStorage(unittest.TestCase):

    def setUp(self):
        self.storage = Storage("test_employees.pkl")
        self.test_data = {
            str(uuid.uuid4()): {'name': 'Kavya Menon', 'department': 'R&D', 'designation': 'Scientist', 'gross_salary': 110000},
            str(uuid.uuid4()): {'name': 'Suresh Kumar', 'department': 'Operations', 'designation': 'Supervisor', 'gross_salary': 70000}
        }

    def tearDown(self):
        # Clean up the test file after each test
        if os.path.exists(self.storage.filename):
            os.remove(self.storage.filename)

    def test_save_data(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        result = self.storage.save_data(self.test_data)
        sys.stdout = sys.__stdout__
        self.assertTrue(result)
        self.assertTrue(os.path.exists(self.storage.filename))
        self.assertIn("saved to disk.", captured_output.getvalue())

    def test_load_data_existing_file(self):
        self.storage.save_data(self.test_data)
        loaded_data = self.storage.load_data()
        self.assertEqual(len(loaded_data), len(self.test_data))
        self.assertIn(list(self.test_data.keys())[0], loaded_data)

    def test_load_data_non_existent_file(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        loaded_data = self.storage.load_data()
        sys.stdout = sys.__stdout__
        self.assertEqual(loaded_data, {})
        self.assertIn("No employee data file found", captured_output.getvalue())

    def test_save_and_load_round_trip(self):
        self.storage.save_data(self.test_data)
        loaded_data = self.storage.load_data()
        self.assertEqual(loaded_data, self.test_data)

if __name__ == '__main__':
    unittest.main()