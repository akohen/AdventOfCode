from src import day3

def test_phase1():
    assert day3.phase1('>') == 2
    assert day3.phase1('^>v<') == 4
    assert day3.phase1('^v^v^v^v^v') == 2

def test_phase2():
    assert day3.phase2('^v') == 3
    assert day3.phase2('^>v<') == 3
    assert day3.phase2('^v^v^v^v^v') == 11
