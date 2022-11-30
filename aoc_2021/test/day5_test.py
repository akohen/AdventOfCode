from aoc_2021.src import day5 as day

test_data = day.parse("""0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2""")

def test_phase1():
    assert day.phase1(test_data) == 5

def test_phase2():
    assert day.phase2(test_data) == 12
