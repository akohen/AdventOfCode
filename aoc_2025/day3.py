from pathlib import Path

def part1(data):
    total = 0
    for row in data:
        first = max(row[:-1])
        i = row.index(first)
        total += 10 * first + max(row[i+1:])
    return total


def part2(data):
    def find_joltage(row, remaining):
        if remaining == 1:
            return [max(row)]
        next_digit = max(row[:-remaining+1])
        i = row.index(next_digit)
        return [next_digit] + find_joltage(row[i+1:], remaining-1)

    return sum(
        int(''.join(map(str,
            find_joltage(row, 12)
        )))
        for row in data
    )


def parse(file):
    return [[int(char) for char in line] for line in file.split('\n')]


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/"+Path(__file__).stem).open(encoding="UTF-8") as f:
        DATA = parse(f.read())

        print(f"Phase 1: {part1(DATA)}")
        print(f"Phase 2: {part2(DATA)}")
