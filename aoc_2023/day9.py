from pathlib import Path

def next_order(seq): return [seq[i+1] - seq[i] for i in range(len(seq)-1)]

def part1(data):
    def find_next(seq):
        if not any(seq): return 0
        return seq[-1] + find_next(next_order(seq))

    return sum(find_next(sequence) for sequence in data)


def part2(data):
    def find_first(seq):
        if not any(seq): return 0
        return seq[0] - find_first(next_order(seq))

    return sum(find_first(sequence) for sequence in data)

def parse(file):
    return [[int(x) for x in line.split(' ')] for line in file.split('\n')]


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/"+Path(__file__).stem).open(encoding="UTF-8") as f:
        DATA = parse(f.read())

        print(f"Phase 1: {part1(DATA)}")
        print(f"Phase 2: {part2(DATA)}")
