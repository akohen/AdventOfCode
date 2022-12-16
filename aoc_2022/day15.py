from pathlib import Path
import re

def get_distance(point_1, point_2):
    return abs(point_1[0]-point_2[0]) + abs(point_1[1]-point_2[1])

def phase1(data, y=10):
    sensors, beacons = {}, set()
    for sx,sy,bx,by in data:
        distance = get_distance((sx,sy),(bx,by))
        sensors[(sx,sy)] = distance
        beacons.add((bx,by))

    result, segments = 0, []
    # |Sx-x| + |Sy-y| < D   <=>   x = [Sx-D+|Sy-y|; Sx+D-|Sy-y|]
    for (sx,sy), d in sensors.items():
        segment = [sx - d + abs(sy-y), sx + d - abs(sy-y)]
        if segment[0] <= segment[1]:
            segments.append(segment)

    result, current = 0, []
    for a, b in sorted(segments):
        if not current:
            current = [a, b]
        elif a > current[1]:
            result += current[1] - current[0] + 1
            current = [a, b]
        elif b > current[1]:
            current[1] = b
    result += current[1] - current[0] + 1

    for bx, by in beacons:
        if by == y:
            result -= 1
    return result

def phase2(data, max_search):
    sensors = {}
    for sx,sy,bx,by in data:
        distance = get_distance((sx,sy),(bx,by))
        sensors[(sx,sy)] = distance

    for (sx,sy), d in sensors.items():
        for i in range(-d-1,d+2):
            x = sx + i
            y1 = sy +d-abs(i)+1
            y2 = sy-d+abs(i)-1
            if x > max_search or y1 > max_search or x < 0 or y1 < 0 or y2 < 0:
                continue
            if all(get_distance((x,y1),s2) > d2 for (s2), d2 in sensors.items()):
                return x*4000000+y1
            if all(get_distance((x,y2),s2) > d2 for (s2), d2 in sensors.items()):
                return x*4000000+y2

def parse(file):
    rule = re.compile(r"^Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)")
    return [[int(x) for x in rule.findall(line)[0]] for line in file.split('\n')]


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/"+Path(__file__).stem).open(encoding="UTF-8") as f:
        DATA = parse(f.read())

        print(f"Phase 1: {phase1(DATA,2000000)}")
        print(f"Phase 2: {phase2(DATA, 4000000)}")
