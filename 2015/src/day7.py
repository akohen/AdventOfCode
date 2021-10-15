from pathlib import Path


def phase1(wires, out='a'):
    return interpret(wires, wires[out])


def phase2(wires, value):
    wires['b'][0]['value'] = value
    return interpret(wires, wires['a'])


def interpret(wires, expr):
    if len(expr) == 1 & (expr[0]['type'] == 'int'):
        return expr[0]['value']
    if len(expr) == 1 & (expr[0]['type'] == 'wire'):
        val = interpret(wires, wires[expr[0]['value']])
        wires[expr[0]['value']] = [{ 'type':'int', 'value':val }]
        return val
    if expr[0]['value'] == 'NOT':
        return 65535 - interpret(wires, [expr[1]])
    if expr[1]['value'] == 'AND':
        return interpret(wires, [expr[0]]) & interpret(wires, [expr[2]])
    if expr[1]['value'] == 'OR':
        return interpret(wires, [expr[0]]) | interpret(wires, [expr[2]])
    if expr[1]['value'] == 'LSHIFT':
        return interpret(wires, [expr[0]]) << interpret(wires, [expr[2]])
    if expr[1]['value'] == 'RSHIFT':
        return interpret(wires, [expr[0]]) >> interpret(wires, [expr[2]])
    raise ValueError('Unknown expression')


def parse(file):
    def lexer(token):
        if token.isnumeric():
            return { 'type':'int', 'value':int(token) }
        if token in ['AND', 'OR', 'NOT', 'LSHIFT', 'RSHIFT']:
            return { 'type':'op', 'value':token}
        return {'type':'wire', 'value':token}

    labels = {}
    for line in [l.rstrip().split(' ') for l in file]:
        labels[line[-1]] = [lexer(x) for x in line[:-2]]
    return labels


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("../input/day7").open(encoding="UTF-8") as f:
        INSTRUCTIONS = parse(f)

        print(f"Phase 1: {phase1(INSTRUCTIONS.copy())}")
        print(f"Phase 2: {phase2(INSTRUCTIONS, 956)}")
