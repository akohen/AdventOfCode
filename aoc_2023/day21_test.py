from aoc_2023 import day21

test_data = day21.parse("""...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........""")


def test_day21():
    assert day21.part1(test_data) == 16
    #assert day21.part2(test_data) == 1
