from pathlib import Path
import sys

TEST_MODE = bool(len(sys.argv) > 1 and sys.argv[1] == "test")

def phase1(v):
    return next(v[i]*v[j] for i in range(len(v)) for j in range(i,len(v)) if v[i]+v[j] == 2020)

def phase2(v):
    return next(v[i]*v[j]*v[k] for i in range(len(v)) for j in range(i,len(v)) for k in range(j,len(v)) if v[i]+v[j]+v[k] == 2020)

if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/day1_sample" if TEST_MODE else "input/day1").open() as f:
        values = [int(i) for i in f]

        print(f'Phase 1: {phase1(values)}')
        print(f'Phase 1: {phase2(values)}')
