from pathlib import Path
import sys

test_mode = True if len(sys.argv) > 1 and sys.argv[1] == "test" else False

def phase1(forest, right=3, down=1):
    curr, total = 0, 0
    for i in range(0,len(forest), down):
        if forest[i][curr] == "#":
            total += 1
        curr = (curr + right) % len(forest[i])
    return total


def phase2(forest):
    return phase1(forest, 1,1)*phase1(forest, 3,1)*phase1(forest, 5,1)*phase1(forest, 7,1)*phase1(forest, 1,2)

if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/day3_sample" if test_mode else "input/day3").open() as f:
        forest = [line.rstrip("\n") for line in f]
        
        print('Phase 1: {}'.format(phase1(forest)))
        print('Phase 2: {}'.format(phase2(forest)))