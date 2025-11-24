from aoc_2024 import day19

test_data = day19.parse("""r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb""")


def test_day19():
    assert day19.part1(*test_data) == 6
    assert day19.part2(*test_data) == 16
