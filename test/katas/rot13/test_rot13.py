import unittest

from katas.rot13.rot13 import rot13


class Rot13TestCase(unittest.TestCase):

    def test_rot13(self) -> None:
        self.assertEqual(rot13("test"), "grfg")
        self.assertEqual(rot13("Test"), "Grfg")
