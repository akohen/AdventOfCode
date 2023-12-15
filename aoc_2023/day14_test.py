from aoc_2023 import day14

test_data = day14.parse("""O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....""")


def test_day14():
    assert day14.part1(*test_data) == 136
    assert day14.part2(*test_data) == 64
