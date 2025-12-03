from aoc_2025 import day3

test_data = day3.parse("""987654321111111
811111111111119
234234234234278
818181911112111""")


def test_day3():
    assert day3.part1(test_data) == 357
    assert day3.part2(test_data) == 3121910778619
