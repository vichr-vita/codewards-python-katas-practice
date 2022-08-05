import unittest

from katas.gloves.gloves import solution


class GlovesTestCase(unittest.TestCase):

    def test_gloves(self) -> None:
        self.assertEqual(solution(["red", "green", "red", "blue", "blue"]), 2)
        self.assertEqual(
            solution(["red", "red", "red", "red", "red", "red"]), 3)
