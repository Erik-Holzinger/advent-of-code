import unittest
from pathlib import Path

from day3 import solve_3a, solve_3b


class TestDay3(unittest.TestCase):
    def test_solve_3a(self):
        self.assertEqual(161, solve_3a(Path("input_test.txt")))

    def test_solve_3b(self):
        self.assertEqual(48, solve_3b(Path("input_test.txt")))
