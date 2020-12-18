from pathlib import Path
from collections import defaultdict
import sys

TEST_MODE = bool(len(sys.argv) > 1 and sys.argv[1] == "test")

def count_neighbors(cube, data):
    total = 0
    for x in range(-1,2):
        for y in range(-1,2):
            for z in range(-1,2):
                try:
                    if data[cube[0]+x][cube[1]+y][cube[2]+z] == 1 and not (x == 0 and y == 0 and z == 0):
                        total += 1
                except KeyError:
                    pass
    return total

def phase1(data):
    a = [0,0,0]
    b = [8,8,0]
    for i in range(6):
        next_a = a
        next_b = b
        next_cycle = defaultdict(lambda: defaultdict(dict))
        for x in range(a[0]-1,b[0]+2):
            for y in range(a[1]-1,b[1]+2):
                for z in range(a[2]-1,b[2]+2):
                    count = count_neighbors((x,y,z), data)
                    try:
                        if data[x][y][z] == 1 and (count == 2 or count == 3):
                            next_cycle[x][y][z] = 1
                            next_a = [min(next_a[0],x), min(next_a[1],y), min(next_a[2],z)]
                            next_b = [max(next_b[0],x), max(next_b[1],y), max(next_b[2],z)]
                        if data[x][y][z] == 0 and count == 3:
                            next_cycle[x][y][z] = 1
                            next_a = [min(next_a[0],x), min(next_a[1],y), min(next_a[2],z)]
                            next_b = [max(next_b[0],x), max(next_b[1],y), max(next_b[2],z)]
                    except KeyError:
                        if count == 3:
                            next_cycle[x][y][z] = 1
                            next_a = [min(next_a[0],x), min(next_a[1],y), min(next_a[2],z)]
                            next_b = [max(next_b[0],x), max(next_b[1],y), max(next_b[2],z)]
        a = next_a
        b = next_b
        data = next_cycle
    total = 0
    for x in data:
        for y in data[x]:
            for z in data[x][y]:
             total += 1
    return total


def count_neighbors_4(cube, data):
    total = 0
    for x in range(-1,2):
        for y in range(-1,2):
            for z in range(-1,2):
                for w in range(-1,2):
                    try:
                        if data[cube[0]+x][cube[1]+y][cube[2]+z][cube[3]+w] == 1 and not (x == 0 and y == 0 and z == 0 and w == 0):
                            total += 1
                    except KeyError:
                        pass
    return total

def phase2(data):
    a = [0,0,0,0]
    b = [8,8,0,0]
    for i in range(6):
        next_a = a
        next_b = b
        next_cycle = defaultdict(lambda: defaultdict(lambda: defaultdict(dict)))
        for x in range(a[0]-1,b[0]+2):
            for y in range(a[1]-1,b[1]+2):
                for z in range(a[2]-1,b[2]+2):
                    for w in range(a[3]-1,b[3]+2):
                        count = count_neighbors_4((x,y,z,w), data)
                        try:
                            if data[x][y][z][w] == 1 and (count == 2 or count == 3):
                                next_cycle[x][y][z][w] = 1
                                next_a = [min(next_a[0],x), min(next_a[1],y), min(next_a[2],z), min(next_a[3],w)]
                                next_b = [max(next_b[0],x), max(next_b[1],y), max(next_b[2],z), max(next_b[3],w)]
                            if data[x][y][z][w] == 0 and count == 3:
                                next_cycle[x][y][z][w] = 1
                                next_a = [min(next_a[0],x), min(next_a[1],y), min(next_a[2],z), min(next_a[3],w)]
                                next_b = [max(next_b[0],x), max(next_b[1],y), max(next_b[2],z), max(next_b[3],w)]
                        except KeyError:
                            if count == 3:
                                next_cycle[x][y][z][w] = 1
                                next_a = [min(next_a[0],x), min(next_a[1],y), min(next_a[2],z), min(next_a[3],w)]
                                next_b = [max(next_b[0],x), max(next_b[1],y), max(next_b[2],z), max(next_b[3],w)]
        a = next_a
        b = next_b
        data = next_cycle
    total = 0
    for x in data:
        for y in data[x]:
            for z in data[x][y]:
                for w in data[x][y][z]:
                    total += 1
    return total

def load(data):
    dimension = defaultdict(lambda: defaultdict(dict))
    dimension2 = defaultdict(lambda: defaultdict(lambda: defaultdict(dict)))
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            dimension[x][y][0] = 1 if char == '#' else 0
            dimension2[x][y][0][0] = 1 if char == '#' else 0

    return dimension, dimension2

if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/day17_sample" if TEST_MODE else "input/day17").open() as f:
        DATA, P2 = load([line.strip() for line in f])

        print('Phase 1: {}'.format(phase1(DATA)))
        print('Phase 2: {}'.format(phase2(P2)))