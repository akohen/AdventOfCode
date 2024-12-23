from aoc_2024 import day9

test_data = day9.parse("""2333133121414131402""")


def test_day9():
    assert day9.part1(day9.parse("""12345""")) == 60
    assert day9.part1(test_data.copy()) == 1928
    assert day9.part2(test_data) == 2858
