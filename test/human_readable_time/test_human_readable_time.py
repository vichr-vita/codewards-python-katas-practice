import unittest

from katas.human_readable_time.human_readable_time import make_readable


class HumanReadableTimeTestCase(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(make_readable(3600), '01:00:00')
        self.assertEqual(make_readable(0), "00:00:00")
        self.assertEqual(make_readable(5), "00:00:05")
        self.assertEqual(make_readable(60), "00:01:00")
        self.assertEqual(make_readable(86399), "23:59:59")
        self.assertEqual(make_readable(359999), "99:59:59")
