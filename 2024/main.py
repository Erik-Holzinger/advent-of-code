from pathlib import Path

from day1.day1 import solve_1a, solve_1b
from day2.day2 import solve_2a, solve_2b

if __name__ == '__main__':
    solve_1a(Path("./day1/input.txt"))
    solve_1b(Path("./day1/input.txt"))

    solve_2a(Path("./day2/input.txt"))
    solve_2b(Path("./day2/input.txt"))
