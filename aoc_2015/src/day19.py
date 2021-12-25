from pathlib import Path
from typing import DefaultDict


def phase1(n):
    return n


def phase2(n):
    return n


def parse(f):
    replacements = DefaultDict(list)
    for line in f:
        values = line.rstrip().split(' => ')
        if len(values) == 2:
            replacements[values[0]].append(values[1])
        if len(values) == 1 and values[0] != '':
            return replacements, values[0]
    return replacements


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("../input/day19").open(encoding="UTF-8") as f:
        VALUES, STR = parse(f)

        print(f"Phase 1: {phase1(STR)}")
        print(f"Phase 2: {phase2(VALUES)}")
