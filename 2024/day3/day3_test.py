import unittest
from pathlib import Path

from day3 import solve_3a, solve_3b


class TestDay3(unittest.TestCase):
    def test_solve_3a(self):
        self.assertEqual(solve_3a(Path("input_test.txt")), 161)

    def test_solve_3b(self):
        self.assertEqual(solve_3b(Path("input_test.txt")), 48)
