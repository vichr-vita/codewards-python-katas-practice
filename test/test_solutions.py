import unittest

from katas.solutions import anagrams, dirReduc, fib_lesseqthan, move_zeros, pig_it, productFib, rgb, valid_parentheses


class SolutionsTestCase(unittest.TestCase):

    def test_pig_latin(self):
        self.assertEqual(pig_it('Pig latin is cool'),
                         'igPay atinlay siay oolcay')
        self.assertEqual(pig_it('This is my string'),
                         'hisTay siay ymay tringsay')

    def test_move_zeros(self):
        self.assertEqual(move_zeros([1, 3, 0, 0, 2, 4, 5, 6]), [
                         1, 3, 2, 4, 5, 6, 0, 0])

    def test_rgb(self):
        self.assertEqual(rgb(255, 255, 255), 'FFFFFF')

    def test_anagrams(self):
        self.assertEqual(
            anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']), ['aabb', 'bbaa'])
        self.assertEqual(anagrams(
            'racer', ['crazer', 'carer', 'racar', 'caers', 'racer']), ['carer', 'racer'])

    def test_dirReduc(self):
        a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
        self.assertEqual(dirReduc(a), ['WEST'])
        u = ["NORTH", "WEST", "SOUTH", "EAST"]
        self.assertEqual(dirReduc(u), ["NORTH", "WEST", "SOUTH", "EAST"])

    def test_fib_lesseqthan(self):
        self.assertEqual(fib_lesseqthan(5), [1, 1, 2, 3, 5])
        self.assertEqual(fib_lesseqthan(10), [1, 1, 2, 3, 5, 8])

    def test_productFib(self):
        self.assertEqual(productFib(4895), [55, 89, True])
        self.assertEqual(productFib(5895), [89, 144, False])
