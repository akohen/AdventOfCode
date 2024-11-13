from aoc_2021.src import day7 as day

test_data = day.parse('16,1,2,0,4,2,7,1,2,14')

def test_phase1():
    assert day.phase1(test_data) == 37

def test_phase2():
    assert day.phase2(test_data) == 168
