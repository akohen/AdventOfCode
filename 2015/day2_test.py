import day2

def test_phase1():
    assert day2.phase1(['2x3x4']) == 58
    assert day2.phase1(['1x1x10']) == 43

def test_phase2():
    assert day2.phase2(['2x3x4']) == 34
    assert day2.phase2(['1x1x10']) == 14
