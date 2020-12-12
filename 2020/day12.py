from pathlib import Path
from collections import defaultdict
import sys

TEST_MODE = bool(len(sys.argv) > 1 and sys.argv[1] == "test")

CARD = ['E', 'S', 'W', 'N']
DIRECTIONS = [(1,0),(0,1),(-1,0),(0,-1)]
ROTATIONS = [(1,0,0,1),(0,-1,1,0),(-1,0,0,-1),(0,1,-1,0)]

def phase1(data):
    pos = [0,0]
    facing = 0
    for l, val in data:
        if l in CARD:
            pos[0] += DIRECTIONS[CARD.index(l)][0] * val
            pos[1] += DIRECTIONS[CARD.index(l)][1] * val
        elif l == 'F':
            pos[0] += DIRECTIONS[facing][0] * val
            pos[1] += DIRECTIONS[facing][1] * val
        elif l == 'L':
            facing = (facing - val//90) % 4
        elif l == 'R':
            facing = (facing + val//90) % 4
    return abs(pos[0])+abs(pos[1])

def phase2(data):
    pos = [0,0]
    wp = [10,-1]
    for l, val in data:
        if l in CARD:
            wp[0] += DIRECTIONS[CARD.index(l)][0] * val
            wp[1] += DIRECTIONS[CARD.index(l)][1] * val
        elif l == 'F':
            pos[0] += wp[0] * val
            pos[1] += wp[1] * val
        else:
            direction = 1 if l == 'R' else -1
            matrix = ROTATIONS[direction*val//90]
            wp = [wp[0]*matrix[0]+wp[1]*matrix[1],wp[0]*matrix[2]+wp[1]*matrix[3]]
    return abs(pos[0])+abs(pos[1])

if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/day12_sample" if TEST_MODE else "input/day12").open() as f:
        INSTRUCTIONS = [(line[0], int(line[1:].strip())) for line in f]

        print('Phase 1: {}'.format(phase1(INSTRUCTIONS)))
        print('Phase 2: {}'.format(phase2(INSTRUCTIONS)))