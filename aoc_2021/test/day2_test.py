from aoc_2021.src import day2 as day

test_data = day.parse("""forward 5
down 5
forward 8
up 3
down 8
forward 2""".splitlines())

def test_phase1():
    assert day.phase1(test_data) == 150

def test_phase2():
    assert day.phase2(test_data) == 900
