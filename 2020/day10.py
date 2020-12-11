from pathlib import Path
from collections import defaultdict
import sys

TEST_MODE = bool(len(sys.argv) > 1 and sys.argv[1] == "test")

def phase1(adapters):
    steps = [adapters[i+1]-adapters[i] for i in range(len(adapters)-1)]
    permutations, total = [1,1,2,4,7,13], 1
    adjacent_ones = [steps.index(3, idx)-idx for idx, val in enumerate([3]+steps) if val == 3 and idx < len(steps)]
    for v in adjacent_ones: total *= permutations[v]
    return steps.count(1) * steps.count(3), total

if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/day10_sample" if TEST_MODE else "input/day10").open() as f:
        ADAPTERS = sorted([0] + [int(line) for line in f])
        ADAPTERS.append(ADAPTERS[-1] + 3)

        print('Phase 1: {}\nPhase 2: {}'.format(*phase1(ADAPTERS)))