from pathlib import Path

ENDINGS = {'(': ')', '[': ']', '{': '}', '<': '>'}

def phase1(lines):
    values = {')': 3, ']': 57, '}': 1197, '>': 25137}
    score = 0
    for line in lines:
        chunks = []
        for c in line:
            if c in ENDINGS:
                chunks.append(c)
            elif ENDINGS[chunks[-1]] == c:
                chunks.pop()
            else:
                score += values[c]
                break 
    return score

def phase2(lines):
    values = {'(': 1, '[': 2, '{': 3, '<': 4}
    scores = []
    for line in lines:
        chunks = []
        for c in line:
            if c in ENDINGS:
                chunks.append(c)
            elif ENDINGS[chunks[-1]] == c:
                chunks.pop()
            else:
                chunks = []
                break
        score = 0
        for c in reversed(chunks):
            score *= 5
            score += values[c]
        if score > 0:
            scores.append(score)
    return sorted(scores)[(len(scores)-1)//2]


def parse(file):
    return file.split('\n')

if __name__ == "__main__":
    with Path(__file__).parent.joinpath("../input/"+Path(__file__).stem).open(encoding="UTF-8") as f:
        DATA = parse(f.read())

        print(f"Phase 1: {phase1(DATA)}")
        print(f"Phase 2: {phase2(DATA)}")
