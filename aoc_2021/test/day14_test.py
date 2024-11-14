from aoc_2021.src import day14

test_data = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""


def test_day14():
    parsed_data = day14.parse(test_data)
    assert day14.part1(*parsed_data) == 1588
    assert day14.part2(*parsed_data) == 2188189693529
