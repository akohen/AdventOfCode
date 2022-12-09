from aoc_2022 import day9 as day

test_data = day.parse("""R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2""")

test_data2 = day.parse("""R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20""")

def test_day9():
    assert day.phase1(test_data) == 13
    assert day.phase2(test_data2) == 36
