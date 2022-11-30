from pathlib import Path
from typing import DefaultDict

def phase1(lines):
    seen = DefaultDict(int)
    for [x1,y1,x2,y2] in lines:
        if x1 == x2:
            for i in range(min(y1,y2),max(y1,y2)+1):
                seen[(x1,i)] += 1
        elif y1 == y2:
            for i in range(min(x1,x2),max(x1,x2)+1):
                seen[(i,y1)] += 1

    return len([i for i in seen.values() if i > 1])


def phase2(lines):
    seen = DefaultDict(int)
    for [x1,y1,x2,y2] in lines:
        x_dir = 1 if x2 >= x1 else -1
        y_dir = 1 if y2 >= y1 else -1
        x = list(range(x1, x2+x_dir, x_dir))
        y = list(range(y1, y2+y_dir, y_dir))
        x = x*len(y) if len(x) < len(y) else x
        y = y*len(x) if len(x) > len(y) else y
        for p in zip(x,y):
            seen[p] += 1
    return len([i for i in seen.values() if i > 1])


# returns array of [x1,y1,x2,y2]
def parse(file):
    return [[int(x) for point in line.split(' -> ') for x in point.split(',')] for line in file.split('\n')]

if __name__ == "__main__":
    with Path(__file__).parent.joinpath("../input/"+Path(__file__).stem).open(encoding="UTF-8") as f:
        LINES = parse(f.read())

        print(f"Phase 1: {phase1(LINES)}")
        print(f"Phase 2: {phase2(LINES)}")
