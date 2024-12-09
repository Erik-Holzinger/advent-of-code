from pathlib import Path
from typing import List

from y2024.utils import timer


def __load_puzzle_input(input_file: Path) -> List[str]:
    puzzle_input: List[str] = []
    with open(input_file) as f:
        for line in f:
            counter = 0
            for i in range(len(line)):
                if i % 2 == 0:
                    # Block
                    for j in range(int(line[i])):
                        puzzle_input.append(str(counter))
                    counter += 1
                else:
                    # Free
                    puzzle_input += "." * int(line[i])
    return puzzle_input


def sort_quicker(puzzle_input: List[str]) -> List[str]:
    left = 0
    right = len(puzzle_input) - 1

    while left < right:
        # Search for dot
        while left < len(puzzle_input) and puzzle_input[left] != ".":
            left += 1

        # Search for non-dot
        while right >= 0 and puzzle_input[right] == ".":
            right -= 1

        if left < right and puzzle_input[left] == "." and puzzle_input[right] != ".":
            puzzle_input[left], puzzle_input[right] = puzzle_input[right], '.'
            left += 1
            right -= 1
        else:
            break

    return puzzle_input


def sort_quicker_blocks(puzzle_input: List[str]) -> List[str]:
    left = 0
    right = len(puzzle_input) - 1

    while right >= 0:
        # Search for non-dot
        while right >= 0 and puzzle_input[right] == ".":
            right -= 1

        # Calculate needed space
        space_right = 1
        right_search = right - 1
        while right_search > 0 and puzzle_input[right_search] == puzzle_input[right]:
            space_right += 1
            right_search -= 1

        # Search for dot
        while left < len(puzzle_input) and puzzle_input[left] != ".":
            left += 1

        # Calculate space on left side
        space_left = 1
        left_search = left + 1
        while left_search < len(puzzle_input) and puzzle_input[left_search] == ".":
            space_left += 1
            left_search += 1

        if left_search > right:
            left = 0
            right = right_search
            continue

        if space_left >= space_right:
            # Block fits
            for i in range(space_right):
                puzzle_input[left + i] = puzzle_input[right - i]
                puzzle_input[right - i] = "."
            left += space_right
            right = right_search
        else:
            # Block does not fit
            left = left_search

    return puzzle_input


@timer
def solve_9a(input_file: Path) -> int:
    puzzle_input: List[str] = __load_puzzle_input(input_file)
    puzzle_input = sort_quicker(puzzle_input)

    checksum = 0
    for i in range(len(puzzle_input)):
        if puzzle_input[i] == ".":
            break
        checksum += i * int(puzzle_input[i])

    return checksum


@timer
def solve_9b(input_file: Path) -> int:
    puzzle_input: List[str] = __load_puzzle_input(input_file)
    puzzle_input = sort_quicker_blocks(puzzle_input)
    print(puzzle_input)

    checksum = 0
    for i in range(len(puzzle_input)):
        if puzzle_input[i] == ".":
            continue
        checksum += i * int(puzzle_input[i])

    return checksum
