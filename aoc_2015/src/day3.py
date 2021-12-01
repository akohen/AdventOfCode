from pathlib import Path

def phase1(values):
    pos = (0,0)
    seen = set([pos])
    for val in values:
        if val == '>': pos = (pos[0]+1,pos[1])
        if val == '<': pos = (pos[0]-1,pos[1])
        if val == '^': pos = (pos[0],pos[1]+1)
        if val == 'v': pos = (pos[0],pos[1]-1)
        seen.add(pos)
    return len(seen)

def phase2(values):
    pos = [(0,0), (0,0)]
    seen = set([(0,0)])
    for i, val in enumerate(values):
        active = i%2
        if val == '>': pos[active] = (pos[active][0]+1,pos[active][1])
        if val == '<': pos[active] = (pos[active][0]-1,pos[active][1])
        if val == '^': pos[active] = (pos[active][0],pos[active][1]+1)
        if val == 'v': pos[active] = (pos[active][0],pos[active][1]-1)
        seen.add(pos[active])
    return len(seen)

if __name__ == "__main__":
    with Path(__file__).parent.joinpath("../input/day3").open(encoding="UTF-8") as f:
        my_input = f.read()

        print(f"Phase 1: {phase1(my_input)}")
        print(f"Phase 2: {phase2(my_input)}")
