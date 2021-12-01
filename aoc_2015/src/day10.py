from pathlib import Path

def step(n):
    new_n, count, i = '', 1, 1
    n += 'z'
    while i < len(n):
        if n[i] == n[i-1]:
            count += 1
        else:
            new_n += str(count) + n[i-1]
            count = 1
        i += 1
    return new_n

def phase1(n):
    for i in range(0,40):
        n = step(n)
    n1 = n
    for i in range(0,10):
        n = step(n)
    return len(n1), len(n)


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("../input/day10").open(encoding="UTF-8") as f:
        NUMBER = f.read()

        print(f"Phase 1: {phase1(NUMBER)}")
