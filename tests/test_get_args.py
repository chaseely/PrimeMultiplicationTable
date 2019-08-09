from unittest import TestCase
from prime_multiplication_table import get_args


class TestGetArgs(TestCase):
    def test_get_args_passed(self):
        self.assertEqual(get_args(['14']), 14)

    def test_get_args_not_passed(self):
        self.assertEqual(get_args([]), 10)

    def test_get_args_passed_alpha(self):
        self.assertEqual(get_args(['five']), -1)
