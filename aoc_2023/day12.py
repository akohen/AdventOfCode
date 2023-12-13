from pathlib import Path
from functools import cache

@cache
def count_arrangements(arr, pattern, current_group=0):
    if not arr: return int(not pattern and not current_group)
    result = 0
    for c in [".", "#"] if arr[0] == "?" else arr[0]:
        if c == "#":
            result += count_arrangements(arr[1:], pattern, current_group + 1)
        else:
            if current_group:
                if pattern and pattern[0] == current_group:
                    result += count_arrangements(arr[1:], pattern[1:])
            else:
                result += count_arrangements(arr[1:], pattern)
    return result

def part1(data):
    return sum([count_arrangements(line[0]+'.', line[1]) for line in data])


def part2(data):
    return sum([count_arrangements('?'.join([line[0]]*5)+'.', line[1]*5) for line in data])


def parse(file):
    return [(
        parts[0],
        tuple(int(x) for x in parts[1].split(','))
        ) for line in file.split('\n') if (parts:=line.split(' '))]


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/"+Path(__file__).stem).open(encoding="UTF-8") as f:
        DATA = parse(f.read())

        print(f"Phase 1: {part1(DATA)}")
        print(f"Phase 2: {part2(DATA)}")
