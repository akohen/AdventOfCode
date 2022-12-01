from aoc_2022 import day1 as day

test_data = day.parse("""1000
2000
3000

4000

5000
6000

7000
8000
9000

10000""")

def test_phase1():
    assert day.phase1(test_data) == 24000

def test_phase2():
    assert day.phase2(test_data) == 45000
