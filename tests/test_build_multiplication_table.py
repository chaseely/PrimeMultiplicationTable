from unittest import TestCase
from prime_multiplication_table import build_multiplication_table


class TestBuildMultiplicationTable(TestCase):
    def test_build_multiplication_table(self):
        primes = [2, 3, 5]
        table = [[2, 3, 5],
                 [2, 4, 6, 10],
                 [3, 6, 9, 15],
                 [5, 10, 15, 25]]
        self.assertEqual(build_multiplication_table(primes), table)
