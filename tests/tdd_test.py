import unittest
import sys

sys.path.append('../')

from sort import *

class TestAbsSort(unittest.TestCase):

    def test_type(self):
        self.assertIsInstance(abs_sort([4, -30, 100, -100, 123, 1, 0, -1, -4]), list)
        self.assertIsInstance(abs_sort([4]), list)

    def test_default_case(self):
        self.assertEqual(abs_sort([4, -30, 100, -100, 123, 1, 0, -1, -4]), [123, 100, -100, -30, 4, -4, 1, -1, 0])
        self.assertEqual(abs_sort([4]), [4])
        self.assertEqual(abs_sort([]), [])



class TestAbsLambdaSort(unittest.TestCase):

    def test_type(self):
        self.assertIsInstance(abs_sort_lambda([4, -30, 100, -100, 123, 1, 0, -1, -4]), list)
        self.assertIsInstance(abs_sort_lambda([4]), list)

    def test_default_case(self):
        self.assertEqual(abs_sort_lambda([4, -30, 100, -100, 123, 1, 0, -1, -4]), [123, 100, -100, -30, 4, -4, 1, -1, 0])
        self.assertEqual(abs_sort_lambda([4]), [4])
        self.assertEqual(abs_sort_lambda([]), [])


if __name__ == '__main__':
    unittest.main()