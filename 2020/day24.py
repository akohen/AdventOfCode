from pathlib import Path
from collections import defaultdict
import sys

TEST_MODE = bool(len(sys.argv) > 1 and sys.argv[1] == "test")

SHIFTS = {'w': (-1,0), 'e': (1,0), 'nw': (0,-1), 'se': (0,1), 'ne': (1,-1), 'sw': (-1,1)}

def get_shift(instruction, ptr):
    end = ptr+2 if instruction[ptr] != 'w' and instruction[ptr] != 'e' else ptr+1
    return SHIFTS[instruction[ptr:end]], end

def add(t1,t2):
    return (t1[0]+t2[0], t1[1]+t2[1])

def count_neighbors(tile, flipped):
    return sum([flipped[add(tile, shift)] for shift in SHIFTS.values()])

def solve(data):
    flipped = defaultdict(int)
    corners = ((0,0),(0,0))
    for line in data:
        tile, ptr = (0,0,0), 0
        while ptr < len(line):
            shift, ptr = get_shift(line, ptr)
            tile = add(tile, shift)
            corners = (
                ( min(tile[0],corners[0][0]), min(tile[1],corners[0][1]) ),
                ( max(tile[0],corners[1][0]), max(tile[1],corners[1][1]) )
            )
        flipped[tile] ^= 1
    
    p1 = sum(flipped.values())
    
    for i in range(100):
        next_iteration = defaultdict(int)
        for q in range(corners[0][0]-1, corners[1][0]+2):
            for r in range(corners[0][1]-1, corners[1][1]+2):
                neighbors = count_neighbors((q,r), flipped)
                if (flipped[(q,r)] == 1 and neighbors == 1) or (flipped[(q,r)] == 1 and neighbors == 2) or (flipped[(q,r)] == 0 and neighbors == 2):
                    next_iteration[(q,r)] = 1        
                    corners = (
                        ( min(q,corners[0][0]), min(r,corners[0][1]) ),
                        ( max(q,corners[1][0]), max(r,corners[1][1]) )
                    )
        flipped = next_iteration
        print(str(i)+"%", end="\r")
    return p1, sum(flipped.values())


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/day24_sample" if TEST_MODE else "input/day24").open() as f:
        DATA = [line.strip() for line in f]

        print('Phase 1: {}\nPhase 2: {}'.format(*solve(DATA)))
