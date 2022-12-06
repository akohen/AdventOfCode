from aoc_2022 import day6 as day

test_data = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"

def test_day6():
    assert day.phase1(test_data, 4) == 7
    assert day.phase1(test_data, 14) == 19
