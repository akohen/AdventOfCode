from pathlib import Path
from typing import DefaultDict
from itertools import permutations

def calc_distance(path, distances):
    return sum([
        distances[path[i]][path[i+1]]
        for i in range(0, len(path)-1)
    ])

def phase1(distances):
    min_distance = 9999999999
    for path in permutations(distances.keys()):
        min_distance = min(min_distance, calc_distance(path, distances))
    return min_distance


def phase2(distances):
    max_distance = 0
    for path in permutations(distances.keys()):
        max_distance = max(max_distance, calc_distance(path, distances))
    return max_distance


def parse(text):
    distances = DefaultDict(dict)
    for place in [line.split(' ') for line in text.split('\n')]:
        distances[place[0]][place[2]] = int(place[4])
        distances[place[2]][place[0]] = int(place[4])
    return distances

if __name__ == "__main__":
    with Path(__file__).parent.joinpath("../input/day9").open(encoding="UTF-8") as f:
        INSTRUCTIONS = parse(f.read())

        print(f"Phase 1: {phase1(INSTRUCTIONS)}")
        print(f"Phase 2: {phase2(INSTRUCTIONS)}")
