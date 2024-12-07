import unittest
from pathlib import Path

from day4 import solve_4a, solve_4b


class TestDay4(unittest.TestCase):
    def test_solve_4a(self):
        self.assertEqual(18, solve_4a(Path("input_test_a.txt")))

    def test_solve_4b(self):
        self.assertEqual(9, solve_4b(Path("input_test_b.txt")))
