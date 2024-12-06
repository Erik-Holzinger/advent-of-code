import re
from pathlib import Path
from typing import Tuple, List


def get_input(input_file: Path) -> Tuple[List[int], List[int]]:
    left, right = [], []

    with open(input_file) as f:
        for line in f:
            x, y = re.findall(r'\d+', line)
            left.append(int(x))
            right.append(int(y))

    return left, right


def solve_1a(input_file: Path):
    left, right = get_input(input_file)

    result = 0
    for (x, y) in zip(sorted(left), sorted(right)):
        result += abs(x - y)
    return result


def solve_1b(input_file: Path):
    left, right = get_input(input_file)

    result = 0
    for x in left:
        y = right.count(x)
        result += x * y
    return result
