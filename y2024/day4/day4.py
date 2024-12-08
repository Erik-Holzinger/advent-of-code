from pathlib import Path
from typing import List

from y2024.utils import timer


def __get_input(input_file: Path) -> List[List[str]]:
    puzzle_input = []
    with open(input_file) as f:
        for line in f:
            chars = [c for c in line.strip()]
            puzzle_input.append(chars)
    return puzzle_input


# Possible traverse directions; includes reversed check
all_directions = [
    (0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)
]


def __search_predicate(x, y, dir_x, dir_y, rows, cols,
                       search_text, predicate) -> bool:
    """Iterate from a given starting point in each direction and check if the predicate was found."""
    for i in range(len(predicate)):
        # Index to look for next character
        ix, iy = x + i * dir_x, y + i * dir_y

        # Boundary check + character check
        if ix < 0 or ix >= rows or iy < 0 or iy >= cols or search_text[ix][iy] != predicate[i]:
            return False
    return True


@timer
def solve_4a(input_file: Path):
    puzzle_input = __get_input(input_file)

    word = "XMAS"
    rows, cols = len(puzzle_input), len(puzzle_input[0])
    count = 0

    for i in range(rows):
        for j in range(cols):
            # Only start check if first character matches; reduce loop for
            # EFFICIENCY :)
            if puzzle_input[i][j] == word[0]:
                for dx, dy in all_directions:
                    if __search_predicate(
                            i, j, dx, dy, rows, cols, puzzle_input, word):
                        count += 1

    return count


@timer
def solve_4b(input_file: Path):
    puzzle_input = __get_input(input_file)

    word = "MAS"
    rows, cols = len(puzzle_input), len(puzzle_input[0])
    count = 0

    for i in range(rows):
        for j in range(cols):
            if puzzle_input[i][j] == "A":
                tl_br = __search_predicate(
                    i - 1, j - 1, 1, 1, rows, cols, puzzle_input, word)
                br_tl = __search_predicate(
                    i + 1, j + 1, -1, -1, rows, cols, puzzle_input, word)

                tr_bl = __search_predicate(
                    i - 1, j + 1, 1, -1, rows, cols, puzzle_input, word)
                bl_tr = __search_predicate(
                    i + 1, j - 1, -1, 1, rows, cols, puzzle_input, word)

                if (tl_br or br_tl) and (tr_bl or bl_tr):
                    count += 1

    return count
