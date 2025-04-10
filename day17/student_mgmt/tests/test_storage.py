import unittest
import os
import json
from storage import Storage

class TestStorage(unittest.TestCase):
    def setUp(self):
        self.filename = "test_students.json"
        self.storage = Storage(self.filename)

    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_save_and_load(self):
        data_to_save = [{'student_id': 1, 'name': "Divya", 'age': 22, 'grade': "B"}]
        self.storage.save(data_to_save)
        loaded_data = self.storage.load()
        self.assertEqual(loaded_data, data_to_save)

    def test_load_empty_file(self):
        open(self.filename, 'w').close()  # Create an empty file
        loaded_data = self.storage.load()
        self.assertEqual(loaded_data, [])

    def test_load_non_existent_file(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)
        loaded_data = self.storage.load()
        self.assertEqual(loaded_data, [])

    def test_load_invalid_json(self):
        with open(self.filename, 'w') as f:
            f.write("[{'student_id': 1, 'name': 'Prakash', 'age': 20, 'grade': 'A'},]") # Trailing comma makes it invalid
        loaded_data = self.storage.load()
        self.assertEqual(loaded_data, [])

if __name__ == '__main__':
    unittest.main()