from pathlib import Path

def get_distance(point_1, point_2):
    return max( abs(point_1[0]-point_2[0]), abs(point_1[1]-point_2[1]) )

def phase1(data):

    directions, seen = {'L':(-1,0), 'R':(1,0), 'U':(0,1), 'D':(0,-1)}, set([(0,0)])
    tail, head = (0,0),(0,0)

    for direct, dist in data:
        for _ in range(dist):
            new_head = (head[0] + directions[direct][0], head[1]+directions[direct][1])
            if get_distance(new_head, tail) > 1:
                tail = head
                seen.add(tail)
            head = new_head
    return len(seen)


def phase2(data):
    sign = lambda x: -1 if x < 0 else (1 if x > 0 else 0)

    def update_rope(knot):
        if get_distance(rope[knot-1], rope[knot]) > 1:
            rope[knot] = (
                rope[knot][0] + sign(rope[knot-1][0]-rope[knot][0]),
                rope[knot][1] + sign(rope[knot-1][1]-rope[knot][1])
            )
            if knot < 9:
                update_rope(knot+1)

    directions, seen, rope = {'L':(-1,0), 'R':(1,0), 'U':(0,1), 'D':(0,-1)}, set([(0,0)]), [(0,0)]*10

    for direct, dist in data:
        for _ in range(dist):
            rope[0] = (rope[0][0] + directions[direct][0], rope[0][1]+directions[direct][1])
            update_rope(1)
            seen.add(rope[9])
    return len(seen)


def parse(file):
    return [(words[0], int(words[1])) for line in file.split('\n') if (words := line.split(' '))]


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/"+Path(__file__).stem).open(encoding="UTF-8") as f:
        DATA = parse(f.read())

        print(f"Phase 1: {phase1(DATA)}")
        print(f"Phase 2: {phase2(DATA)}")
