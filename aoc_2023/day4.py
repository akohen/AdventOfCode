from pathlib import Path

def part1(cards):
    return sum(
        int(2**(len( set(card[0]).intersection(set(card[1])) )-1))
        for card in cards)


def part2(cards):
    values = [len( set(card[0]).intersection(set(card[1])) ) for card in cards]
    counts = [1] * len(cards)
    for id, card in enumerate(values):
        for i in range(card):
            counts[id+i+1] += counts[id]
    return sum(counts)

def parse(file):
    return [
        [
            [int(x) for x in nums.split(' ') if x]
            for nums in line.split(':')[1].split(' | ')
        ] for line in file.split('\n')
    ]


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/"+Path(__file__).stem).open(encoding="UTF-8") as f:
        DATA = parse(f.read())

        print(f"Phase 1: {part1(DATA)}")
        print(f"Phase 2: {part2(DATA)}")
