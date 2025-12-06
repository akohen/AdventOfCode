from aoc_2025 import day6

test_data = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """


def test_day6():
    assert day6.part1(day6.parse(test_data)) == 4277556
    assert day6.part2(test_data) == 3263827
