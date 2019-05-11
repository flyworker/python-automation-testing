import unittest
from course2.guass_function import gass_sum


class TestGaussSum(unittest.TestCase):
    def setUp(self):
        print("start")

    def tearDown(self):
        print("shut down")

    def test_gass_sum(self):
        print("test_gass_sum")
        self.assertEqual(gass_sum(100), 5050,"Not equal")

    @unittest.skip("Not implemented")
    def test_gass_sum_negative(self):
        self.assertEqual(gass_sum(-100), -5050)

    def test_gass_sum_string(self):
        print("test_gass_sum_string")
        self.assertEqual(gass_sum("a"), "Error,type not supported")

    def test_gass_sum_float(self):
        print("test_gass_sum_float")
        self.assertEqual(gass_sum(10.1), "Error,type not supported")


if __name__ == "__main__":
    unittest.main()
