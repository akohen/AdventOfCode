from pathlib import Path
from functools import cmp_to_key

def compare(left, right):
    if type(left) != type(right):
        if type(left) == int:
            return compare([left], right)
        else:
            return compare(left, [right])
    if type(left) == int:
        return 1 if left > right else (-1 if left < right else 0)


    for i in range(min(len(left), len(right))):
        comparison = compare(left[i], right[i])
        if comparison != 0:
            return comparison
    return 1 if len(left) > len(right) else (-1 if len(left) < len(right) else 0)


def phase1(data):
    result = 0
    
    for i, pair in enumerate(data):
        if compare(*pair) == -1:
            result += 1 + i
    return result


def phase2(data):
    packets = [x for pair in data for x in pair] + [[[2]],[[6]]]
    result = 1
    for i, key in enumerate(sorted(packets, key=cmp_to_key(compare))):
        if key in [[[2]],[[6]]]:
            result *= 1+i
    return result

def parse(file):
    return [[eval(x) for x in pair.split('\n')]for pair in file.split('\n\n')]


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/"+Path(__file__).stem).open(encoding="UTF-8") as f:
        DATA = parse(f.read())

        print(f"Phase 1: {phase1(DATA)}")
        print(f"Phase 2: {phase2(DATA)}")
