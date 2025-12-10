from aoc_2025 import day9

test_data = day9.parse("""7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3""")


def test_day9():
    assert day9.part1(test_data) == 50
    assert day9.part2(test_data) == 24
