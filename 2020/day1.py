from pathlib import Path
import sys

test_mode = True if len(sys.argv) > 1 and sys.argv[1] == "test" else False

def phase1(v):
    return next(v[i]*v[j] for i in range(len(v)) for j in range(i,len(v)) if v[i]+v[j] == 2020)

def phase2(v):
    return next(v[i]*v[j]*v[k] for i in range(len(v)) for j in range(i,len(v)) for k in range(j,len(v)) if v[i]+v[j]+v[k] == 2020)

if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/day1_sample" if test_mode else "input/day1").open() as f:
        values = [int(i) for i in f]
        
        print('Phase 1: {}'.format(phase1(values)))
        print('Phase 2: {}'.format(phase2(values)))