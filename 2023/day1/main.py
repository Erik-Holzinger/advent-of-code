import re

if __name__ == '__main__':
    with open("input_1.txt") as file:
        lines = [line.strip() for line in file]
        sum = [line.isdigit() for line in lines]
        print(sum)
