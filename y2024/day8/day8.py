from pathlib import Path
from typing import List, Tuple

from y2024.utils import timer


def __load_puzzle_input(input_file: Path) -> List[List[str]]:
    puzzle_map: List[List[str]] = []
    with open(input_file) as f:
        for line in f:
            chars = [c for c in line.strip()]
            puzzle_map.append(chars)
    return puzzle_map


def __append_antinode_if_possible(i: int, j: int, x: int, y: int, puzzle_map: List[List[str]],
                                  antinodes: List[Tuple[int, int]]):
    dix, djy = abs(i - x), abs(j - y)

    an_i = i + dix if i - dix == x else i - dix
    an_j = j + djy if j - djy == y else j - djy
    if an_i < 0 or an_i >= len(
            puzzle_map) or an_j < 0 or an_j >= len(puzzle_map[0]):
        return
    antinodes.append((an_i, an_j))

    an_x = x + dix if x - dix == i else x - dix
    an_y = y + djy if y - djy == j else y - djy
    if an_x < 0 or an_x >= len(
            puzzle_map) or an_y < 0 or an_y >= len(puzzle_map[0]):
        return
    antinodes.append((an_x, an_y))


def __check_for_antinodes(
        i: int, j: int, puzzle_map: List[List[str]], antinodes: List[Tuple[int, int]]):
    predicate = puzzle_map[i][j]
    for x in range(len(puzzle_map)):
        for y in range(len(puzzle_map[0])):
            if i == x and j == y:
                continue
            if puzzle_map[x][y] == predicate:
                __append_antinode_if_possible(
                    i, j, x, y, puzzle_map, antinodes)


def __append_antinode_for_line_if_possible(i: int, j: int, x: int, y: int, puzzle_map: List[List[str]],
                                           antinodes: List[Tuple[int, int]]):
    dix, djy = abs(i - x), abs(j - y)

    if i <= x and j <= y:
        dir_i, dir_j = dix, djy
    elif i <= x and j > y:
        dir_i, dir_j = dix, -1 * djy
    elif i > x and j <= y:
        dir_i, dir_j = -1 * dix, djy
    else:
        dir_i, dir_j = -1 * dix, -1 * djy

    an_i = i + dir_i
    an_j = j + dir_j
    while an_i >= 0 and an_i < len(
            puzzle_map) and an_j >= 0 and an_j < len(puzzle_map[0]):
        antinodes.append((an_i, an_j))
        an_i += dir_i
        an_j += dir_j

    an_x = x + -1 * dir_i
    an_y = y + -1 * dir_j
    while an_x >= 0 and an_x < len(
            puzzle_map) and an_y >= 0 and an_y < len(puzzle_map[0]):
        antinodes.append((an_x, an_y))
        an_x += -1 * dir_i
        an_y += -1 * dir_j


def __check_for_antinodes_in_line(
        i: int, j: int, puzzle_map: List[List[str]], antinodes: List[Tuple[int, int]]):
    predicate = puzzle_map[i][j]
    for x in range(len(puzzle_map)):
        for y in range(len(puzzle_map[0])):
            if i == x and j == y:
                continue
            if puzzle_map[x][y] == predicate:
                __append_antinode_for_line_if_possible(
                    i, j, x, y, puzzle_map, antinodes)


@timer
def solve_8a(input_file: Path) -> int:
    puzzle_input = __load_puzzle_input(input_file)
    antinodes: List[Tuple[int, int]] = []

    for i in range(len(puzzle_input)):
        for j in range(len(puzzle_input[0])):
            if puzzle_input[i][j] != ".":
                __check_for_antinodes(i, j, puzzle_input, antinodes)

    return len(set(antinodes))


@timer
def solve_8b(input_file: Path) -> int:
    puzzle_input = __load_puzzle_input(input_file)
    antinodes: List[Tuple[int, int]] = []

    for i in range(len(puzzle_input)):
        for j in range(len(puzzle_input[0])):
            if puzzle_input[i][j] != ".":
                __check_for_antinodes_in_line(i, j, puzzle_input, antinodes)

    return len(set(antinodes))
