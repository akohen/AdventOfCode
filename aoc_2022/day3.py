from pathlib import Path
import string

def phase1(rucksacks):
    score = 0
    for sack in rucksacks:
        intersection = set(sack[:len(sack)//2]).intersection(set(sack[len(sack)//2:]))
        for item in intersection:
            score += list(string.ascii_letters).index(item) +1
    return score


def phase2(rucksacks):
    score = 0
    for i in range(len(rucksacks)//3):
        intersection = set(rucksacks[3*i]).intersection(set(rucksacks[3*i+1])).intersection(set(rucksacks[3*i+2]))
        for item in intersection:
            score += list(string.ascii_letters).index(item) +1
    return score


def parse(file):
    return file.split('\n')


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/"+Path(__file__).stem).open(encoding="UTF-8") as f:
        DATA = parse(f.read())

        print(f"Phase 1: {phase1(DATA)}")
        print(f"Phase 2: {phase2(DATA)}")
