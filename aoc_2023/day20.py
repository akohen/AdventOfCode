from pathlib import Path
from collections import deque, defaultdict
from math import prod
from copy import deepcopy


def process_signal(modules):
    signals, low, high = deque([('button','broadcaster',False)]), 0, 0

    while len(signals) > 0:
        source, dest, pulse = signals.popleft()
        
        if pulse: high += 1
        else: low += 1
        module = modules[dest]

        # defining return value
        out_pulse = None
        if module['type'] == '%':
            if pulse == False:
                module['values'] = not module['values']
                out_pulse = module['values']
        elif module['type'] == '&':
            module['values'][source] = pulse
            out_pulse = not all(module['values'].values())
        else: out_pulse = pulse

        # output
        if out_pulse == None: continue
        for out in modules[dest]['outputs']:
            signals.append((dest, out, out_pulse))
    return low, high

def part1(modules):
    total = [0,0]
    for _ in range(1000):
        low, high = process_signal(modules)
        total = [total[0]+low, total[1]+high]

    return total[0] * total[1]


def part2(modules):
    for m in modules:
        if 'rx' in modules[m]['outputs']:
            final_module = m
    cycles, i = [], 0
    
    while len(cycles) < len(modules[final_module]['values']):
        signals, low, high = deque([('button','broadcaster',False)]), 0, 0
        i += 1

        while len(signals) > 0:
            source, dest, pulse = signals.popleft()
            
            if dest == final_module and pulse: cycles.append(i)
            if pulse: high += 1
            else: low += 1
            module = modules[dest]

            # defining return value
            out_pulse = None
            if module['type'] == '%':
                if pulse == False:
                    module['values'] = not module['values']
                    out_pulse = module['values']
            elif module['type'] == '&':
                module['values'][source] = pulse
                out_pulse = not all(module['values'].values())
            else: out_pulse = pulse

            # output
            if out_pulse == None: continue
            for out in modules[dest]['outputs']:
                signals.append((dest, out, out_pulse))

    return prod(cycles)


def parse(file):
    modules = defaultdict(lambda: {"type":'', "outputs": [], "values":False})
    for line in file.split('\n'):
        first, *rest = line.replace(' ->','').replace(',','').split()
        (key, t) = (first[1:], first[0]) if first[0] in '%&' else (first, 'start')
        modules[key] = {"type":t, "outputs": rest, "values": {} if t == '&' else False}
    
    for module in list(modules.keys()):
        for out in modules[module]['outputs']:
            if modules[out]['type'] == '&':
                modules[out]['values'][module] = False
    return modules


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/"+Path(__file__).stem).open(encoding="UTF-8") as f:
        DATA = parse(f.read())

        print(f"Phase 1: {part1(deepcopy(DATA))}")
        print(f"Phase 2: {part2(DATA)}")
