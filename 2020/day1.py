from pathlib import Path
import sys

test_mode = True if len(sys.argv) > 1 and sys.argv[1] == "test" else False

def phase1(values):
    for i in range(len(values)):
        for j in range(i,len(values)):
            if values[i] + values[j] == 2020:
                return values[i] * values[j]

def phase2(values):
    for i in range(len(values)):
        for j in range(i,len(values)):
            for k in range(j,len(values)):
                if values[i] + values[j] + values[k] == 2020:
                    return values[i] * values[j] * values[k]

if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/day1_sample" if test_mode else "input/day1").open() as f:
        values = [int(i) for i in f]

        print('Phase 1: {}'.format(phase1(values)))
        print('Phase 2: {}'.format(phase2(values)))