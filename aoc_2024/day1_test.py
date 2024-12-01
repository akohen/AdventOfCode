from aoc_2024 import day1

test_data = day1.parse("""3   4
4   3
2   5
1   3
3   9
3   3""")


def test_day1():
    assert day1.part1(test_data) == 11
    assert day1.part2(test_data) == 31
