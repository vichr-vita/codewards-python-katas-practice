import unittest

from katas.highest_and_lowest.highest_and_lowest import high_and_low


class HighestAndLowestTestCase(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(high_and_low('1 2 3 4 5'), '5 1')
        self.assertEqual(high_and_low('1 2 -3 4 5'), '5 -3')
        self.assertEqual(high_and_low('1 9 3 4 -5'), '9 -5')
