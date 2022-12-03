from aoc_2022 import day3 as day

test_data = day.parse("""vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw""")

def test_phase1():
    assert day.phase1(test_data) == 157

def test_phase2():
    assert day.phase2(test_data) == 12
