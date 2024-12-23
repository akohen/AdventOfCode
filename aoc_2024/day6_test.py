from aoc_2024 import day6

test_data = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""


def test_day6():
    parsed_data = day6.parse(test_data)
    assert day6.part1(parsed_data) == 41
    assert day6.part2(parsed_data) == 6