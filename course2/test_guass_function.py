import unittest
from course2.guass_function import *


class test_GassSum(unittest.TestCase):
    def test_gass_sum(self):
        self.assertEqual(gass_sum(100), 5050)

    def test_gass_sum_negative(self):
        self.assertEqual(gass_sum(-100), -5050)

    def test_gass_sum_string(self):
        self.assertEqual(gass_sum("a"), "Error,type not supported")

    def test_gass_sum_float(self):
        self.assertEqual(gass_sum(10.1), "Error,type not supported")

if __name__ == "__main__":
    unittest.main()
