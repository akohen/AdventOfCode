from aoc_2025 import day4

test_data = day4.parse("""..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.""")


def test_day4():
    assert day4.part1(test_data) == 13
    assert day4.part2(test_data) == 43
