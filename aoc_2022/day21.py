from pathlib import Path


def eval_node(node, data):
    if isinstance(data[node], int):
        return data[node]
    return eval( str(eval_node(data[node][0], data)) + data[node][1] + str(eval_node(data[node][2], data)))

def phase1(data):
    return int(eval_node('root', data))


def phase2(data, step=100000000000):
    tgt, last = eval_node(data['root'][2], data), 0
    while (diff := eval_node(data['root'][0], data) - tgt) != 0:
        if diff > 0:
            last = data['humn']
            data['humn'] += step
        else:
            step = step // 10
            data['humn'] = last
    return data['humn']



def parse(file):
    monkeys = {}
    for line in file.split('\n'):
        args = line[6:].split(' ')
        monkeys[line[:4]] = int(args[0]) if len(args) == 1 else args
    return monkeys


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/"+Path(__file__).stem).open(encoding="UTF-8") as f:
        DATA = parse(f.read())

        print(f"Phase 1: {phase1(DATA)}")
        print(f"Phase 2: {phase2(DATA)}")
