import unittest
from pathlib import Path

from day10 import solve_10a, solve_10b


class TestDay10(unittest.TestCase):
    def test_solve_10a(self):
        self.assertEqual(36, solve_10a(Path("input_test.txt")))

    def test_solve_10b(self):
        self.assertEqual(81, solve_10b(Path("input_test.txt")))
