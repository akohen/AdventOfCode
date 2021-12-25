from aoc_2021.src import day3 as day

test_data = day.parse("""00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010""")

def test_phase1():
    assert day.phase1(test_data) == 198

def test_phase2():
    assert day.phase2(test_data) == 230
