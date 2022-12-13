from aoc_2022 import day13 as day
from copy import deepcopy

test_data = day.parse("""[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]""")

def test_day13():
    assert day.phase1(test_data) == 13
    assert day.phase2(test_data) == 140
