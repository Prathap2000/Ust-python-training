from student import Student
from student_manager import StudentManager
from storage import Storage

def display_students(students):
    if not students:
        print("No students to display.")
    else:
        for student in students:
            print(student)

def main():
    manager = StudentManager()
    store = Storage()

    saved_students = store.load()
    manager.load_students(saved_students)

    while True:
        print("\nStudent Management System CLI")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student by ID")
        print("4. Delete Student by ID")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter student name: ")
            try:
                age = int(input("Enter student age: "))
                grade = input("Enter student grade: ")
                manager.add_student(name, age, grade)
                store.save(manager.to_dict_list())
                print("Student added successfully.")
            except ValueError:
                print("Invalid age. Please enter a number.")
        elif choice == '2':
            students = manager.view_all_students()
            display_students(students)
        elif choice == '3':
            try:
                student_id = int(input("Enter student ID to search: "))
                student = manager.search_student(student_id)
                if student:
                    print(student)
                else:
                    print(f"Student with ID {student_id} not found.")
            except ValueError:
                print("Invalid student ID. Please enter a number.")
        elif choice == '4':
            try:
                student_id = int(input("Enter student ID to delete: "))
                if manager.delete_student(student_id):
                    store.save(manager.to_dict_list())
                    print(f"Student with ID {student_id} deleted successfully.")
                else:
                    print(f"Student with ID {student_id} not found.")
            except ValueError:
                print("Invalid student ID. Please enter a number.")
        elif choice == '5':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()