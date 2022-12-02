from pathlib import Path

shapes = ['A', 'B', 'C']
responses = ['X', 'Y', 'Z']

def phase1(guide):
    score = 0
    for line in guide:
        p1 = shapes.index(line[0])
        p2 = responses.index(line[1])
        score += p2 + 1 + ((p2-p1 + 1)%3) * 3
    return score


def phase2(guide):
    score = 0
    for line in guide:
        p1 = shapes.index(line[0])
        p2 = responses.index(line[1])
        score += 1 + 3*p2 + (p1+p2-1)%3
    return score


def parse(file):
    return [line.split(' ') for line in file.split('\n')]


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/"+Path(__file__).stem).open(encoding="UTF-8") as f:
        GUIDE = parse(f.read())

        print(f"Phase 1: {phase1(GUIDE)}")
        print(f"Phase 2: {phase2(GUIDE)}")
