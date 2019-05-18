import unittest

from course2.test_guass_function import TestGaussSum
from course2.test_person_function import TestPerson


def user_acceptance_test_suite():
    suite = unittest.TestSuite()
    suite.addTest(TestGaussSum('test_gass_sum_negative'))
    suite.addTest(TestPerson('test_student_set_name'))
    return suite


if __name__ == "__main__":
    user_acceptance_test_suite = user_acceptance_test_suite()
    runner = unittest.TextTestRunner()
    runner.run(user_acceptance_test_suite)
