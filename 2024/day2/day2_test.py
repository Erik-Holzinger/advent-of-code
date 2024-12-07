import unittest
from pathlib import Path

from day2 import solve_2a, solve_2b


class TestDay2(unittest.TestCase):
    def test_solve_2a(self):
        self.assertEqual(2, solve_2a(Path("input_test.txt")))

    def test_solve_2b(self):
        self.assertEqual(4, solve_2b(Path("input_test.txt")))
