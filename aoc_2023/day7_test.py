from aoc_2023 import day7

test_data = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""


def test_day7():
    assert day7.part1(day7.parse(test_data)) == 6440
    assert day7.part2(day7.parse2(test_data)) == 5905
