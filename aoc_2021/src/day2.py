from pathlib import Path

def phase1(commands):
    horizontal, depth = 0, 0
    for command in commands:
        if command[0] == 'down':
            depth = depth + command[1]
        if command[0] == 'up':
            depth = depth - command[1]
        if command[0] == 'forward':
            horizontal = horizontal + command[1]
    return horizontal * depth

def phase2(commands):
    horizontal, depth, aim = 0, 0, 0
    for command in commands:
        if command[0] == 'down':
            aim = aim + command[1]
        if command[0] == 'up':
            aim = aim - command[1]
        if command[0] == 'forward':
            horizontal = horizontal + command[1]
            depth = depth + ( command[1] * aim )
    return horizontal * depth

def parse(file):
    return [(s[0],int(s[1])) for line in file if (s := line.split(' '))]

if __name__ == "__main__":
    with Path(__file__).parent.joinpath("../input/day2").open(encoding="UTF-8") as f:
        VALUES = parse(f)

        print(f"Phase 1: {phase1(VALUES)}")
        print(f"Phase 2: {phase2(VALUES)}")
