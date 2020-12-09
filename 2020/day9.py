from pathlib import Path
import sys

TEST_MODE = bool(len(sys.argv) > 1 and sys.argv[1] == "test")

def phase1(data, preamble):
    for idx, num in enumerate(data[preamble:]):
        found = False
        for i in range(preamble-1):
            for j in range(i+1, preamble):
                if num == data[idx+i] + data[idx+j]:
                    found = True
        if not found:
            return num

def phase2(data, target):
    for i, num in enumerate(data):
        total, j = num, i
        while total < target:
            j += 1
            total += data[j]
        if total == target:
            return min(data[i:j]) + max(data[i:j])

if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/day9_sample" if TEST_MODE else "input/day9").open() as f:
        INPUT = [int(line) for line in f]
        PREAMBLE = 5 if TEST_MODE else 25

        print('Phase 1: {}'.format(phase1(INPUT, PREAMBLE)))
        print('Phase 2: {}'.format(phase2(INPUT, phase1(INPUT, PREAMBLE))))
