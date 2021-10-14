from pathlib import Path

def phase1(values):
    total = 0
    for value in values:
        [l,w,h] = [int(x) for x in value.split('x')]
        total += 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)
    return total

def phase2(values):
    total = 0
    for value in values:
        [l,w,h] = [int(x) for x in value.split('x')]
        total += l*w*h + 2*min(l+w, w+h, h+l)
    return total

if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/day2").open(encoding="UTF-8") as f:
        values = f.read().splitlines()

        print(f"Phase 1: {phase1(values)}")
        print(f"Phase 2: {phase2(values)}")
