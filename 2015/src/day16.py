from pathlib import Path
from operator import eq, gt, lt


def phase1(aunts, tape):
    for n, aunt in enumerate(aunts,1):
        for item, qty in tape.items():
            if item in aunt and aunt[item] != qty[0]:
                break
        else:
            return n


def phase2(aunts, tape):
    for n, aunt in enumerate(aunts,1):
        for item, qty in tape.items():
            if item in aunt and not qty[1](aunt[item], qty[0]):
                break
        else:
            return n


def parse(f):
    return [
        {a[2]: int(a[3]), a[4]: int(a[5]), a[6]: int(a[7])}
        for a in [line.replace(':','').replace(',','').split() for line in f]
    ]


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("../input/day16").open(encoding="UTF-8") as f:
        AUNTS = parse(f)
        TAPE = {
            'children': (3, eq),
            'cats': (7, gt),
            'samoyeds': (2, eq),
            'pomeranians': (3, lt),
            'akitas': (0, eq),
            'vizslas': (0, eq),
            'goldfish': (5, lt),
            'trees': (3, gt),
            'cars': (2, eq),
            'perfumes': (1, eq)
        }

        print(f"Phase 1: {phase1(AUNTS, TAPE)}")
        print(f"Phase 2: {phase2(AUNTS, TAPE)}")
