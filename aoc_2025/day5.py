from pathlib import Path


def get_merged_ranges(ranges):
    merged_ranges = []
    for r in sorted(ranges):
        if not merged_ranges or merged_ranges[-1][1] < r[0]:
            merged_ranges.append(r)
        else:
            merged_ranges[-1] = (merged_ranges[-1][0], max(merged_ranges[-1][1], r[1]))
    return merged_ranges


def part1(ranges, ingredients):
    return sum(
        any(r[0] <= ingredient <= r[1] for r in get_merged_ranges(ranges))
        for ingredient in ingredients
    )


def part2(ranges, _):
    return sum(
        r[1] - r[0] + 1
        for r in get_merged_ranges(ranges)
    )


def parse(file):
    ranges, ingredients = file.split('\n\n')
    return [
            (int(x[0]), int(x[1])) for line in ranges.splitlines() if (x:= line.split('-'))
        ], [
            int(x) for x in ingredients.splitlines()
        ]


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/"+Path(__file__).stem).open(encoding="UTF-8") as f:
        DATA = parse(f.read())

        print(f"Phase 1: {part1(*DATA)}")
        print(f"Phase 2: {part2(*DATA)}")
