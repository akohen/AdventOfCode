from aoc_2023 import day13

test_data = day13.parse("""#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#""")


def test_day13():
    assert day13.part1(test_data) == 405
    assert day13.part2(test_data) == 400
