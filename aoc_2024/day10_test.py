from aoc_2024 import day10

test_data = day10.parse("""0123
1234
8765
9876""")

test_data2 = day10.parse("""89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732""")

def test_day10():
    assert day10.part1(test_data) == 1
    assert day10.part1(test_data2) == 36
    assert day10.part2(test_data2) == 81
