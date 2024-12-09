import unittest
from pathlib import Path

from day9 import solve_9a, solve_9b


class TestDay9(unittest.TestCase):
    def test_solve_9a(self):
        self.assertEqual(1928, solve_9a(Path("input_test.txt")))

    def test_solve_9b(self):
        self.assertEqual(2858, solve_9b(Path("input_test.txt")))
