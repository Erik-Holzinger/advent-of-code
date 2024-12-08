import unittest
from pathlib import Path

from day8 import solve_8a, solve_8b


class TestDay8(unittest.TestCase):
    def test_solve_8a(self):
        self.assertEqual(14, solve_8a(Path("input_test.txt")))

    def test_solve_8b(self):
        self.assertEqual(34, solve_8b(Path("input_test.txt")))
