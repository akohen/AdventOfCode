from aoc_2021.src import day12 as day

test_data1 = day.parse("""start-A
start-b
A-c
A-b
b-d
A-end
b-end""")

test_data2 = day.parse("""dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc""")

test_data3 = day.parse("""fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW""")


def test_day10():
    assert day.phase1(test_data1) == 10
    assert day.phase1(test_data2) == 19
    assert day.phase1(test_data3) == 226

    assert day.phase2(test_data1) == 36
    assert day.phase2(test_data2) == 103
    assert day.phase2(test_data3) == 3509
