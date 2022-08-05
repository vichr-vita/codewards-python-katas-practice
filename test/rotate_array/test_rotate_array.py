import unittest

from katas.rotate_array.rotate_array import rotate


class RotateArrayTestCase(unittest.TestCase):

    def test_rotate_array(self):
        self.assertEqual(rotate([1, 2, 3, 4, 5], 1), [5, 1, 2, 3, 4])
        self.assertEqual(rotate([1, 2, 3, 4, 5], -1), [2, 3, 4, 5, 1])
        self.assertEqual(rotate([1, 2, 3, 4, 5], 2), [4, 5, 1, 2, 3])
        self.assertEqual(rotate([1, 2, 3, 4, 5], -2), [3, 4, 5, 1, 2])
        self.assertEqual(rotate([1, 2, 3, 4, 5], 3), [3, 4, 5, 1, 2])
        self.assertEqual(rotate([1, 2, 3, 4, 5], -3), [4, 5, 1, 2, 3])
        self.assertEqual(rotate([1, 2, 3, 4, 5], 4), [2, 3, 4, 5, 1])
        self.assertEqual(rotate([1, 2, 3, 4, 5], -4), [5, 1, 2, 3, 4])
        self.assertEqual(rotate([1, 2, 3, 4, 5], 5), [1, 2, 3, 4, 5])
        self.assertEqual(rotate([1, 2, 3, 4, 5], -5), [1, 2, 3, 4, 5])
        self.assertEqual(rotate([1, 2, 3, 4, 5], 6), [5, 1, 2, 3, 4])
        self.assertEqual(rotate([1, 2, 3, 4, 5], -6), [2, 3, 4, 5, 1])
        self.assertEqual(rotate([True, True, False], 2), [True, False, True])
        self.assertEqual(rotate([1, 2, 3, 4, 5], 12478), [3, 4, 5, 1, 2])
        self.assertEqual(rotate([], 976999), [])
