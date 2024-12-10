from pathlib import Path
import re

def part1(data):
    return sum(
        int(a) * int(b)
        for a,b in re.findall(r"mul\((\d+),(\d+)\)", data)
    )


def part2(data):
    return sum(
        part1(chunk.split("don't()")[0])
        for chunk in data.split("do()")
    )


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/"+Path(__file__).stem).open(encoding="UTF-8") as f:
        DATA = f.read()

        print(f"Phase 1: {part1(DATA)}")
        print(f"Phase 2: {part2(DATA)}")
