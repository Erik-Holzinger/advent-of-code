from enum import Enum
from pathlib import Path
from typing import List, Tuple


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


def load_puzzle_input(input_file: Path) -> List[List[str]]:
    puzzle_map = []
    with open(input_file) as f:
        for line in f:
            chars = [c for c in line.strip()]
            puzzle_map.append(chars)
    return puzzle_map


def find_starting_char(puzzle_map: List[List[str]]):
    allowed_chars = [x.character for x in Direction]
    for i in range(len(puzzle_map)):
        for j in range(len(puzzle_map[0])):
            if puzzle_map[i][j] in allowed_chars:
                return i, j, Direction.from_character(puzzle_map[i][j])


def find_new_direction(i, j, current_direction, puzzle_map):
    match current_direction:
        case Direction.UP:
            if puzzle_map[i][j + 1] != "#":
                return Direction.RIGHT
            return Direction.LEFT
        case Direction.RIGHT:
            if puzzle_map[i + 1][j] != "#":
                return Direction.DOWN
            return Direction.UP
        case Direction.DOWN:
            if puzzle_map[i][j - 1] != "#":
                return Direction.LEFT
            return Direction.RIGHT
        case Direction.LEFT:
            if puzzle_map[i - 1][j] != "#":
                return Direction.UP
            return Direction.DOWN
    raise ValueError("No new direction to go can be found")


def iterate_directions(i, j, direction, visited, puzzle_map):
    dx = direction.direction[0]
    dy = direction.direction[1]

    while puzzle_map[i + dx][j + dy] != "#":
        i += dx
        j += dy
        visited["x" + str(i) + "y" + str(j)] = True

        if (i + dx) < 0 or (i + dx) >= len(puzzle_map) or (j + dy) < 0 or (j + dy) >= len(puzzle_map[0]):
            return i, j, direction, visited, puzzle_map

    direction = find_new_direction(i, j, direction, puzzle_map)
    return i, j, direction, visited, puzzle_map


def has_escaped(i, j, direction, puzzle_map: List[List[str]]) -> bool:
    dx = direction.direction[0]
    dy = direction.direction[1]
    return i + dx < 0 or i + dx >= len(puzzle_map) or j + dy < 0 or j + dy >= len(puzzle_map[0])


def solve_6a(input_file: Path):
    puzzle_map = load_puzzle_input(input_file)

    i, j, direction = find_starting_char(puzzle_map)
    visited = {"x" + str(i) + "y" + str(j): True}

    while not has_escaped(i, j, direction, puzzle_map):
        i, j, direction, visited, puzzle_map = iterate_directions(i, j, direction, visited, puzzle_map)

    return len(visited.keys())


def solve_6b(input_file: Path):
    result = 0
    return result
