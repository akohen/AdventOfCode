from pathlib import Path
from math import lcm

def part1(instr, network):
    curr, step = 'AAA', 0
    while curr != 'ZZZ':
        curr = network[curr][0 if instr[step%len(instr)] == 'L' else 1]
        step += 1
    return step


def part2(instr, network):
    curr = [node for node in network.keys() if node[-1] == 'A']
    step = [0] * len(curr)
    for i in range(len(curr)):
        while curr[i][-1] != 'Z':
            curr[i] = network[curr[i]][0 if instr[step[i]%len(instr)] == 'L' else 1]
            step[i] += 1
    return lcm(*step)


def parse(file):
    blocs = file.split('\n\n')
    return blocs[0], {line[:3]: (line[7:10], line[12:-1]) for line in blocs[1].split('\n')}


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/"+Path(__file__).stem).open(encoding="UTF-8") as f:
        DATA = parse(f.read())

        print(f"Phase 1: {part1(*DATA)}")
        print(f"Phase 2: {part2(*DATA)}")
