from pathlib import Path

NEIGHBORS = [(-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1)]

def add(a, b):
    return (a[0]+b[0], a[1]+b[1], a[2]+b[2])

def phase1(cubes):
    return sum([len({add(cube, dir) for dir in NEIGHBORS} - cubes) for cube in cubes])


def phase2(cubes):
    def get_trapped_cubes(chunk):
        adjacent = set(chunk)
        for cube in chunk:
            for x in cube:
                if x > 19 or x < 1:
                    return 0
            adjacent.update({add(cube, dir) for dir in NEIGHBORS} - cubes)
        if len(adjacent) == len(chunk):
            return adjacent

        return get_trapped_cubes(adjacent)


    total_neighbors = sum([list({add(cube, dir) for dir in NEIGHBORS} - cubes) for cube in cubes],[])

    inside_count, inside_cubes = 0, set()
    for cube in total_neighbors:
        if cube in inside_cubes:
            inside_count += 1
        elif (chunk := get_trapped_cubes([cube])):
            inside_count += 1
            inside_cubes.update(chunk)

    return len(total_neighbors) - inside_count


def parse(file):
    return {tuple(int(x) for x in line.split(',')) for line in file.split('\n')}


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/"+Path(__file__).stem).open(encoding="UTF-8") as f:
        DATA = parse(f.read())

        print(f"Phase 1: {phase1(DATA)}")
        print(f"Phase 2: {phase2(DATA)}")
