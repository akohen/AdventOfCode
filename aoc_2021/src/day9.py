import math
from pathlib import Path

def phase1(map):
    h_mins = set((x,y) for y in range(len(map[0])) for x in range(len(map)) if map[x][y] < min(map[x][y-1:y]+map[x][y+1:y+2]))
    cols = list(zip(*map))
    v_mins = set((y,x) for y in range(len(cols[0])) for x in range(len(cols)) if cols[x][y] < min(cols[x][y-1:y]+cols[x][y+1:y+2]))
    return sum([1+map[x][y] for x,y in h_mins.intersection(v_mins)])


def phase2(map):
    h_mins = set((x,y) for y in range(len(map[0])) for x in range(len(map)) if map[x][y] < min(map[x][y-1:y]+map[x][y+1:y+2]))
    cols = list(zip(*map))
    v_mins = set((y,x) for y in range(len(cols[0])) for x in range(len(cols)) if cols[x][y] < min(cols[x][y-1:y]+cols[x][y+1:y+2]))
    basins = h_mins.intersection(v_mins)
    sizes = []
    for basin in basins:
        seen, to_open = [], [basin]
        while len(to_open) > 0:
            curr = to_open.pop()
            if curr not in seen:
                seen.append(curr)
                x,y = curr
                if x < len(map)-1 and map[x+1][y] < 9: to_open.append((x+1,y))
                if x > 0 and map[x-1][y] < 9: to_open.append((x-1,y))
                if y < len(map[0])-1 and map[x][y+1] < 9: to_open.append((x,y+1))
                if y > 0 and map[x][y-1] < 9: to_open.append((x,y-1))
        sizes.append(len(seen))

    return math.prod(sorted(sizes)[-3:])


def parse(file):
    return [[int(x) for x in line] for line in file.split('\n')]

if __name__ == "__main__":
    with Path(__file__).parent.joinpath("../input/"+Path(__file__).stem).open(encoding="UTF-8") as f:
        DATA = parse(f.read())

        print(f"Phase 1: {phase1(DATA)}")
        print(f"Phase 2: {phase2(DATA)}")
