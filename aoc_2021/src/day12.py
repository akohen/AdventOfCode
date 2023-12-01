from collections import defaultdict
from pathlib import Path

def is_big(cave): return cave == cave.upper()

def phase1(data):    
    paths, to_open = [], [['start']]
    while len(to_open) > 0:
        current = to_open.pop()
        for node in data[current[-1]]:
            if node == 'end':
                paths.append(current + ['end'])
            elif is_big(node) or node not in current:
                to_open.append(current + [node])
    return len(paths)


def phase2(data):
    def can_visit(path, cave):
        if cave == 'start': return False
        if is_big(cave): return True
        if cave not in path: return True
        small_caves = [x for x in path if not is_big(x)]

        return len(small_caves) == len(set(small_caves))

    paths, to_open = [], [['start']]
    while len(to_open) > 0:
        current = to_open.pop()
        for node in data[current[-1]]:
            if node == 'end':
                paths.append(current + ['end'])
            elif can_visit(current, node):
                to_open.append(current + [node])
    return len(paths)

def parse(file):
    graph = defaultdict(list)
    for line in file.split('\n'):
        a,b = line.split('-')
        graph[a].append(b)
        graph[b].append(a)
    return graph

if __name__ == "__main__":
    with Path(__file__).parent.joinpath("../input/"+Path(__file__).stem).open(encoding="UTF-8") as f:
        DATA = parse(f.read())

        print(f"Phase 1: {phase1(DATA)}")
        print(f"Phase 2: {phase2(DATA)}")
