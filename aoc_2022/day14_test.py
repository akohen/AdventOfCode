from aoc_2022 import day14 as day

test_data = day.parse("""498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9""")

def test_day14():
    assert day.phase1(test_data) == 24
    assert day.phase2(test_data) == 93
