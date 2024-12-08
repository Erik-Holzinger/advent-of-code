import re
from pathlib import Path
from typing import List

from y2024.utils import timer


def __get_input(input_file: Path) -> List[str]:
    with open(input_file) as f:
        return re.findall(r"mul\(\d+,\d+\)|don't\(\)|do\(\)", f.read())


@timer
def solve_3a(input_file: Path):
    puzzle_input = __get_input(input_file)

    result = 0
    for entry in puzzle_input:
        matching = re.search(r'mul\((\d+),(\d+)\)', entry)
        if matching:
            x, y = int(matching.group(1)), int(matching.group(2))
            result += x * y
    return result


@timer
def solve_3b(input_file: Path):
    puzzle_input = __get_input(input_file)

    calc_disabled = False
    result = 0
    for entry in puzzle_input:
        do_matcher = re.search(r"do\(\)", entry)
        do_not_matcher = re.search(r"don't\(\)", entry)
        mul_matcher = re.search(r"mul\((\d+),(\d+)\)", entry)

        if do_not_matcher:
            calc_disabled = True
            continue

        if do_matcher:
            calc_disabled = False
            continue

        if calc_disabled:
            continue

        if mul_matcher:
            result += int(mul_matcher.group(1)) * int(mul_matcher.group(2))

    return result
