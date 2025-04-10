import unittest
from student import Student

class TestStudent(unittest.TestCase):
    def test_student_creation(self):
        student = Student(1, "Alice", 20, "A")
        self.assertEqual(student.student_id, 1)
        self.assertEqual(student.name, "Alice")
        self.assertEqual(student.age, 20)
        self.assertEqual(student.grade, "A")

    def test_student_str(self):
        student = Student(2, "Bob", 22, "B")
        expected_str = "ID: 2, Name: Bob, Age: 22, Grade: B"
        self.assertEqual(str(student), expected_str)

    def test_student_to_dict(self):
        student = Student(3, "Charlie", 19, "C")
        expected_dict = {'student_id': 3, 'name': "Charlie", 'age': 19, 'grade': "C"}
        self.assertEqual(student.to_dict(), expected_dict)

    def test_student_from_dict(self):
        data = {'student_id': 4, 'name': "David", 'age': 21, 'grade': "B"}
        student = Student.from_dict(data)
        self.assertEqual(student.student_id, 4)
        self.assertEqual(student.name, "David")
        self.assertEqual(student.age, 21)
        self.assertEqual(student.grade, "B")

if __name__ == '__main__':
    unittest.main()