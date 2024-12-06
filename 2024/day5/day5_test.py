import unittest
from pathlib import Path

from day5 import solve_5a, solve_5b


class TestDay5(unittest.TestCase):
    def test_solve_5a(self):
        self.assertEqual(solve_5a(Path("input_test.txt")), 143)

    def test_solve_5b(self):
        self.assertEqual(solve_5b(Path("input_test.txt")), 123)
