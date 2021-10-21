from src import day14

INSTRUCTIONS = day14.parse("""Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.""".splitlines())

def test_phase1():
    assert day14.phase1(INSTRUCTIONS, 1000) == 1120
    assert day14.phase2(INSTRUCTIONS, 1000) == 689
