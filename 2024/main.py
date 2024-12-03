from pathlib import Path

from day1.day1 import solve_1a, solve_1b
from day2.day2 import solve_2a, solve_2b
from day3.day3 import solve_3a, solve_3b


if __name__ == '__main__':
    solve_1a(Path("./day1/input.txt"))
    solve_1b(Path("./day1/input.txt"))

    solve_2a(Path("./day2/input.txt"))
    solve_2b(Path("./day2/input.txt"))

    # https://regex-generator.olafneumann.org/
    # https://regex101.com/
    solve_3a(Path("./day3/input_test.txt"))
    solve_3b(Path("./day3/input_test.txt"))
