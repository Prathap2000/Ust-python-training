import json
import os

class Storage:
    def __init__(self, filename="students.json"):
        self.filename = filename

    def save(self, students_data):
        with open(self.filename, 'w') as f:
            json.dump(students_data, f, indent=4)

    def load(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    return []
        return []