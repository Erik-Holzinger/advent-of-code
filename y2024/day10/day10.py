from pathlib import Path
from typing import List, Set, Tuple

from y2024.utils import timer


def __load_puzzle_input(input_file: Path) -> List[List[int]]:
    puzzle_map = []
    with open(input_file) as f:
        for line in f:
            number = [int(c) for c in line.strip()]
            puzzle_map.append(number)
    return puzzle_map


directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def __find_unique_endpoints(i, j, puzzle_map: List[List[int]]) -> Set[Tuple[int, int]]:
    if puzzle_map[i][j] == 9:
        # Base case found 9 and return set containing position
        return {(i, j)}

    results = set()
    for direction in directions:
        di, dj = i + direction[0], j + direction[1]
        if 0 <= di < len(puzzle_map) and 0 <= dj < len(puzzle_map[0]):
            if puzzle_map[i][j] + 1 == puzzle_map[di][dj]:
                endpoints = __find_unique_endpoints(di, dj, puzzle_map)
                results.update(endpoints)

    return results


def __find_unique_paths(i, j, puzzle_map: List[List[int]]) -> int:
    if puzzle_map[i][j] == 9:
        # Base case found 9 and return 1 successful path
        return 1

    result = 0
    for direction in directions:
        di, dj = i + direction[0], j + direction[1]
        if 0 <= di < len(puzzle_map) and 0 <= dj < len(puzzle_map[0]):
            if puzzle_map[i][j] + 1 == puzzle_map[di][dj]:
                result += __find_unique_paths(di, dj, puzzle_map)

    return result


@timer
def solve_10a(input_file: Path) -> int:
    puzzle_input: List[List[int]] = __load_puzzle_input(input_file)
    trail_start = [(x, y) for x in range(len(puzzle_input)) for y in range(len(puzzle_input[0])) if
                   puzzle_input[x][y] == 0]

    counter = 0
    for (x, y) in trail_start:
        counter += len(__find_unique_endpoints(x, y, puzzle_input))
    return counter


@timer
def solve_10b(input_file: Path) -> int:
    puzzle_input: List[List[int]] = __load_puzzle_input(input_file)
    trail_start = [(x, y) for x in range(len(puzzle_input)) for y in range(len(puzzle_input[0])) if
                   puzzle_input[x][y] == 0]

    counter = 0
    for (x, y) in trail_start:
        counter += __find_unique_paths(x, y, puzzle_input)
    return counter
