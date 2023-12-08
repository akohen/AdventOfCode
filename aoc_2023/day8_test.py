from aoc_2023 import day8

test_data = day8.parse("""RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)""")
                       
test_data2 = day8.parse("""LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)""")
                       
test_data3 = day8.parse("""LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)""")


def test_day8():
    assert day8.part1(*test_data) == 2
    assert day8.part1(*test_data2) == 6
    assert day8.part2(*test_data3) == 6
