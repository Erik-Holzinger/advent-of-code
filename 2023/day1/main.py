import re


def exercise_a():
    with open("input.txt") as file:
        print(calc_sum(file.readlines()))


def exercise_b():
    with open("input.txt") as file:
        lines = []
        for line in file:
            new_line = line.strip()
            for k, v in number_map.items():
                new_line = new_line.replace(k, v)
            lines.append(new_line)
        print(calc_sum(lines))


number_map = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}


def calc_sum(lines):
    return sum([int(re.sub("[^0-9]", "", line)[0]) * 10 +
                int(re.sub("[^0-9]", "", line)[-1]) for line in lines])


if __name__ == '__main__':
    exercise_a()
    exercise_b()
