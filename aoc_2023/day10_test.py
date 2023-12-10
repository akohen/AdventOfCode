from aoc_2023 import day10

test_data = day10.parse("""-L|F7
7S-7|
L|7||
-L-J|
L|-JF""")
                        
test_data2 = day10.parse("""..F7.
.FJ|.
SJ.L7
|F--J
LJ...""")
                                            
test_data3 = day10.parse("""..........
.S------7.
.|F----7|.
.||....||.
.||....||.
.|L-7F-J|.
.|..||..|.
.L--JL--J.
..........""")


def test_day10():
    assert day10.part2(test_data)[0] == 4
    assert day10.part2(test_data2)[0] == 8
    assert day10.part2(test_data3)[1] == 4
