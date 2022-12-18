
from aoc_2022 import day18 as day

test_data = day.parse("""2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5""")

def test_day18():
    assert day.phase1({(1,1,1),(2,1,1)}) == 10
    assert day.phase1(test_data) == 64
    assert day.phase2(test_data) == 58
