from operator import mul, add
from pathlib import Path


def check(ops, target, current, values, ):
    if len(values) == 0:
        return current == target
    if current > target:
        return False
    if len(values) > 0:
        return any(
            check(ops, target, op(current, values[0]), values[1:])
            for op in ops
        )


def part1(data):
    def is_solvable(equation):
        return check([add, mul], equation[0], equation[1][0], equation[1][1:])

    return sum(equation[0] for equation in data if is_solvable(equation))


def part2(data):
    def concat(a,b):
        return int(str(a) + str(b))
    def is_solvable(equation):
        return check([add, mul, concat], equation[0], equation[1][0], equation[1][1:])

    return sum(equation[0] for equation in data if is_solvable(equation))


def parse(file):
    return [
        [
            int(equation[0]),
            tuple(map(int, equation[1].split()))
        ] for line in file.split('\n') if (equation := line.split(': '))
    ]


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/"+Path(__file__).stem).open(encoding="UTF-8") as f:
        DATA = parse(f.read())

        print(f"Phase 1: {part1(DATA)}")
        print(f"Phase 2: {part2(DATA)}")
