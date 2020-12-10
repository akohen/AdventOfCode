from pathlib import Path
from collections import defaultdict
import sys

TEST_MODE = bool(len(sys.argv) > 1 and sys.argv[1] == "test")

def phase1(adapters):
    step_1, step_3, prev = 0, 0, 0
    for val in adapters:
        if val - prev == 1:
            step_1 += 1
        elif val - prev == 3:
            step_3 += 1
        prev = val
    return step_1 * step_3

def phase2(adapters):
    arrangements = defaultdict(int)
    arrangements[0] = 1
    for val in adapters[1:]: 
        arrangements[val] = arrangements[val-3] + arrangements[val-2] + arrangements[val-1]
    return arrangements[adapters[-1]]

if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/day10_sample" if TEST_MODE else "input/day10").open() as f:
        ADAPTERS = sorted([0] + [int(line) for line in f])
        ADAPTERS.append(ADAPTERS[-1] + 3)
        
        print('Phase 1: {}'.format(phase1(ADAPTERS)))
        print('Phase 2: {}'.format(phase2(ADAPTERS)))