from aoc_2023 import day6

test_data = """Time:      7  15   30
Distance:  9  40  200"""


def test_day6():
    assert day6.part1(day6.parse(test_data)) == 288
    assert day6.part2(day6.parse2(test_data)) == 71503
