from src import day7

INSTRUCTIONS = day7.parse("""123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i""".splitlines())

def test_phase1():
    assert day7.phase1(INSTRUCTIONS,'d') == 72
    assert day7.phase1(INSTRUCTIONS,'g') == 114
