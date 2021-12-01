from pathlib import Path
import sys

TEST_MODE = bool(len(sys.argv) > 1 and sys.argv[1] == "test")

def phase1(data):
    return execute(data)[1]

def execute(program):
    ptr, acc, seen = 0, 0, [len(program)]
    while ptr not in seen:
        seen.append(ptr)
        if program[ptr][0] == "nop":
            ptr += 1
        elif program[ptr][0] == "acc":
            acc += program[ptr][1]
            ptr += 1
        else:
            ptr += program[ptr][1]
    return ptr == len(program), acc, program

def phase2(data):
    for i in range(len(data)):
        if data[i][0] == "nop":
            program = data.copy()
            program[i] = ("jmp", data[i][1])
            result = execute(program)
            if result[0]:
                return result[1]
        elif data[i][0] == "jmp":
            program = data.copy()
            program[i] = ("nop", data[i][1])
            result = execute(program)
            if result[0]:
                return result[1]
    return False

if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/day8_sample" if TEST_MODE else "input/day8").open() as f:
        game_code = [(instr[0], int(instr[1])) for line in f if (instr := line.rstrip("\n").split(" "))]
        
        print(f'Phase 1: {phase1(game_code)}')
        print(f'Phase 2: {phase2(game_code)}')