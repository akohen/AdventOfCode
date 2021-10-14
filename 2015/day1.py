from pathlib import Path

def phase1(value):
    return value.count('(') - value.count(')')

def phase2(value):
    floor = 0
    for i, char in enumerate(value):
        floor += 1 if char == '(' else -1
        if floor == -1:
            return i+1
    return None

if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/day1").open(encoding="UTF-8") as f:
        values = f.read()

        print(f"Phase 1: {phase1(values)}")
        print(f"Phase 2: {phase2(values)}")
