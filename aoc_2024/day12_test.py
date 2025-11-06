from aoc_2024 import day12

test_data = day12.parse("""AAAA
BBCD
BBCC
EEEC""")

test_data2 = day12.parse("""RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE""")

test_data3 = day12.parse("""AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA""")

def test_day12():
    assert day12.part1(test_data) == 140
    assert day12.part1(test_data2) == 1930
    assert day12.part2(test_data) == 80
    assert day12.part2(test_data2) == 1206
    assert day12.part2(test_data3) == 368
