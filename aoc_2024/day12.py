from pathlib import Path
from collections import defaultdict

def get_neighbors(x, y, region):
    return [(x + dx, y + dy) for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)] if (x + dx, y + dy) in region]

def part1(data):
    def perimeter(region):
        return sum(
            4 - len(get_neighbors(x, y, region))
            for x, y in region
        )
    return sum(len(region) * perimeter(region) for region in data)


def part2(data):

    DIRECTIONS = [(0, 0), (1, 0), (0, 1), (1, 1)] # Corner (x,y) is top-left of cell (x,y)
    def count_sides(region):
        # list all the corners of each point in the region
        # For each corner, check how many of the 4 surrounding points are in the region
        corners, sides = set(), 0
        for x, y in region:
            for dx, dy in DIRECTIONS:
                corners.add((x + dx, y + dy))
        for cx, cy in corners:
            neighbors = [(cx - dx, cy - dy) for dx, dy in DIRECTIONS if (cx - dx, cy - dy) in region]
            if len(neighbors) == 1 or len(neighbors) == 3:
                sides += 1
            elif len(neighbors) == 2: # Check if neighbors are diagonal or aligned
                if (neighbors[0][0] != neighbors[1][0]) and (neighbors[0][1] != neighbors[1][1]):
                    sides += 2 # inside corner adds 2 sides
        return sides
    return sum(len(region) * count_sides(region) for region in data)


def parse(file):
    chars, regions = defaultdict(list), []
    for y, line in enumerate(file.splitlines()):
        for x, char in enumerate(line):
            chars[char].append((x, y))

    for points in chars.values():
        while points:
            current = points.pop()
            region = [current]
            to_visit = [current]
            while to_visit:
                x, y = to_visit.pop()
                for nx, ny in get_neighbors(x, y, points):
                    points.remove((nx, ny))
                    region.append((nx, ny))
                    to_visit.append((nx, ny))
            regions.append(sorted(region))

    return regions


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/"+Path(__file__).stem).open(encoding="UTF-8") as f:
        DATA = parse(f.read())
        
        print(f"Phase 1: {part1(DATA)}")
        print(f"Phase 2: {part2(DATA)}")
