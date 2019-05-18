import unittest

from course2.Person import Student, Teacher
from course2.guass_function import gass_sum


class TestPerson(unittest.TestCase):
    def setUp(self):
        print("start")

    def tearDown(self):
        print("shut down")

    def test_student_set_name(self):
        jim = Student("Jim", 20)
        jim.set_name("Ray")
        self.assertEqual(jim.name, "Ray","set name failed")

    def test_teacher_set_name(self):
        jim = Teacher("Jim", 20)
        jim.set_name("Ray")
        self.assertEqual(jim.name, "Ray.","set name failed")

    def test_teacher_get_name(self):
        jim = Teacher("Ray", 1000)
        jim.set_name("张三")
        self.assertEqual(jim.get_name(), "张三.","set name failed")

    @unittest.skip("Not implemented")
    def test_gass_sum_negative(self):
        self.assertEqual(gass_sum(-100), -5050)

if __name__ == "__main__":
    unittest.main()
