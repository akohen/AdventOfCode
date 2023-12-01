from pathlib import Path
import string


def phase1(data):
    return sum([10 * line[0] + line[-1] for line in data])

NUMS = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'] \
    + list(string.digits)


def parse2(file):
    return [
        [
            n%10 
            for i in range(len(line)) 
            for n, digit in enumerate(NUMS) 
            if digit == line[i:i+len(digit)]
        ]
        for line in file.split('\n')
    ]



def parse(file):
    return [[int(x) for x in line if str.isdigit(x)] for line in file.split('\n')]


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/"+Path(__file__).stem).open(encoding="UTF-8") as f:
        DATA = f.read()

        print(f"Phase 1: {phase1(parse(DATA))}")
        print(f"Phase 2: {phase1(parse2(DATA))}")
