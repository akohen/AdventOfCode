from pathlib import Path
import math


def part1(races):
    return math.prod(len([i for i in range(race[0]) if i*(race[0]-i) > race[1]]) for race in races)


def part2(data):
    return len([i for i in range(data[0]) if i*(data[0]-i) > data[1]])


def parse(file):
    data = [[int(x) for x in line.split(' ') if str.isdigit(x)] for line in file.split('\n')]
    return list(zip(*data))


def parse2(file):
    return [int(x) for line in file.split('\n')  for x in line.replace(' ','').split(':') if str.isdigit(x)]


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/"+Path(__file__).stem).open(encoding="UTF-8") as f:
        DATA = f.read()

        print(f"Phase 1: {part1(parse(DATA))}")
        print(f"Phase 2: {part2(parse2(DATA))}")
