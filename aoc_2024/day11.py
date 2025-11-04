from pathlib import Path
from collections import defaultdict

def blink(stone):
    if stone == 0:
        return [1]
    elif len(str(stone)) % 2 == 0:
        middle = len(str(stone))//2
        return [int(str(stone)[:middle]), int(str(stone)[middle:])]
    else:
        return [stone * 2024]

def part1(data, depth=25):
    stones = defaultdict(int)
    for stone in data:
        stones[stone] += 1
    for _ in range(depth):
        next_stones = defaultdict(int)
        for stone, count in stones.items():
            for new_stone in blink(stone):
                next_stones[new_stone] += count
        stones = next_stones
    return sum(stones.values())


def parse(file):
    return [int(x) for x in file.split(' ')]


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/"+Path(__file__).stem).open(encoding="UTF-8") as f:
        DATA = parse(f.read())

        print(f"Phase 1: {part1(DATA)}")
        print(f"Phase 2: {part1(DATA, depth=75)}")
