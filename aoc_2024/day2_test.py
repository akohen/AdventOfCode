from aoc_2024 import day2

test_data = day2.parse("""7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9""")


def test_day2():
    assert day2.part1(test_data) == 2
    assert day2.part2(test_data) == 4
