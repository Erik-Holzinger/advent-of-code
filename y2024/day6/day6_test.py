import unittest
from pathlib import Path

from day6 import solve_6a, solve_6b


class TestDay6(unittest.TestCase):
    def test_solve_6a(self):
        self.assertEqual(41, solve_6a(Path("input_test.txt")))

    def test_solve_6b(self):
        self.assertEqual(6, solve_6b(Path("input_test.txt")))
