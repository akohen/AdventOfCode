from pathlib import Path

def part1(rotations):
    position, total = 50, 0
    for direction, steps in rotations:
        position = (position + steps * direction) % 100
        if position == 0:
            total += 1
    return total


def part2(rotations):
    position, total = 50, 0
    for direction, steps in rotations:
        for _ in range(steps):
            position = (position + direction) % 100
            if position == 0:
                total += 1
    return total


def parse(file):
    return [(1 if line[0] == 'R' else -1, int(line[1:])) for line in file.split('\n')]


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/"+Path(__file__).stem).open(encoding="UTF-8") as f:
        DATA = parse(f.read())

        print(f"Phase 1: {part1(DATA)}")
        print(f"Phase 2: {part2(DATA)}")
