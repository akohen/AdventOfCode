from aoc_2024 import day17

test_data = day17.parse("""Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0""")


def test_day17():
    assert day17.part1(*test_data) == '4,6,3,5,6,3,5,2,1,0'