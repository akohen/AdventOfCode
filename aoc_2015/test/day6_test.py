from aoc_2015.src import day6

def test_phase1():
    assert day6.phase1(day6.prep(['turn on 499,499 through 500,500'])) == 4
    assert day6.phase1(day6.prep(
        ['toggle 0,0 through 0,2', 'toggle 0,0 through 1,0']
    )) == 3


def test_phase2():
    assert day6.phase2(day6.prep(['toggle 0,0 through 999,999'])) == 2000000
