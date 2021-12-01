from pathlib import Path

def phase1(values):
    total, prev = 0, values[0]
    for curr in values:
        if curr > prev:
            total = total +1
        prev = curr
    return total

def phase2(values):
    return phase1([values[i] + values[i+1] + values[i+2] for i in range(0,len(values)-2)])

if __name__ == "__main__":
    with Path(__file__).parent.joinpath("../input/day1").open(encoding="UTF-8") as f:
        VALUES = [int(i) for i in f]

        print(f"Phase 1: {phase1(VALUES)}")
        print(f"Phase 2: {phase2(VALUES)}")
