from pathlib import Path
import sys
import re


TEST_MODE = bool(len(sys.argv) > 1 and sys.argv[1] == "test")


def phase1(data):
    memory = {}
    for line in data:
        if line[1] == "a":
            mask = line[7:]
        else:
            matches = re.match(r"^mem\[(\d+)\] = (\d+)$",line)
            address, value, result = int(matches.group(1)), int(matches.group(2)), 0
            for i in range(35,-1,-1):
                if mask[i] == 'X':
                    result += (value % 2) << (35-i)
                else:
                    result += int(mask[i]) << (35-i)
                value = value >> 1
            memory[address] = result
    total = 0
    for address in memory:
        total += memory[address]
    return total


def phase2(data):
    memory = {}
    for line in data:
        if line[1] == "a":
            mask = line[7:]
        else:
            matches = re.match(r"^mem\[(\d+)\] = (\d+)$",line)
            address, value, result = int(matches.group(1)), int(matches.group(2)), [0]*36
            for i in range(35,-1,-1):
                if mask[i] == 'X':
                    result[i] = 'X'
                else:
                    result[i] = str((address % 2) | int(mask[i]))
                address = address >> 1

            addresses = [[]]
            start = 0
            for idx, bit in enumerate(result):
                if bit == 'X':
                    addresses = [i+result[start:idx]+new_add for i in addresses for new_add in (['0'],['1'])]
                    start = idx+1
                elif idx == 35:
                    addresses = [i+result[start:idx+1] for i in addresses]
            for a in addresses:
                memory[int(''.join(a),2)] = value

    total = 0
    for address in memory:
        total += memory[address]
    return total

def load(data):
    return data

if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/day14_sample" if TEST_MODE else "input/day14").open() as f:
        DATA = [line.strip() for line in f]

        print('Phase 1: {}'.format(phase1(DATA)))
        print('Phase 2: {}'.format(phase2(DATA)))