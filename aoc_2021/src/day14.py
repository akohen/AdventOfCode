from pathlib import Path
from collections import Counter

def pair_insertion_process(polymer, rules, depth=1):
    elements, pairs = Counter(polymer), Counter()
    for i in range( sum(elements.values()) -1 ):
        pairs[polymer[i:i+2]] += 1
    
    for _ in range(depth):
        prev_pairs, pairs = pairs.items(), Counter()
        for pair, count in prev_pairs:
            reaction = rules[pair]
            elements[reaction] += count
            pairs[pair[0]+reaction] += count
            pairs[reaction+pair[1]] += count

    values = sorted(elements.values())
    return values[-1] - values[0]


def part1(polymer, rules):
    return pair_insertion_process(polymer, rules, 10)


def part2(polymer, rules):
    return pair_insertion_process(polymer, rules, 40)


def parse(file):
    polymer, rules = file.split('\n\n')
    return [
        polymer,
        { rule[:2]: rule[6] for rule in rules.split('\n') }
    ]


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("../input/day14").open(encoding="UTF-8") as f:
        DATA = parse(f.read())

        print(f"Phase 1: {part1(*DATA)}")
        print(f"Phase 2: {part2(*DATA)}")
