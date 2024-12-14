from pathlib import Path
from collections import defaultdict

def part1(size, antennas):
    antinodes = set()
    for nodes in antennas.values():
        for i, node in enumerate(nodes[:-1]):
            for other in nodes[i+1:]:
                diff = (node[0] - other[0], node[1] - other[1])
                for a in [
                    (node[0] + diff[0], node[1] + diff[1]),
                    (other[0] - diff[0], other[1] - diff[1])
                ]:
                    if 0 <= a[0] <= size and 0 <= a[1] <= size:
                        antinodes.add(a)
    return len(antinodes)


def part2(size, antennas):
    antinodes = set()
    for nodes in antennas.values():
        for i, node in enumerate(nodes[:-1]):
            for other in nodes[i+1:]:
                diff = (node[0] - other[0], node[1] - other[1])
                for i in range(size):
                    for a in [
                        (node[0] + i * diff[0], node[1] + i * diff[1]),
                        (other[0] - i * diff[0], other[1] - i * diff[1])
                    ]:
                        if 0 <= a[0] <= size and 0 <= a[1] <= size:
                            antinodes.add(a)
    return len(antinodes)


def parse(file):
    antennas = defaultdict(list)
    for x, row in enumerate(file.split('\n')):
        for y, c in enumerate(row):
            if c.isalnum():
                antennas[c].append((x, y))
    return x, antennas


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/"+Path(__file__).stem).open(encoding="UTF-8") as f:
        DATA = parse(f.read())

        print(f"Phase 1: {part1(*DATA)}")
        print(f"Phase 2: {part2(*DATA)}")
