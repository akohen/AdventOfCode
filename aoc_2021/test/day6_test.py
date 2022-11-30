from aoc_2021.src import day6 as day

test_data = day.parse("""3,4,3,1,2""")

def test_phase1():
    assert day.phase1(test_data.copy(), 18) == 26

def test_phase2():
    assert day.phase1(test_data, 256) == 26984457539
