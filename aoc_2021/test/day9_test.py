from aoc_2021.src import day9 as day

test_data = day.parse("""2199943210
3987894921
9856789892
8767896789
9899965678""")

def test_day9():
    assert day.phase1(test_data) == 15
    assert day.phase2(test_data) == 1134
