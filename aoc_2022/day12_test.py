from aoc_2022 import day12 as day
from copy import deepcopy

test_data = day.parse("""Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi""")

def test_day12():
    assert day.phase1(deepcopy(test_data)) == 31
    assert day.phase2(test_data) == 29
