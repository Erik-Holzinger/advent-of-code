import re
from collections import deque
from pathlib import Path
from typing import List, Dict, Tuple

from y2024.utils import timer


def __load_puzzle_input(
        input_file: Path) -> Tuple[Dict[int, List[int]], List[List[int]]]:
    dag: Dict[int, List[int]] = {}
    puzzle_input: List[List[int]] = []

    with open(input_file) as f:
        for line in f:
            rule_matcher = re.search(r"(\d+)\|(\d+)", line)
            input_matcher = re.search(r"^\d+(?:,\d+)+$", line)
            if rule_matcher:
                before, after = rule_matcher.groups()
                dag.setdefault(int(before), []).append(int(after))
            if input_matcher:
                puzzle_input.append([int(num) for num in line.split(",")])

    return dag, puzzle_input


def __is_entry_valid(entry: List[int], dag: Dict[int, List[int]]) -> bool:
    for i in range(len(entry)):
        for j in range(len(entry)):
            if i >= j:
                continue
            entry_i = entry[i]
            entry_to_compare = entry[j]
            if entry_i in dag.get(entry_to_compare, []):
                return False
    return True


def __sort_entry_using_kahn(
        numbers_to_sort: List[int], dag: Dict[int, List[int]]) -> List[int]:
    # https://www.geeksforgeeks.org/topological-sorting-indegree-based-solution/

    # graph should only contain nodes and edges that are in our entry to sort
    dag_with_relevant_nodes = {}
    for node in dag:
        if node not in numbers_to_sort:
            continue
        dag_with_relevant_nodes[node] = [
            val for val in dag[node] if val in numbers_to_sort]

    # in_degree = number of incoming edges to a node
    in_degree: Dict[int, int] = {}
    for k in dag_with_relevant_nodes:
        # init node
        if k not in in_degree:
            in_degree[k] = 0
        for v in dag_with_relevant_nodes[k]:
            in_degree[v] = in_degree.get(v, 0) + 1

    # dequeue to start removing nodes with 0 incoming edges
    queue = deque()
    for node in in_degree:
        if in_degree[node] == 0:
            queue.append(node)

    result = []
    while queue:
        removed_node = queue.popleft()
        result.append(removed_node)

        for v in dag_with_relevant_nodes.get(removed_node, []):
            # remove now popped node u fron incoming edges
            in_degree[v] -= 1
            # append new node without incoming edges
            if in_degree[v] == 0:
                queue.append(v)

    # cycle detection
    if len(result) != len(in_degree):
        raise ValueError(
            "Given DAG has a cycle therefore no sorting is possible")
    return result


@timer
def solve_5a(input_file: Path):
    dag, puzzle_input = __load_puzzle_input(input_file)

    valid_entries = [x for x in puzzle_input if __is_entry_valid(x, dag)]

    result = 0
    for entry in valid_entries:
        result += entry[int((len(entry) - 1) / 2)]
    return result


@timer
def solve_5b(input_file: Path):
    dag, puzzle_input = __load_puzzle_input(input_file)

    invalid_entries = [
        __sort_entry_using_kahn(
            x, dag) for x in puzzle_input if not __is_entry_valid(
            x, dag)]

    result = 0
    for entry in invalid_entries:
        result += entry[int((len(entry) - 1) / 2)]
    return result
