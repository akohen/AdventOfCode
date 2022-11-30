from pathlib import Path
from typing import DefaultDict

def phase1(points):
    distances = DefaultDict(int)
    for i in range(points[-1]):
        for point in points:
            distances[i] += abs(point-i)
    return min(distances.values())


def phase2(points):
    distances = DefaultDict(int)
    for i in range(points[-1]):
        for point in points:
            distances[i] += int(abs(point-i) * (1 + abs(point-i))/2)
    return min(distances.values())


def parse(file):
    return sorted([int(x) for x in file.split(',')])

if __name__ == "__main__":
    with Path(__file__).parent.joinpath("../input/"+Path(__file__).stem).open(encoding="UTF-8") as f:
        POINTS = parse(f.read())

        print(f"Phase 1: {phase1(POINTS)}")
        print(f"Phase 2: {phase2(POINTS)}")
