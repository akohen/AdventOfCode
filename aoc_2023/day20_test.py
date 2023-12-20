from aoc_2023 import day20

test_data = day20.parse("""broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a""")

test_data2 = day20.parse("""broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output""")


def test_day20():
    assert day20.part1(test_data) == 32000000
    assert day20.part1(test_data2) == 11687500
