from aoc_2025 import day1

test_data = day1.parse("""L68
L30
R48
L5
R60
L55
L1
L99
R14
L82""")


def test_day1():
    assert day1.part1(test_data) == 3
    assert day1.part2(test_data) == 6
