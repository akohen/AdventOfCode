from aoc_2024 import day4

test_data = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""


def test_day4():
    parsed_data = day4.parse(test_data)
    assert day4.part1(parsed_data) == 18
    assert day4.part2(parsed_data) == 9
