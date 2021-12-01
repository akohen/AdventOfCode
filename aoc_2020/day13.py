from pathlib import Path
import sys

# from https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6
from functools import reduce


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
 
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1



TEST_MODE = bool(len(sys.argv) > 1 and sys.argv[1] == "test")


def phase1(timestamp, schedule):
    for i in range(0,9999):
        for bus in schedule:
            if bus != 'x' and (timestamp+i) % int(bus) == 0:
                return int(bus) * i


def phase2(data):
    n = [int(b) for b in data if b != 'x']
    a = [int(b)-idx for idx,b in enumerate(data) if b != 'x']
    return chinese_remainder(n,a)

def load(data):
    timestamp, buses = data.split('\n')
    return int(timestamp), buses.split(',')

if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/day13_sample" if TEST_MODE else "input/day13").open() as f:
        TIMESTAMP, SCHEDULE = load(f.read())

        print(f'Phase 1: {phase1(TIMESTAMP, SCHEDULE)}')
        print(f'Phase 2: {phase2(SCHEDULE)}')