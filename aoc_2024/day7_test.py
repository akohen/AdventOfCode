from aoc_2024 import day7

test_data = day7.parse("""190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20""")


def test_day7():
    assert day7.part1(test_data) == 3749
    assert day7.part2(test_data) == 11387
