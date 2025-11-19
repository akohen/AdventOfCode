from pathlib import Path
import heapq
from collections import defaultdict

DIRECTIONS = [(1, 0), (0, -1), (-1, 0), (0, 1)]

def step(a, direction):
    b = DIRECTIONS[direction]
    return (a[0] + b[0], a[1] + b[1])

def traverse(data):
    def get_start(data):
        for y, row in enumerate(data):
            for x, cell in enumerate(row):
                if cell == 'S':
                    return (x, y)
    queue = [(0, get_start(data), 0)]
    visited = defaultdict(lambda: float('inf'))
    while queue:
        cost, pos, direction = heapq.heappop(queue)
        if visited[(pos, direction)] <= cost:
            continue
        visited[(pos, direction)] = cost
        if data[pos[1]][pos[0]] == 'E':
            break
        for i in [-1, 0, 1]:
            new_direction = (direction + i) % 4
            new_pos = step(pos, new_direction)
            if data[new_pos[1]][new_pos[0]] == '#':
                continue
            new_cost = cost + (1 if i == 0 else 1001)
            heapq.heappush(queue, (new_cost, new_pos, new_direction))

    return visited

def part1(data):
    visited = traverse(data)
    end = list(visited.keys())[-1]
    return visited[end]

def part2(data):
    visited = traverse(data)
    end = list(visited.keys())[-1]
    path = set()
    to_visit = [end]

    while to_visit:
        point = to_visit.pop()
        if point in path:
            continue
        path.add(point[0])
        cost = visited[point]
        for i in range(4):
            for j in range(4):
                new_point = (step(point[0], i), j)
                if new_point not in visited:
                    continue
                new_cost = visited[new_point]
                if (new_cost + 1 == cost) or (new_cost + 1001 == cost):
                    to_visit.append(new_point)

    return len(path)


def parse(file):
    return [line for line in file.split('\n')]


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/"+Path(__file__).stem).open(encoding="UTF-8") as f:
        DATA = parse(f.read())

        print(f"Phase 1: {part1(DATA)}")
        print(f"Phase 2: {part2(DATA)}")
