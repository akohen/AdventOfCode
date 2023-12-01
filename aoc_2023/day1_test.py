from aoc_2023 import day1 as day

test_data = day.parse("""1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet""")


test_data2 = day.parse2("""two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen""")

def test_day21():
    assert day.phase1(test_data) == 142
    assert day.phase1(test_data2) == 281
