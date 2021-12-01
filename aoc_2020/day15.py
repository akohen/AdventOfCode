from pathlib import Path
import sys


TEST_MODE = bool(len(sys.argv) > 1 and sys.argv[1] == "test")

def play(data, rounds):
    memory, num = {}, 0
    for i,v in enumerate(data):
        memory[v] = i+1
    for i in range(len(data)+1,rounds):
        if num not in memory:
            memory[num] = i
            num = 0
        else:
            next_num = i - memory[num]
            memory[num] = i
            num = next_num
    return num


def phase1(data):
    return play(data, 2020)

def phase2(data):
    return play(data, 30000000)

def load(data):
    return [int(i) for i in data.split(',')]

if __name__ == "__main__":
    DATA = load("0,3,6" if TEST_MODE else "0,5,4,1,10,14,7")

    print(f'Phase 1: {phase1(DATA)}')
    print(f'Phase 2: {phase2(DATA)}')