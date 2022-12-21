from aoc_2022 import day21 as day

test_data = day.parse("""root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32""")

def test_day21():
    assert day.phase1(test_data) == 152
    #assert day.phase2(test_data,10) == 58
