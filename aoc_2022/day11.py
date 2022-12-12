from pathlib import Path
from copy import deepcopy
from operator import mul, add
from math import prod

def phase1(data, rounds = 20):
    for _ in range(rounds):
        for monkey in data:
            for _ in range(len(monkey['items'])):
                item = monkey['items'].pop()
                monkey['count'] += 1
                var = item if monkey['value'] == 'old' else monkey['value']
                new_value = monkey['operation'](item, var)//3
                if new_value % monkey['test'] == 0:
                    data[monkey['true']]['items'].append(new_value)
                else:
                    data[monkey['false']]['items'].append(new_value)
    return mul(*sorted([monkey['count'] for monkey in data])[-2:])


def phase2(data, rounds = 10000):
    div = prod([monkey['test'] for monkey in data])
    for _ in range(rounds):
        for monkey in data:
            for _ in range(len(monkey['items'])):
                item = monkey['items'].pop()
                monkey['count'] += 1
                var = item if monkey['value'] == 'old' else monkey['value']
                new_value = monkey['operation'](item, var)%div
                if new_value % monkey['test'] == 0:
                    data[monkey['true']]['items'].append(new_value)
                else:
                    data[monkey['false']]['items'].append(new_value)
    return mul(*sorted([monkey['count'] for monkey in data])[-2:])


def parse(file):
    monkeys = []
    for monkey in file.split('\n\n'):
        lines = monkey.split('\n')
        monkeys.append({
            'items': [int(x) for x in lines[1][18:].split(', ')],
            'operation': mul if lines[2][23] == '*' else add,
            'value': lines[2][25:] if lines[2][25:] == 'old' else int(lines[2][25:]),
            'test': int(lines[3][21:]),
            'true': int(lines[4][29:]),
            'false': int(lines[5][30:]),
            'count': 0
        })
    return monkeys


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/"+Path(__file__).stem).open(encoding="UTF-8") as f:
        DATA = parse(f.read())

        print(f"Phase 1: {phase1(deepcopy(DATA))}")
        print(f"Phase 2: {phase2(DATA)}")
