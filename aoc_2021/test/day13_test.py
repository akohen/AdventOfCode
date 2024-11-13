from aoc_2021.src import day13

test_data = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""


def test_day13():
    parsed_data = day13.parse(test_data)
    assert day13.part1(*parsed_data) == 17
    assert day13.part2(*parsed_data) == """
#####
#...#
#...#
#...#
#####
.....
....."""
