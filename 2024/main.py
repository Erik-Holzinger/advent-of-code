from pathlib import Path

from day1 import solve_1a, solve_1b
from day2 import solve_2a, solve_2b
from day3 import solve_3a, solve_3b
from day4 import solve_4a, solve_4b
from day5 import solve_5a, solve_5b
from day6 import solve_6a, solve_6b

if __name__ == '__main__':
    print("Result 1a: " + str(solve_1a(Path("./day1/input.txt"))))
    print("Result 1b: " + str(solve_1b(Path("./day1/input.txt"))))

    print("Result 2a: " + str(solve_2a(Path("./day2/input.txt"))))
    print("Result 2b: " + str(solve_2b(Path("./day2/input.txt"))))

    # https://regex-generator.olafneumann.org/
    # https://regex101.com/
    print("Result 3a: " + str(solve_3a(Path("./day3/input.txt"))))
    print("Result 3b: " + str(solve_3b(Path("./day3/input.txt"))))

    print("Result 4a: " + str(solve_4a(Path("./day4/input.txt"))))
    print("Result 4b: " + str(solve_4b(Path("./day4/input.txt"))))

    print("Result 5a: " + str(solve_5a(Path("./day5/input.txt"))))
    print("Result 5b: " + str(solve_5b(Path("./day5/input.txt"))))

    print("Result 6a: " + str(solve_6a(Path("./day6/input.txt"))))
    print("Result 6b: " + str(solve_6b(Path("./day6/input.txt"))))
