from pathlib import Path
import re

def part1(data):
    regex, ids = re.compile(r"^(.+)\1$"), 0
    for start, end in data:
        for i in range(start, end + 1):
            if regex.match(str(i)):
                ids += i
    return ids


def part2(data):
    regex, ids = re.compile(r"^(.+)\1+$"), 0
    for start, end in data:
        for i in range(start, end + 1):
            if regex.match(str(i)):
                ids += i
    return ids


def parse(file):
    return [tuple(int(x) for x in line.split('-')) for line in file.split(',')]


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/"+Path(__file__).stem).open(encoding="UTF-8") as f:
        DATA = parse(f.read())

        print(f"Phase 1: {part1(DATA)}")
        print(f"Phase 2: {part2(DATA)}")
