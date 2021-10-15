from src import day5

def test_phase1():
    assert day5.phase1('ugknbfddgicrmopn') is True
    assert day5.phase1('aaa') is True
    assert day5.phase1('jchzalrnumimnmhp') is False
    assert day5.phase1('haegwjzuvuyypxyu') is False
    assert day5.phase1('dvszwmarrgswjxmb') is False

def test_phase2():
    assert day5.phase2('qjhvhtzxzqqjkmpb') is True
    assert day5.phase2('xxyxx') is True
    assert day5.phase2('uurcxstgmygtbstg') is False
    assert day5.phase2('ieodomkazucvgmuy') is False
