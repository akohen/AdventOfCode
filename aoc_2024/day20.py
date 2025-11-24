from pathlib import Path
from collections import deque

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def add(a,b):
    return (a[0] + b[0], a[1] + b[1])

def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def get_path(walls, start, end):
    paths = deque([[start]])
    for _ in range(len(walls)):
        path = paths.popleft()
        for direction in DIRECTIONS:
            new_point = add(path[-1], direction)
            if new_point in walls:
                continue
            if len(path) > 1 and new_point == path[-2]:
                continue
            new_path = path + [new_point]
            if new_point == end:
                return new_path
            paths.append(new_path)
    return None
    

def part1(walls, start, end, min_skip=100):
    cheats, path = [], get_path(walls, start, end)
    for i, point in enumerate(path[:-min_skip]):
        for direction in DIRECTIONS:
            first = add(point, direction)
            second = add(first, direction)
            if first in walls and second in path[i+1:]:
                cheats.append(path.index(second)-i-2)
    
    return sum(1 for c in cheats if c >= min_skip)
    

def part2(walls, start, end, min_skip=100):
    cheats, path = 0, get_path(walls, start, end)
    for i, point in enumerate(path[:-min_skip]):
        for j, second in enumerate(path[i+min_skip:]):
            d = distance(point, second)
            if d > 20:
                continue # too far
            if j+min_skip-d >= min_skip:
                cheats += 1
    return cheats


def parse(file):
    walls, start, end = set(), None, None
    for y, row in enumerate(file.split('\n')):
        for x, col in enumerate(row):
            if col == '#':
                walls.add((x, y))
            elif col == 'S':
                start = (x, y)
            elif col == 'E':
                end = (x, y)

    return walls, start, end


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/"+Path(__file__).stem).open(encoding="UTF-8") as f:
        DATA = parse(f.read())

        print(f"Phase 1: {part1(*DATA)}")
        print(f"Phase 2: {part2(*DATA)}")
