from operator import imod

import unittest

from katas.vowels.vowels import solution


class VowelsTestCase(unittest.TestCase):

    def test_vowels(self):
        self.assertEqual(solution('Mmmm'), [])
        self.assertEqual(solution('Super'), [2, 4])
        self.assertEqual(solution('Apple'), [1, 5])
        self.assertEqual(solution('YoMama'), [1, 2, 4, 6])
