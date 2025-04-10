import unittest
from student_manager import StudentManager
from student import Student

class TestStudentManager(unittest.TestCase):
    def setUp(self):
        self.manager = StudentManager()

    def test_add_student(self):
        student = self.manager.add_student("Anjali", 20, "A")
        self.assertEqual(len(self.manager.students), 1)
        self.assertEqual(student.student_id, 1)
        self.assertEqual(student.name, "Anjali")

    def test_view_all_students(self):
        self.manager.add_student("Vikram", 22, "B")
        self.manager.add_student("Shalini", 19, "C")
        students = self.manager.view_all_students()
        self.assertEqual(len(students), 2)
        self.assertIsInstance(students[0], Student)
        self.assertEqual(students[0].name, "Vikram")
        self.assertEqual(students[1].name, "Shalini")

    def test_search_student_found(self):
        self.manager.add_student("Ganesh", 21, "B")
        student = self.manager.search_student(1)
        self.assertIsNotNone(student)
        self.assertEqual(student.name, "Ganesh")

    def test_search_student_not_found(self):
        student = self.manager.search_student(99)
        self.assertIsNone(student)

    def test_delete_student_found(self):
        self.manager.add_student("Meera", 20, "A")
        initial_count = len(self.manager.students)
        self.assertTrue(self.manager.delete_student(1))
        self.assertEqual(len(self.manager.students), initial_count - 1)
        self.assertIsNone(self.manager.search_student(1))

    def test_delete_student_not_found(self):
        initial_count = len(self.manager.students)
        self.assertTrue(self.manager.delete_student(99)) # Should still return True
        self.assertEqual(len(self.manager.students), initial_count)

    def test_load_students(self):
        data = [{'student_id': 1, 'name': "Suresh", 'age': 23, 'grade': "C"},
                {'student_id': 2, 'name': "Lakshmi", 'age': 20, 'grade': "A"}]
        self.manager.load_students(data)
        self.assertEqual(len(self.manager.students), 2)
        self.assertEqual(self.manager.students[0].name, "Suresh")
        self.assertEqual(self.manager.next_student_id, 3)

    def test_load_students_empty_file(self):
        self.manager.load_students([])
        self.assertEqual(len(self.manager.students), 0)
        self.assertEqual(self.manager.next_student_id, 1)

    def test_to_dict_list(self):
        self.manager.add_student("Kavya", 21, "B")
        self.manager.add_student("Rohit", 19, "A")
        dict_list = self.manager.to_dict_list()
        self.assertEqual(len(dict_list), 2)
        self.assertEqual(dict_list[0]['name'], "Kavya")
        self.assertEqual(dict_list[1]['age'], 19)

if __name__ == '__main__':
    unittest.main()