import unittest
from pathlib import Path

from day1 import solve_1a, solve_1b


class TestDay1(unittest.TestCase):
    def test_solve_1a(self):
        self.assertEqual(11, solve_1a(Path("input_test.txt")))

    def test_solve_1b(self):
        self.assertEqual(31, solve_1b(Path("input_test.txt")))
