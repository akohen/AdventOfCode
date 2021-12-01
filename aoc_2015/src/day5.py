from pathlib import Path
from string import ascii_lowercase


VOWELS = 'aeiou'
DISALLOWED = ['ab','cd','pq','xy']

def phase1(string:str):
    for sub in DISALLOWED:
        if sub in string:
            return False
    if sum([string.count(i) for i in VOWELS]) < 3:
        return False
    for letter in ascii_lowercase:
        if letter+letter in string:
            return True
    return False


def phase2(string:str):
    pair, repeat, i = False, False, 0
    for i in range(0,len(string)-2):
        if string[i+2] == string[i]:
            repeat = True
        for k in range(i+2,len(string)):
            if string[i:i+2] == string[k:k+2]:
                pair = True
    return pair & repeat


if __name__ == "__main__":
    with Path(__file__).parent.parent.joinpath("input/day5").open(encoding="UTF-8") as f:
        STRINGS = f.read().splitlines()

        print(f"Phase 1: {sum([phase1(x) for x in STRINGS])}")
        print(f"Phase 2: {sum([phase2(x) for x in STRINGS])}")
