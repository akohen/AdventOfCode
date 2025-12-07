from pathlib import Path
from collections import defaultdict

def part1(data):
    total = 0
    current = set([len(data[0])//2])
    for i in range(2, len(data), 2):
        next_layer = set()
        for x in current:
            if data[i][x] == '^':
                next_layer.add(x-1)
                next_layer.add(x+1)
                total += 1
            else:
                next_layer.add(x)
        current = next_layer
    return total


def part2(data):
    current = defaultdict(int)
    current[len(data[0])//2] = 1
    for i in range(2, len(data), 2):
        next_layer = defaultdict(int)
        for x in current:
            if data[i][x] == '^':
                next_layer[x-1] += current[x]
                next_layer[x+1] += current[x]
            else:
                next_layer[x] += current[x]
        current = next_layer
    return sum(current.values())


def parse(file):
    return [line for line in file.split('\n')]


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/"+Path(__file__).stem).open(encoding="UTF-8") as f:
        DATA = parse(f.read())

        print(f"Phase 1: {part1(DATA)}")
        print(f"Phase 2: {part2(DATA)}")