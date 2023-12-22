from pathlib import Path
from collections import deque

def is_overlap(a,b):
    if (a[0][1] <= b[1][1] and a[1][1] >= b[0][1] and
     a[1][0] >= b[0][0] and a[0][0] <= b[1][0] ):
        return True
    return False

def settle_bricks(data):
    bricks = sorted(data, key=lambda x:x[0][2], reverse=True)
    settled = {}
    while len(bricks) > 0:
        brick, level, below = bricks.pop(), 0, []
        for other in settled:
            if other[1][2] < level: continue
            if is_overlap(brick, other):
                if level == other[1][2]: below.append(other)
                else:
                    level = other[1][2]
                    below = [other]
        new_position = ((brick[0][0],brick[0][1],level+1),(brick[1][0],brick[1][1],level+1+brick[1][2]-brick[0][2]))
        settled[new_position] = {"below":below, "above":[]}
        for b in below:
            settled[b]['above'].append(new_position)
    return settled

def part1(data):
    settled = settle_bricks(data)
    to_remove = [b for b in settled if all(len(settled[a]['below']) > 1 for a in settled[b]['above'])]
    return len(to_remove)
    


def part2(data):
    settled = settle_bricks(data)
    total = 0

    for brick in settled:
        will_fall, to_open = set([brick]), deque(settled[brick]['above'])
        while len(to_open) > 0:
            b = to_open.popleft()
            if all(below in will_fall for below in settled[b]['below']):
                will_fall.add(b)
                to_open.extend(settled[b]['above'])
        total += len(will_fall)-1
    return total


def parse(file):
    return [(a[:3],a[3:]) for line in file.split('\n') if (a := tuple(map(int,line.replace('~',',').split(','))))]


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/"+Path(__file__).stem).open(encoding="UTF-8") as f:
        DATA = parse(f.read())

        print(f"Phase 1: {part1(DATA)}")
        print(f"Phase 2: {part2(DATA)}")
