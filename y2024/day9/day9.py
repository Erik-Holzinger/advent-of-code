from collections import Counter
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


def sort_quicker_with_blocks(puzzle_input: List[str]) -> List[str]:
    last_index = len(puzzle_input) - 1
    left = 0
    right = last_index
    # Lookup map for block size
    block_size = Counter([x for x in puzzle_input if x != "."])

    # Sort every element exactly once to the left side
    while right > 0:
        # Search for free space
        while left < last_index and puzzle_input[left] != ".":
            left += 1
        left_ahead = left + 1
        found_space = 1
        while left_ahead < last_index and puzzle_input[left_ahead] == ".":
            left_ahead += 1
            found_space += 1

        # Search for block to move
        while right > 0 and puzzle_input[right] == ".":
            right -= 1
        needed_space = block_size[puzzle_input[right]]

        # Would move the element further away so stop and reset
        if right < left:
            right -= needed_space
            left = 0
            continue

        if needed_space <= found_space:
            # Found space, move block
            for i in range(needed_space):
                puzzle_input[left + i] = puzzle_input[right - i]
                puzzle_input[right - i] = "."

            right -= needed_space
            left = 0
        else:
            # Not enough space, search for next one
            left = left_ahead

    return puzzle_input


def __calculate_checksum(puzzle_input: List[str]) -> int:
    checksum = 0
    for i in range(len(puzzle_input)):
        if puzzle_input[i] == ".":
            continue
        checksum += i * int(puzzle_input[i])
    return checksum


@timer
def solve_9a(input_file: Path) -> int:
    puzzle_input: List[str] = __load_puzzle_input(input_file)
    puzzle_input = sort_quicker(puzzle_input)
    return __calculate_checksum(puzzle_input)


@timer
def solve_9b(input_file: Path) -> int:
    puzzle_input: List[str] = __load_puzzle_input(input_file)
    puzzle_input = sort_quicker_with_blocks(puzzle_input)
    return __calculate_checksum(puzzle_input)
