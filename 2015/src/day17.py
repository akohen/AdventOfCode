from pathlib import Path
from itertools import chain, combinations


def phase1(containers, eggnog):
    total = 0
    for combination in chain.from_iterable(combinations(containers, r) for r in range(len(containers)+1)):
        if sum(combination) == eggnog:
            total += 1
    return total


def phase2(containers, eggnog):
    for r in range(1, len(containers)):
        total = 0
        for combination in combinations(containers, r):
            if sum(combination) == eggnog:
                total += 1
        if total != 0:
            return total


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("../input/day17").open(encoding="UTF-8") as f:
        CONTAINERS = [int(x) for x in f]
        EGGNOG = 150

        print(f"Phase 1: {phase1(CONTAINERS, EGGNOG)}")
        print(f"Phase 2: {phase2(CONTAINERS, EGGNOG)}")
