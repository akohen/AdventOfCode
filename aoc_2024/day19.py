from pathlib import Path
from functools import cache


def part1(patterns, designs):
    def is_design_possible(patterns, design):
        if len(design) == 0:
            return True
        return any(
            design.startswith(pattern) and
            is_design_possible(patterns, design[len(pattern):])
            for pattern in patterns
        )
    return sum(1 for design in designs if is_design_possible(patterns, design))


def part2(patterns, designs):
    @cache
    def count_patterns(patterns, design):
        if len(design) == 0:
            return 1
        return sum(
            count_patterns(patterns, design[len(pattern):])
            for pattern in patterns
            if design.startswith(pattern)
        )
    return sum(count_patterns(patterns, design) for design in designs)


def parse(file):
    patterns, designs = file.split('\n\n')
    return tuple(patterns.split(', ')), designs.splitlines()


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/"+Path(__file__).stem).open(encoding="UTF-8") as f:
        DATA = parse(f.read())

        print(f"Phase 1: {part1(*DATA)}")
        print(f"Phase 2: {part2(*DATA)}")
