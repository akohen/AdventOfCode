from aoc_2022 import day7 as day

test_data = day.parse("""$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k""")

def test_day7():
    assert day.phase1(test_data) == 95437
    assert day.phase2(test_data) == 24933642
