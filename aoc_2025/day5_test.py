from aoc_2025 import day5

test_data = day5.parse("""3-5
10-14
16-20
12-18

1
5
8
11
17
32""")


def test_day5():
    assert day5.part1(*test_data) == 3
    assert day5.part2(*test_data) == 14
