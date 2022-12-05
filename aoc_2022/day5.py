import copy
from pathlib import Path

def phase1(crates, instructions):
    for instr in instructions:
        crates[instr[2]] += list(reversed(crates[instr[1]][-instr[0]:]))
        crates[instr[1]] = crates[instr[1]][:-instr[0]]
    return ''.join(c.pop() for c in crates)


def phase2(crates, instructions):
    for instr in instructions:
        crates[instr[2]] += crates[instr[1]][-instr[0]:]
        crates[instr[1]] = crates[instr[1]][:-instr[0]]
    return ''.join(c.pop() for c in crates)


def parse(file):
    crates_data, instructions_data = file.split('\n\n')
    crates = [[] for i in range(int(crates_data[-2]))]
    for line in reversed(crates_data.split('\n')[:-1]):
        for i in range(int(crates_data[-2])):
            if line[i*4+1] != ' ':
                crates[i].append(line[i*4+1])
    instructions = [[int(x[1]),int(x[3])-1,int(x[5])-1] for line in instructions_data.split('\n') if (x := line.split(' '))]
    return crates, instructions


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/"+Path(__file__).stem).open(encoding="UTF-8") as f:
        CRATES, INSTR = parse(f.read())

        print(f"Phase 1: {phase1(copy.deepcopy(CRATES), INSTR)}")
        print(f"Phase 2: {phase2(CRATES, INSTR)}")
