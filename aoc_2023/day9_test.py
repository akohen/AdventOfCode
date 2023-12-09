from aoc_2023 import day9

test_data = day9.parse("""0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45""")


def test_day9():
    assert day9.part1(test_data) == 114
    assert day9.part2(test_data) == 2
