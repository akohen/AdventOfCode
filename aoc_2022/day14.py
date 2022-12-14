from pathlib import Path

def add_sand_grain(seen, y_max):
    x, y = 500, 0
    while y <= y_max:
        options = [position for step in [0,-1,1] if (position := (x + step, y + 1)) not in seen]
        if len(options) == 0:
            return x,y
        x,y = options[0]
    return x, y


def phase1(data):
    seen, y_max = set(), 0
    for path in data:
        for i, (x1, y1) in enumerate(path[:-1]):
            x2, y2 = path[i+1]
            y_max = max(y_max, y1, y2)
            if x1 == x2:
                for y in range(min(y1,y2), max(y1,y2)+1):
                    seen.add((x1,y))
            else:
                for x in range(min(x1,x2), max(x1,x2)+1):
                    seen.add((x,y1))
    result = 0
    while True:
        x, y = add_sand_grain(seen, y_max)
        if y > y_max:
            return result
        seen.add((x,y))
        result += 1


def phase2(data):
    seen, y_max, x_min, x_max = set(), 0, 999999, 0
    for path in data:
        for i, (x1, y1) in enumerate(path[:-1]):
            x2, y2 = path[i+1]
            y_max = max(y_max, y1, y2)
            x_min = min(x_min, x1, x2)
            x_max = max(x_max, x1, x2)
            if x1 == x2:
                for y in range(min(y1,y2), max(y1,y2)+1):
                    seen.add((x1,y))
            else:
                for x in range(min(x1,x2), max(x1,x2)+1):
                    seen.add((x,y1))
    for x in range(x_min-10, x_max+10):
        seen.add((x,y_max+2))
    result = 0

    while True:
        x, y = add_sand_grain(seen, y_max)
        if (x, y) == (500, 0):
            return result+1
        seen.add((x,y))
        result += 1

def parse(file):
    return [[
        [int(x) for x in pair.split(',')] for pair in line.split(' -> ')]
        for line in file.split('\n')]


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/"+Path(__file__).stem).open(encoding="UTF-8") as f:
        DATA = parse(f.read())

        print(f"Phase 1: {phase1(DATA)}")
        print(f"Phase 2: {phase2(DATA)}")
