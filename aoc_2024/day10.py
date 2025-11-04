from pathlib import Path
from collections import deque

DIRECTIONS = [(1,0), (-1,0), (0,1), (0,-1)]

def score(data, unique=True):
    def get_trails(start):
        to_open, ends = deque([start]), []
        while to_open:
            current = to_open.popleft()
            for step in DIRECTIONS:
                next_pos = (current[0] + step[0], current[1] + step[1])
                if not (0 <= next_pos[0] < len(data) and 0 <= next_pos[1] < len(data[0])):
                    continue
                if not data[next_pos[0]][next_pos[1]] == data[current[0]][current[1]] + 1:
                    continue
                if data[next_pos[0]][next_pos[1]] == 9:
                    ends.append(next_pos)
                else:
                    to_open.append(next_pos)
        return len(set(ends)) if unique else len(ends)
    return sum([
        get_trails((r, c))
        for r in range(len(data)) for c in range(len(data[0]))
        if data[r][c] == 0
    ])

def part1(data):
    return score(data, unique=True)

def part2(data):
    return score(data, unique=False)

def parse(file):
    return [[int(x) for x in line] for line in file.split('\n')]


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/"+Path(__file__).stem).open(encoding="UTF-8") as f:
        DATA = parse(f.read())

        print(f"Phase 1: {part1(DATA)}")
        print(f"Phase 2: {part2(DATA)}")
