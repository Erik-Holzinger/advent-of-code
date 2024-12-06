from pathlib import Path

from day1 import solve_1a, solve_1b
from day2 import solve_2a, solve_2b
from day3 import solve_3a, solve_3b
from day4 import solve_4a, solve_4b
from day5 import solve_5a, solve_5b
from day6 import solve_6a, solve_6b

if __name__ == '__main__':
    solve_1a(Path("./day1/input.txt"))
    solve_1b(Path("./day1/input.txt"))

    solve_2a(Path("./day2/input.txt"))
    solve_2b(Path("./day2/input.txt"))

    # https://regex-generator.olafneumann.org/
    # https://regex101.com/
    solve_3a(Path("./day3/input.txt"))
    solve_3b(Path("./day3/input.txt"))

    solve_4a(Path("./day4/input.txt"))
    solve_4b(Path("./day4/input.txt"))

    solve_5a(Path("./day5/input.txt"))
    solve_5b(Path("./day5/input.txt"))

    solve_6a(Path("./day6/input.txt"))
    solve_6b(Path("./day6/input.txt"))
