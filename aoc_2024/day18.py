from pathlib import Path
from collections import deque

DIRECTIONS = [(1,0), (0,1), (-1,0), (0,-1)]

def part1(positions, count=1024, size=70):
    memory, queue, seen = set(), deque([((0,0), 0)]), set((0,0))
    for pos in positions[:count]:
        memory.add(pos)

    while queue:
        pos, distance = queue.popleft()
        if pos == (size, size):
            return distance
        for direction in DIRECTIONS:
            next_step = (pos[0] + direction[0], pos[1] + direction[1])
            if next_step in memory or next_step in seen or \
                not (0 <= next_step[0] <= size and 0 <= next_step[1] <= size):
                continue
            queue.append((next_step, distance + 1))
            seen.add(next_step)

    return -1


def part2(positions, count=1024, size=70):
    for i in range(count, len(positions)):
        if part1(positions, i, size) == -1:
            return f"{positions[i-1][0]},{positions[i-1][1]}"


def parse(file):
    return [tuple(int(x) for x in line.split(',')) for line in file.split('\n')]


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/"+Path(__file__).stem).open(encoding="UTF-8") as f:
        DATA = parse(f.read())

        print(f"Phase 1: {part1(DATA)}")
        print(f"Phase 2: {part2(DATA)}")
