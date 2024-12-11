from pathlib import Path

DIR = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def explore(data):
    walls, current, seen, direction = set(), (-1, -1), set(), 3

    for x, line in enumerate(data):
        for y, c in enumerate(line):
            if c == '#':
                walls.add((x, y))
            elif c == '^':
                current = (x, y)

    while 0 <= current[0] < len(data) and 0 <= current[1] < len(data[0]):
        seen.add(current)
        next_move = current[0] + DIR[direction][0], current[1] + DIR[direction][1]
        while next_move in walls:
            direction = (direction + 1) % 4
            next_move = current[0] + DIR[direction][0], current[1] + DIR[direction][1]
        current = next_move
    
    return seen


def part1(data):
    return len(explore(data))


def part2(data):
    path = explore(data)
    walls, start = set(), (-1, -1)

    for x, line in enumerate(data):
        for y, c in enumerate(line):
            if c == '#':
                walls.add((x, y))
            elif c == '^':
                start = (x, y)

    total = 0
    for p in path:
        all_walls = walls.copy()
        all_walls.add(p)
        current, seen, direction = start, set(), 3
        while 0 <= current[0] < len(data) and 0 <= current[1] < len(data[0]):
            if (current, direction) in seen:
                total += 1
                break
            seen.add((current, direction))
            next_move = current[0] + DIR[direction][0], current[1] + DIR[direction][1]
            while next_move in all_walls:
                direction = (direction + 1) % 4
                next_move = current[0] + DIR[direction][0], current[1] + DIR[direction][1]
            current = next_move

    return total



def parse(file):
    return [line for line in file.split('\n')]


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/"+Path(__file__).stem).open(encoding="UTF-8") as f:
        DATA = parse(f.read())

        print(f"Phase 1: {part1(DATA)}")
        print(f"Phase 2: {part2(DATA)}")
