from pathlib import Path
import re
import math


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])

def mul(a, b):
    return (a[0] * b[0], a[1] * b[0])

def mod(a, b):
    return (a[0] % b[0], a[1] % b[1])

def get_safety_score(robots, dimensions):
    quadrants = [0,0,0,0]
    for position, _ in robots:
        if position[0] < dimensions[0] // 2 and position[1] < dimensions[1] // 2:
            quadrants[0] += 1
        elif position[0] > dimensions[0] // 2 and position[1] < dimensions[1] // 2:
            quadrants[1] += 1
        elif position[0] < dimensions[0] // 2 and position[1] > dimensions[1] // 2:
            quadrants[2] += 1
        elif position[0] > dimensions[0] // 2 and position[1] > dimensions[1] // 2:
            quadrants[3] += 1

    return math.prod(quadrants)

def part1(robots, dimensions = (11,7), steps = 1):
    final_positions = []
    for position, velocity in robots:
        change = mul(velocity, (steps, steps))
        new_position = mod(add(position, change), dimensions)
        final_positions.append((new_position, velocity))
    return get_safety_score(final_positions, dimensions)


def part2(robots, dimensions = (11,7)):
    positions = robots.copy()
    for step in range(10000):
        new_positions = []
        for position, velocity in positions:
            new_position = mod(add(position, velocity), dimensions)
            new_positions.append((new_position, velocity))
        positions = new_positions
        new_score = get_safety_score(positions, dimensions)
        if new_score < 90000000:
            return step + 1


def parse(file):
    return [((int(x[0]), int(x[1])),(int(x[2]), int(x[3]))) for line in file.split('\n') if (x := re.findall( r"-?\d+", line))]


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/"+Path(__file__).stem).open(encoding="UTF-8") as f:
        DATA = parse(f.read())

        print(f"Phase 1: {part1(DATA, (101, 103), 100)}")
        print(f"Phase 2: {part2(DATA, (101, 103))}")
