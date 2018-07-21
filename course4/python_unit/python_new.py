import unittest


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_plus(self):
        self.assertEqual(converting_chinese_to_english("天"),'sky1')

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

def converting_chinese_to_english(chinese):
    if chinese=="天":
        return 'sky'

if __name__ == '__main__':
    unittest.main()
