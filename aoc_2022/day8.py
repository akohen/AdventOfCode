import math
from pathlib import Path

def phase1(data):
    cols = list(map(list, zip(*data))) # yolo

    visible = set( # horizontal
        (x,y) for y in range(len(data[0])) for x in range(len(data))
        if not data[x][:y] or not data[x][y+1:] or data[x][y] > max(data[x][:y]) or data[x][y] > max(data[x][y+1:])
    ).union(set( # vertical
        (y,x) for y in range(len(cols[0])) for x in range(len(cols))
        if not cols[x][:y] or not cols[x][y+1:] or cols[x][y] > max(cols[x][:y]) or cols[x][y] > max(cols[x][y+1:])
    ))
    return len(visible)


def phase2(data):
    max_tree = 0

    def get_visible_trees(a, b):
        v = [0,0,0,0]
        for y in range(b+1, len(data[a])): # right
            v[0] += 1
            if data[a][y] >= data[a][b]:
                break
        for y in range(b-1, -1, -1): # left
            v[1] += 1
            if data[a][y] >= data[a][b]:
                break
        for x in range(a+1, len(data)): # down
            v[2] += 1
            if data[x][b] >= data[a][b]:
                break
        for x in range(a-1, -1, -1): # up
            v[3] += 1
            if data[x][b] >= data[a][b]:
                break
        return math.prod(v)

    for x in range(len(data)):
        for y in range(len(data[0])):
            visible_trees = get_visible_trees(x, y)
            if visible_trees > max_tree:
                max_tree = visible_trees

    return max_tree


def parse(file):
    return [[int(x) for x in line] for line in file.split('\n')]


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/"+Path(__file__).stem).open(encoding="UTF-8") as f:
        DATA = parse(f.read())

        print(f"Phase 1: {phase1(DATA)}")
        print(f"Phase 2: {phase2(DATA)}")
