import unittest
from pathlib import Path

from day7 import solve_7a, solve_7b


class TestDay7(unittest.TestCase):
    def test_solve_7a(self):
        self.assertEqual(3749, solve_7a(Path("input_test.txt")))

    def test_solve_7b(self):
        self.assertEqual(11387, solve_7b(Path("input_test.txt")))
