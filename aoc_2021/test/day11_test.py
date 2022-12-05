from copy import deepcopy
from aoc_2021.src import day11 as day

test_data = day.parse("""5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526""")

def test_day10():
    assert day.phase1(deepcopy(test_data)) == 1656
    assert day.phase1(test_data, 500) == 195
