from aoc_2023 import day16
from pathlib import Path


def test_day16():
    with Path(__file__).parent.joinpath("input/day16_test").open(encoding="UTF-8") as f:
        test_data = day16.parse(f.read())
        assert day16.part1(*test_data) == 46
        assert day16.part2(*test_data) == 51
