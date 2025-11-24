from aoc_2024 import day18

test_data = day18.parse("""5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0""")


def test_day18():
    assert day18.part1(test_data, 12, 6) == 22
    assert day18.part2(test_data, 12, 6) == '6,1'
