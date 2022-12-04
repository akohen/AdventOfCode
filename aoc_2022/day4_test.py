from aoc_2022 import day4 as day

test_data = day.parse("""2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8""")

def test_phase1():
    assert day.phase1(test_data) == 2

def test_phase2():
    assert day.phase2(test_data) == 4
