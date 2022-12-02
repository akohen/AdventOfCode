from aoc_2022 import day2 as day

test_data = day.parse("""A Y
B X
C Z""")

def test_phase1():
    assert day.phase1(test_data) == 15

def test_phase2():
    assert day.phase2(test_data) == 12
