from pathlib import Path
from string import ascii_letters
from copy import deepcopy
from collections import deque, defaultdict

neighbors = [(-1,0),(1,0),(0,1),(0,-1)]


def phase1(data):
    for x, line in enumerate(data):
        if 44 in line:
            start = (x, line.index(44))
        if 30 in line:
            end = (x, line.index(30))
            line[end[1]] = 25
    to_open, seen = deque([(start,0)]), defaultdict(lambda: 9999999)
    while len(to_open) > 0:
        curr, dist = to_open.popleft()
        if seen[curr] > dist:
            seen[curr] = dist
            for n in neighbors:
                x, y = curr[0] + n[0], curr[1] + n[1]
                if x < 0 or y < 0 or x == len(data) or y == len(data[0]):
                    continue
                if data[curr[0]][curr[1]] + 1 >= data[x][y]:
                    to_open.append(((x,y), dist+1))
    return seen[end]


def phase2(data):
    for x, line in enumerate(data):
        if 44 in line:
            start = (x, line.index(44))
            line[line.index(44)] = 0
        if 30 in line:
            end = (x, line.index(30))
            line[end[1]] = 25
    to_open, seen, results = deque([(end,0)]), defaultdict(lambda: 9999999), []
    while len(to_open) > 0:
        curr, dist = to_open.popleft()
        if seen[curr] > dist:
            seen[curr] = dist
            if data[curr[0]][curr[1]] == 0:
                results.append(dist)
            for n in neighbors:
                x, y = curr[0] + n[0], curr[1] + n[1]
                if x < 0 or y < 0 or x == len(data) or y == len(data[0]):
                    continue
                if data[curr[0]][curr[1]]  <= data[x][y] +1:
                    to_open.append(((x,y), dist+1))
    return min(results)

def parse(file):
    return [[ascii_letters.index(c) for c in line] for line in file.split('\n')]


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/"+Path(__file__).stem).open(encoding="UTF-8") as f:
        DATA = parse(f.read())

        print(f"Phase 1: {phase1(deepcopy(DATA))}")
        print(f"Phase 2: {phase2(DATA)}")
