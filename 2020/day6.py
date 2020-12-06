from pathlib import Path


def phase1(data):
    return sum([len(set(p.replace("\n",""))) for p in data])

def phase2(data):
    total = 0
    answers = [p.split("\n") for p in data]
    for g in answers:
        for char in g[0]:
            seen = 0
            for person in g:
                seen += 1 if char in person else 0
            if seen == len(g):
                total += 1
    return total

def load(data):
    return [p for p in data.split("\n\n")]

if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/day6").open() as f:
        answers = load(f.read())

        print('Phase 1: {}'.format(phase1(answers)))
        print('Phase 2: {}'.format(phase2(answers)))
