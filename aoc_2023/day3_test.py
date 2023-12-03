from aoc_2023 import day3 as day

test_data = day.parse("""467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..""")


def test_day3():
    assert day.part1(*test_data) == 4361
    assert day.part2(*test_data) == 467835
