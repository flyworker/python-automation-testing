import unittest

from course2.Person import Student
from course2.guass_function import gass_sum


class TestGaussSum(unittest.TestCase):
    def setUp(self):
        print("start")

    def tearDown(self):
        print("shut down")

    def test_student_set_name(self):
        jim = Student("Jim", 20)
        jim.set_name("Ray")
        self.assertEqual(jim.name, "Ray","set name failed")

    @unittest.skip("Not implemented")
    def test_gass_sum_negative(self):
        self.assertEqual(gass_sum(-100), -5050)

if __name__ == "__main__":
    unittest.main()
