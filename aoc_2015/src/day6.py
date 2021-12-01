from pathlib import Path

def phase1(instructions):
    lights = [[False]*1000 for i in range(1000)]
    for instr in instructions:
        action = instr[0]
        p_1 = [int(x) for x in instr[1].split(',')]
        p_2 = [int(x) for x in instr[3].split(',')]
        for i in range(p_1[0], p_2[0]+1):
            for j in range(p_1[1], p_2[1]+1):
                if action == 'on':
                    lights[i][j] = True
                elif action == 'off':
                    lights[i][j] = False
                else:
                    lights[i][j] = not lights[i][j]
    return sum([sum(l) for l in lights])

def phase2(instructions):
    lights = [[0]*1000 for i in range(1000)]
    for instr in instructions:
        action = instr[0]
        p_1 = [int(x) for x in instr[1].split(',')]
        p_2 = [int(x) for x in instr[3].split(',')]
        for i in range(p_1[0], p_2[0]+1):
            for j in range(p_1[1], p_2[1]+1):
                if action == 'on':
                    lights[i][j] = lights[i][j] + 1
                elif action == 'off':
                    lights[i][j] = max(0,lights[i][j]-1)
                else:
                    lights[i][j] = lights[i][j] + 2
    return sum([sum(l) for l in lights])

def prep(file):
    return [line.lstrip('turn ').rstrip().split(' ') for line in file]

if __name__ == "__main__":
    with Path(__file__).parent.joinpath("../input/day6").open(encoding="UTF-8") as f:
        INSTRUCTIONS = prep(f)

        print(f"Phase 1: {phase1(INSTRUCTIONS)}")
        print(f"Phase 2: {phase2(INSTRUCTIONS)}")
