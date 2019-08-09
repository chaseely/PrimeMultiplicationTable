from unittest import TestCase
from prime_multiplication_table import display_table


class TestDisplayTable(TestCase):
    def test_display_table_2(self):
        table = [[2, 3], [2, 4, 6], [3, 6, 9]]
        output = '         2    3\n    2    4    6\n    3    6    9'
        self.assertEqual(display_table(table), output)
