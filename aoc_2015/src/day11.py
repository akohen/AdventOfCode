from pathlib import Path
from string import ascii_lowercase

FORBIDDEN_CHARS = ['i','o','l']
TRIGRAMS = [ascii_lowercase[i:i+3] for i in range(0,24)]
PAIRS =[ascii_lowercase[i]*2 for i in range(0,26)]

def is_valid(password):
    if any([t in password for t in FORBIDDEN_CHARS]):
        return False
    
    if not any([t in password for t in TRIGRAMS]):
        return False

    if 2 > sum([t in password for t in PAIRS]):
        return False

    return True


def next_password(password):
    if password[-1] == 'z':
        return next_password(password[:-1]) + 'a'
    return password[:-1] + chr(ord(password[-1])+1)


def phase1(password):
    while not is_valid(password):
        password = next_password(password)
    return password


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("../input/day11").open(encoding="UTF-8") as f:
        PASSWORD = f.read()

        print(f"Phase 1: {phase1(PASSWORD)}")
        print(f"Phase 2: {phase1(next_password(phase1(PASSWORD)))}")
