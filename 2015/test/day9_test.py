from src import day9

INSTRUCTIONS = day9.parse("""London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141""")

def test_phase1():
    assert day9.phase1(INSTRUCTIONS) == 605

def test_phase2():
    assert day9.phase2(INSTRUCTIONS) == 982
