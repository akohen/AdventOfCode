from aoc_2022 import day8 as day

test_data = day.parse("""30373
25512
65332
33549
35390""")

def test_day8():
    assert day.phase1(test_data) == 21
    assert day.phase2(test_data) == 8
