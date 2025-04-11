# employee_mgmt/storage.py

import pickle

class Storage:
    def __init__(self, filename="employees.pkl"):
        self.filename = filename

    def save_data(self, data):
        try:
            with open(self.filename, 'wb') as f:
                pickle.dump(data, f)
            print("Employee data saved to disk.")
            return True
        except Exception as e:
            print(f"An error occurred while saving data: {e}")
            return False

    def load_data(self):
        try:
            with open(self.filename, 'rb') as f:
                return pickle.load(f)
        except FileNotFoundError:
            print("No employee data file found. Starting with an empty roster.")
            return {}
        except Exception as e:
            print(f"An error occurred while loading data: {e}")
            return {}