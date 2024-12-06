import unittest
from pathlib import Path

from day6 import solve_6a, solve_6b


class TestDay5(unittest.TestCase):
    def test_solve_6a(self):
        self.assertEqual(solve_6a(Path("input_test.txt")), 41)

    def test_solve_6b(self):
        self.assertEqual(solve_6b(Path("input_test.txt")), 6)
