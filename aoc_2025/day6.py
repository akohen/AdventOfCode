from pathlib import Path
from math import prod

def part1(data):
    total = 0
    for row in data:
        if row[-1] == '+':
            total += sum(row[:-1])
        else:
            total += prod(row[:-1])
    return total


def part2(file):
    lines = file.splitlines()
    rows, current_row, current_op = [], [], ''

    for i in range(len(lines[0])):
        current_number = [lines[j][i] for j in range(len(lines)-1) if lines[j][i] != ' ']
        if lines[-1][i] != ' ':
            current_op = lines[-1][i]
        if len(current_number) == 0:
            current_row.append(current_op)
            rows.append(current_row)
            current_row = []
        else:
            current_row.append(int(''.join(current_number)))
    current_row.append(current_op)
    rows.append(current_row)

    return part1(rows)




def parse(file):
    values = [
        [ int(x) if x.isnumeric() else x for x in line.split() ]
        for line in file.splitlines()
    ]
    return list(zip(*values))


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/"+Path(__file__).stem).open(encoding="UTF-8") as f:
        DATA = f.read()

        print(f"Phase 1: {part1(parse(DATA))}")
        print(f"Phase 2: {part2(DATA)}")