import copy
from collections import defaultdict
from enum import Enum
from pathlib import Path
from typing import List, Tuple, Dict

from y2024.utils import timer

obstacle = "#"


class Direction(Enum):
    UP = (1, "^", (-1, 0))
    DOWN = (2, "v", (1, 0))
    LEFT = (3, "<", (0, -1))
    RIGHT = (4, ">", (0, 1))

    def __init__(self, code: int, character: str, direction: Tuple[int, int]):
        self.code = code
        self.character = character
        self.direction = direction

    @staticmethod
    def from_character(character: str):
        for direction in Direction:
            if direction.character == character:
                return direction
        raise ValueError(f"No direction found for character '{character}'")


def __load_puzzle_input(input_file: Path) -> List[List[str]]:
    puzzle_map = []
    with open(input_file) as f:
        for line in f:
            chars = [c for c in line.strip()]
            puzzle_map.append(chars)
    return puzzle_map


def __find_starting_char(puzzle_map: List[List[str]]):
    allowed_chars = [x.character for x in Direction]
    for i in range(len(puzzle_map)):
        for j in range(len(puzzle_map[0])):
            if puzzle_map[i][j] in allowed_chars:
                return i, j, Direction.from_character(puzzle_map[i][j])


def __find_new_direction(
        i: int, j: int, current_direction: Direction, puzzle_map: List[List[str]]):
    match current_direction:
        case Direction.UP:
            if puzzle_map[i][j + 1] != obstacle:
                return Direction.RIGHT

            return Direction.DOWN
        case Direction.RIGHT:
            if puzzle_map[i + 1][j] != obstacle:
                return Direction.DOWN
            return Direction.LEFT
        case Direction.DOWN:
            if puzzle_map[i][j - 1] != obstacle:
                return Direction.LEFT
            return Direction.UP
        case Direction.LEFT:
            if puzzle_map[i - 1][j] != obstacle:
                return Direction.UP
            return Direction.RIGHT
    raise ValueError("No new direction to go can be found")


def __iterate_directions(i: int, j: int, direction: Direction, visited: Dict[Tuple[int, int], List[Direction]],
                         puzzle_map: List[List[str]]):
    """ Walk in one direction until obstacle or end is detected and return postion """
    dx = direction.direction[0]
    dy = direction.direction[1]

    while puzzle_map[i + dx][j + dy] != obstacle:
        i += dx
        j += dy
        visited[(i, j)].append(direction)

        # Look ahead to have a valid while loop
        if (i + dx) < 0 or (i + dx) >= len(puzzle_map) or (j +
                                                           dy) < 0 or (j + dy) >= len(puzzle_map[0]):
            return i, j, direction, visited, puzzle_map

    direction = __find_new_direction(i, j, direction, puzzle_map)
    return i, j, direction, visited, puzzle_map


def __has_escaped(i: int, j: int, direction: Direction,
                  puzzle_map: List[List[str]]) -> bool:
    """ If the index went out of bound so did the guard """
    di = i + direction.direction[0]
    dj = j + direction.direction[1]
    return di < 0 or di >= len(
        puzzle_map) or dj < 0 or dj >= len(puzzle_map[0])


def __get_traversal_path(
        puzzle_map: List[List[str]]) -> Dict[Tuple[int, int], List[Direction]]:
    i, j, direction = __find_starting_char(puzzle_map)
    traversal_path: Dict[Tuple[int, int], List[Direction]] = defaultdict(list)
    traversal_path[(i, j)].append(direction)

    while not __has_escaped(i, j, direction, puzzle_map):
        # Goes in one direction until obstacle or escape
        i, j, direction, traversal_path, puzzle_map = __iterate_directions(
            i, j, direction, traversal_path, puzzle_map)

        # Already been on path with same direction
        future_i, future_j = i + \
            direction.direction[0], j + direction.direction[1]

        if (future_i, future_j) in traversal_path and direction in traversal_path[(
                future_i, future_j)]:
            raise RuntimeError("You Spin Me Round (Like a Record)")

    return traversal_path


@timer
def solve_6a(input_file: Path) -> int:
    puzzle_map = __load_puzzle_input(input_file)
    traversal_path: Dict[Tuple[int, int], List[Direction]
                         ] = __get_traversal_path(puzzle_map)
    return len(traversal_path)


@timer
def solve_6b(input_file: Path) -> int:
    puzzle_map = __load_puzzle_input(input_file)
    start_x, start_y, direction = __find_starting_char(puzzle_map)
    traversal_path: Dict[Tuple[int, int], List[Direction]
                         ] = __get_traversal_path(puzzle_map)

    result = 0
    for index, (k, v) in enumerate(traversal_path.items()):
        puzzle_map_new = copy.deepcopy(puzzle_map)

        if k[0] == start_x and k[1] == start_y:
            # Do not change starting point
            continue

        i, j = k
        puzzle_map_new[i][j] = obstacle

        try:
            _ = __get_traversal_path(puzzle_map_new)
        except RuntimeError:
            result += 1

    return result
