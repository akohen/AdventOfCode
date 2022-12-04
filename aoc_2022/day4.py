from pathlib import Path

def phase1(assignments):
    count = 0
    for a,b,c,d in assignments:
        if a <= c and b>= d or (c<=a and d>=b): count += 1
    return count


def phase2(assignments):
    count = 0
    for a,b,c,d in assignments:
        if not(c > b or d < a): count += 1
    return count


def parse(file):
    return [[int(x) for point in line.split(',') for x in point.split('-')] for line in file.split('\n')]


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/"+Path(__file__).stem).open(encoding="UTF-8") as f:
        DATA = parse(f.read())

        print(f"Phase 1: {phase1(DATA)}")
        print(f"Phase 2: {phase2(DATA)}")
