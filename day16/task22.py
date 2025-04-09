import pickle

class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print("Marks:")
        for subject, mark in self.marks.items():
            print(f"  {subject}: {mark}")
        print("-" * 20)

    def update_marks(self, subject, new_marks):
        if subject in self.marks:
            self.marks[subject] = new_marks
            print(f"Marks for {self.name} in {subject} updated to {new_marks}")
        else:
            print(f"Subject '{subject}' not found for {self.name}")

# Create a list of Student objects with sample data
students_data = [
    Student("Alice", 101, {"Math": 92, "Science": 88, "English": 95}),
    Student("Bob", 102, {"Math": 78, "Science": 85, "History": 90}),
    Student("Charlie", 103, {"Physics": 80, "Chemistry": 75, "Computer": 98})
]

# Serialize and save the list to students.pkl
file_name = "students.pkl"
try:
    with open(file_name, 'wb') as file:
        pickle.dump(students_data, file)
    print(f"Student data successfully saved to {file_name}")
except Exception as e:
    print(f"Error saving student data: {e}")

print("\n--- Loading and Displaying Student Data ---")

# Load the student data from students.pkl
loaded_students = []
try:
    with open(file_name, 'rb') as file:
        loaded_students = pickle.load(file)
    # Display each student's details
    for student in loaded_students:
        student.display_details()
except FileNotFoundError:
    print(f"Error: File '{file_name}' not found.")
except Exception as e:
    print(f"Error loading student data: {e}")

# --- Challenge: Allow updating a student's marks and re-saving ---
print("\n--- Updating Student Marks ---")

if loaded_students:
    # Find a student to update (e.g., Alice)
    student_to_update = None
    for student in loaded_students:
        if student.name == "Alice":
            student_to_update = student
            break

    if student_to_update:
        student_to_update.update_marks("Math", 98)
        student_to_update.update_marks("Social Studies", 80) # Subject not initially present

        # Re-save the modified list
        try:
            with open(file_name, 'wb') as file:
                pickle.dump(loaded_students, file)
            print(f"\nModified student data successfully re-saved to {file_name}")
        except Exception as e:
            print(f"Error re-saving student data: {e}")

        print("\n--- Displaying Updated Student Data ---")
        # Load and display the updated data
        loaded_students_updated = []
        try:
            with open(file_name, 'rb') as file:
                loaded_students_updated = pickle.load(file)
            for student in loaded_students_updated:
                student.display_details()
        except FileNotFoundError:
            print(f"Error: File '{file_name}' not found.")
        except Exception as e:
            print(f"Error loading updated student data: {e}")
    else:
        print("Student 'Alice' not found in the loaded data.")
else:
    print("No student data loaded to update.")