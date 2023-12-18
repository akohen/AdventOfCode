from pathlib import Path


D = {'L':(0,-1), 'R':(0,1), 'D':(1,0), 'U':(-1,0)}

def part1(data):
    area, curr = 0, (0,0)
    for dir, count, _ in data:
        next_point = (curr[0] + D[dir][0] * count, curr[1] + D[dir][1] * count)
        area += count + (curr[0] + next_point[0]) * (curr[1] - next_point[1])
        curr = next_point
    return area//2+1


def part2(data):
    area, curr = 0, (0,0)
    for _, _, part2 in data:
        dir, count = 'RDLU'[int(part2[-1])], int(part2[:-1],16)
        next_point = (curr[0] + D[dir][0] * count, curr[1] + D[dir][1] * count)
        area += count + (curr[0] + next_point[0]) * (curr[1] - next_point[1])
        curr = next_point
    return area//2+1


def parse(file):
    return [(parts[0], int(parts[1]), parts[2][2:-1]) for line in file.split('\n') if (parts:=line.split(' '))]


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/"+Path(__file__).stem).open(encoding="UTF-8") as f:
        DATA = parse(f.read())

        print(f"Phase 1: {part1(DATA)}")
        print(f"Phase 2: {part2(DATA)}")
