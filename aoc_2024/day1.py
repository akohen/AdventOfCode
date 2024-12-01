from pathlib import Path
from collections import Counter

def part1(data):
    sorted_ids = list(zip(sorted(data[0]), sorted(data[1])))
    return sum([abs(a-b) for a, b in sorted_ids])


def part2(data):
    counts = Counter(data[1])
    return sum([x * counts[x] for x in data[0]])


def parse(file):
    return [list(a) for a in zip(*[[int(x) for x in line.split()] for line in file.split('\n')])]


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/"+Path(__file__).stem).open(encoding="UTF-8") as f:
        DATA = parse(f.read())

        print(f"Phase 1: {part1(DATA)}")
        print(f"Phase 2: {part2(DATA)}")
