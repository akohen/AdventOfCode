from pathlib import Path

def part1(data):
    def distance(a, b): return abs(a[0]-b[0]) + abs(a[1]-b[1])

    cols, rows = set(), set()
    for galaxy in data:
        cols.add(galaxy[1]) # at least 1 galaxy on column Y
        rows.add(galaxy[0])
    galaxies = [(
            2*galaxy[0]-len([x for x in rows if x < galaxy[0]]), 
            2*galaxy[1]-len([x for x in cols if x < galaxy[1]]), 
        ) for galaxy in data]
    
    paths = [distance(g1,g2) for g1 in galaxies for g2 in galaxies]
    return sum(paths)//2


def part2(data, f):
    def distance(a, b): return abs(a[0]-b[0]) + abs(a[1]-b[1])

    cols, rows = set(), set()
    for galaxy in data:
        cols.add(galaxy[1]) # at least 1 galaxy on column Y
        rows.add(galaxy[0])
    galaxies = [(
            galaxy[0] + (f-1)*(galaxy[0]-len([x for x in rows if x < galaxy[0]])), 
            galaxy[1] + (f-1)*(galaxy[1]-len([x for x in cols if x < galaxy[1]])), 
        ) for galaxy in data]
    
    paths = [distance(g1,g2) for g1 in galaxies for g2 in galaxies]
    return sum(paths)//2


def parse(file):
    data = file.split('\n')
    return [(x,y) for x in range(len(data)) for y in range(len(data[0])) if data[x][y] == '#']


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/"+Path(__file__).stem).open(encoding="UTF-8") as f:
        DATA = parse(f.read())

        print(f"Phase 1: {part1(DATA)}")
        print(f"Phase 2: {part2(DATA, 1000000)}")
