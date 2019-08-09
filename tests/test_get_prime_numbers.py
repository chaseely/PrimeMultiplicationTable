from unittest import TestCase
from prime_multiplication_table import get_prime_numbers


class TestGetPrimeNumbers(TestCase):
    def test_get_prime_numbers10(self):
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        self.assertEqual(get_prime_numbers(), primes)

    def test_get_prime_numbers_not10(self):
        primes = [1, 4, 6, 8, 9, 10, 12, 14, 15, 16]
        self.assertNotEqual(get_prime_numbers(), primes)
