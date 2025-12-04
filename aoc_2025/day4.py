from pathlib import Path

NEIGHBORS = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

def step(rolls):
    accessible = set()
    for x, y in rolls:
        count = 0
        for dx, dy in NEIGHBORS:
            if (x + dx, y + dy) in rolls:
                count += 1
        if count < 4:
            accessible.add((x, y))
    return accessible


def part1(rolls):
    return len(step(rolls))


def part2(data):
    rolls = data.copy()
    while to_remove_set := step(rolls):
        rolls -= to_remove_set
    return len(data) - len(rolls)


def parse(file):
    rolls = set()
    for y, line in enumerate(file.split('\n')):
        for x, char in enumerate(line):
            if char == '@':
                rolls.add((x, y))
    return rolls


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/"+Path(__file__).stem).open(encoding="UTF-8") as f:
        DATA = parse(f.read())

        print(f"Phase 1: {part1(DATA)}")
        print(f"Phase 2: {part2(DATA)}")
