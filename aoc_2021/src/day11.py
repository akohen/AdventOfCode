from pathlib import Path
from copy import deepcopy

def phase1(octopuses, steps=100):
    flashes = 0
    for _ in range(steps):
        flashed = []
        for x in range(10):
            for y in range(10):
                octopuses[x][y] += 1
                if octopuses[x][y] == 10:
                    octopuses[x][y] = 0
                    flashed.append((x,y))
        for x,y in flashed:
            for a,b in [(i,j) for i in range(-1,2) for j in range(-1,2)]:
                if (x1 := x+a) >= 0 and (y1 := y+b) >= 0 and x1 < 10 and y1 < 10:
                    if (x1,y1) not in flashed:
                        octopuses[x1][y1] += 1
                        if octopuses[x1][y1] >= 10:
                            octopuses[x1][y1] = 0
                            flashed.append((x1,y1))
        flashes += len(flashed)

        if len(flashed) == 100:
            return _+1
    return flashes

def parse(file):
    return [[int(x) for x in line] for line in file.split('\n')]

if __name__ == "__main__":
    with Path(__file__).parent.joinpath("../input/"+Path(__file__).stem).open(encoding="UTF-8") as f:
        DATA = parse(f.read())

        print(f"Phase 1: {phase1(deepcopy(DATA))}")
        print(f"Phase 2: {phase1(DATA, 500)}")
