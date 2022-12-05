from aoc_2022 import day5 as day
from copy import deepcopy

test_data = day.parse("""    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2""")

def test_phase1():
    assert day.phase1(*deepcopy(test_data)) == 'CMZ'

def test_phase2():
    assert day.phase2(*test_data) == 'MCD'
