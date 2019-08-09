from unittest import TestCase
from prime_multiplication_table import is_remainder_zero


class TestIsRemainderZero(TestCase):
    def test_is_remainder_zero_true(self):
        self.assertTrue(is_remainder_zero(4, 2))

    def test_is_remainder_zero_false(self):
        self.assertFalse(is_remainder_zero(5, 2))
