from pathlib import Path
from typing import DefaultDict
from itertools import permutations
from math import factorial


def phase1(guests):
    happiness, count = 0, 0
    for perm in permutations(guests.keys()):
        h = 0
        for i in range(-1,len(perm)-1):
            h += guests[perm[i]][perm[i+1]]
            h += guests[perm[i+1]][perm[i]]
        happiness = max(happiness, h)
        count += 1
        if count > factorial(len(guests)-1):
            return happiness


def phase2(guests):
    guests['you'] = DefaultDict(lambda: 0)
    return phase1(guests)


def parse(text):
    guests = DefaultDict(lambda: DefaultDict(lambda: 0))
    for gst in [line.rstrip('.\n').split(' ') for line in text]:
        guests[gst[0]][gst[-1]] = int(gst[3]) if gst[2] == 'gain' else -int(gst[3])
    return guests


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("../input/day13").open(encoding="UTF-8") as f:
        GUESTS = parse(f)

        print(f"Phase 1: {phase1(GUESTS)}")
        print(f"Phase 2: {phase2(GUESTS)}")
