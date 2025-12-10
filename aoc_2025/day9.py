from pathlib import Path
from itertools import chain, combinations, pairwise


def intersects(x1, y1, x2, y2, x3, y3, x4, y4):
    return not (
        max(x1, x2) <= min(x3, x4)
        or max(x3, x4) <= min(x1, x2)
        or max(y1, y2) <= min(y3, y4)
        or max(y3, y4) <= min(y1, y2)
    )


def get_area(p1, p2):
    return (1+abs(p1[0] - p2[0])) * (1+abs(p1[1] - p2[1]))


def part1(data):
    return max(
        get_area(p, q)
        for p, q in combinations(data, 2)
    )


def part2(data):
    edges = [(p, q) for p, q in chain(pairwise(data), [(data[-1], data[0])])]

    max_area = max(
        get_area(p, q)
        for p, q in combinations(data, 2)
        if not any(intersects(*p, *q, *edge[0], *edge[1]) for edge in edges)
    )
    return max_area


def parse(file):
    return [tuple(int(x) for x in line.split(",")) for line in file.splitlines()]


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/"+Path(__file__).stem).open(encoding="UTF-8") as f:
        DATA = parse(f.read())

        print(f"Phase 1: {part1(DATA)}")
        print(f"Phase 2: {part2(DATA)}")