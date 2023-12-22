from aoc_2023 import day22

test_data = day22.parse("""1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9""")


def test_day22():
    assert day22.part1(test_data) == 5
    assert day22.part2(test_data) == 7
