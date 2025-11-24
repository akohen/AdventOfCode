from pathlib import Path
import re

def get_cost(machine):
    a, b, prizes = machine
    a_num = b[1] * prizes[0] - b[0] * prizes[1]
    b_num = a[1] * prizes[0] - a[0] * prizes[1]
    den = a[0] * b[1] - a[1] * b[0]
    if den == 0 or a_num % den != 0 or b_num % den != 0:
        return 0
    return (3 * a_num - b_num) // den


def part1(data):
    return sum(get_cost(machine) for machine in data)


def part2(data):
    total = 0
    for a, b, prizes in data:
        new_prizes = (prizes[0] + 10000000000000, prizes[1] + 10000000000000)
        total += get_cost((a,b,new_prizes))
    return total


def parse(file):
    return [
        (x[:2], x[2:4], x[4:6])
        for line in file.split('\n\n')
        if (x := list(map(int, re.findall( r"\d+", line))))
    ]


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/"+Path(__file__).stem).open(encoding="UTF-8") as f:
        DATA = parse(f.read())

        print(f"Phase 1: {part1(DATA)}")
        print(f"Phase 2: {part2(DATA)}")
