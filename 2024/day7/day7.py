import re
from pathlib import Path
from typing import List


class Equation:
    def __init__(self, expected_result: int, numbers: List[int]):
        self.expected_result = expected_result
        self.numbers = numbers


def __load_puzzle_input(input_file: Path) -> List[Equation]:
    eq_input: List[Equation] = []
    with open(input_file) as f:
        for line in f:
            numbers = re.findall(r"(\d+)", line)
            eq_input.append(Equation(int(numbers[0]), list(map(int, numbers[1::]))))
    return eq_input


def __backtrack_equation(numbers: List[int], expected_result: int, index: int, current_value: int) -> bool:
    if index == len(numbers):
        # If last value reached check for expected result
        return current_value == expected_result

    next_num = numbers[index]

    # Addition case
    if __backtrack_equation(numbers, expected_result, index + 1, current_value + next_num):
        return True

    # Multiplication case
    if __backtrack_equation(numbers, expected_result, index + 1, current_value * next_num):
        return True

    return False


def __backtrack_equation_with_concat(numbers: List[int], expected_result: int, index: int, current_value: int) -> bool:
    if index == len(numbers):
        # If last value reached check for expected result
        return current_value == expected_result

    next_num = numbers[index]

    # Addition case
    if __backtrack_equation_with_concat(numbers, expected_result, index + 1, current_value + next_num):
        return True

    # Multiplication case
    if __backtrack_equation_with_concat(numbers, expected_result, index + 1, current_value * next_num):
        return True

    # Concatenation case
    if __backtrack_equation_with_concat(numbers, expected_result, index + 1, int(f"{current_value}{next_num}")):
        return True

    return False


def __can_eq_be_solved_a(numbers: List[int], expected_res: int) -> bool:
    if not numbers:
        return False
    # Start at index 1 and use index 0 as current value
    return __backtrack_equation(numbers, expected_res, 1, numbers[0])


def __can_eq_be_solved_b(numbers: List[int], expected_res: int) -> bool:
    if not numbers:
        return False
    # Start at index 1 and use index 0 as current value
    return __backtrack_equation_with_concat(numbers, expected_res, 1, numbers[0])


def solve_7a(input_file: Path) -> int:
    eq_input = __load_puzzle_input(input_file)
    result = 0

    for eq in eq_input:
        if __can_eq_be_solved_a(eq.numbers, eq.expected_result):
            result += eq.expected_result

    return result


def solve_7b(input_file: Path) -> int:
    eq_input = __load_puzzle_input(input_file)
    result = 0

    for eq in eq_input:
        if __can_eq_be_solved_b(eq.numbers, eq.expected_result):
            result += eq.expected_result

    return result
