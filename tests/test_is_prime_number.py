from unittest import TestCase
from prime_multiplication_table import is_prime_number


class TestIsPrimeNumber(TestCase):
    def test_is_prime_number2(self):
        self.assertTrue(is_prime_number(2))

    def test_is_prime_number3(self):
        self.assertTrue(is_prime_number(3))

    def test_is_prime_number5(self):
        self.assertTrue(is_prime_number(5))

    def test_is_prime_number7(self):
        self.assertTrue(is_prime_number(7))

    def test_is_prime_number11(self):
        self.assertTrue(is_prime_number(11))

    def test_is_prime_number13(self):
        self.assertTrue(is_prime_number(13))

    def test_is_prime_number17(self):
        self.assertTrue(is_prime_number(17))

    def test_is_prime_number19(self):
        self.assertTrue(is_prime_number(19))

    def test_is_prime_number23(self):
        self.assertTrue(is_prime_number(23))

    def test_is_prime_number29(self):
        self.assertTrue(is_prime_number(29))

    def test_is_prime_number0(self):
        self.assertFalse(is_prime_number(0))

    def test_is_prime_number1(self):
        self.assertFalse(is_prime_number(1))
