import re
from pathlib import Path
from typing import List

from y2024.utils import timer


def __get_input(input_file: Path) -> List[List[int]]:
    puzzle_input = []

    with open(input_file) as f:
        for line in f:
            x = re.findall(r'\d+', line)
            puzzle_input.append(x)

    return puzzle_input


def __detect_invalid(entry: List[int]) -> int:
    asc: bool | None = None
    i = 0
    for x, y in zip(entry, entry[1:]):
        currently_asc = x < y

        if asc is None:
            asc = currently_asc

        if currently_asc != asc or x == y or abs(x - y) > 3:
            return i

        i += 1
    return -1


@timer
def solve_2a(input_file: Path):
    puzzle_input = __get_input(input_file)

    unsafe = 0
    for entry in puzzle_input:
        entry = list(map(int, entry))
        if (__detect_invalid(entry)) != -1:
            unsafe += 1

    safe = len(puzzle_input) - unsafe
    return safe


@timer
def solve_2b(input_file: Path):
    puzzle_input = __get_input(input_file)

    unsafe = 0
    for entry in puzzle_input:
        entry = list(map(int, entry))
        index_to_remove = __detect_invalid(entry)

        if index_to_remove != -1:
            # Usage of "brute-force" due to the fact,
            # that when an entry start asc/desc and then changes
            # the index_to_remove is already offset by 1 to fix the issue.
            for i in range(len(entry)):
                corrected_entry = entry[:i] + entry[i + 1:]
                if (__detect_invalid(corrected_entry)) == -1:
                    break
                elif i == len(entry) - 1:
                    unsafe += 1

    safe = len(puzzle_input) - unsafe
    return safe
