from aoc_2015.src import day1

def test_phase1():
    assert day1.phase1('()()') == 0
    assert day1.phase1('))(((((') == 3
    assert day1.phase1(')))') == -3
    assert day1.phase1(')())())') == -3

def test_phase2():
    assert day1.phase2(')') == 1
    assert day1.phase2('()())') == 5
