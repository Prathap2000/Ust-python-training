from student import Student

class StudentManager:
    def __init__(self):
        self.students = []
        self.next_student_id = 1

    def add_student(self, name, age, grade):
        student = Student(self.next_student_id, name, age, grade)
        self.students.append(student)
        self.next_student_id += 1
        return student

    def view_all_students(self):
        return self.students

    def search_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def delete_student(self, student_id):
        self.students = [student for student in self.students if student.student_id != student_id]
        return True  # Indicate successful deletion (even if not found)

    def load_students(self, students_data):
        self.students = [Student.from_dict(data) for data in students_data]
        if self.students:
            self.next_student_id = max(student.student_id for student in self.students) + 1
        else:
            self.next_student_id = 1

    def to_dict_list(self):
        return [student.to_dict() for student in self.students]