import unittest

from katas.who_likes_it.who_likes_it import solution


class WhoLikesItTestCase(unittest.TestCase):

    def test_who_likes_it(self):
        self.assertEqual(solution([]), "no one likes this")
        self.assertEqual(solution(["Peter"]), "Peter likes this")
        self.assertEqual(solution(["Jacob", "Alex"]),
                         "Jacob and Alex like this")
        self.assertEqual(solution(["Max", "John", "Mark"]),
                         "Max, John and Mark like this")
        self.assertEqual(solution(
            ["Alex", "Jacob", "Mark", "Max"]), "Alex, Jacob and 2 others like this")
