from aoc_2023 import day15

test_data = day15.parse("rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7")


def test_day15():
    assert day15.part1(test_data) == 1320
    assert day15.part2(test_data) == 145
