from pathlib import Path

def tilt(cols, rows, rocks, dir):
    next_rocks = []
    for (x,y) in rocks:
        new_pos = (
            dir[0] + {-1: min, 1: max}[dir[0]]([i for i in cols[y] if dir[0]*x-dir[0]*i>0]) if dir[0] != 0 else x, 
            dir[1] + {-1: min, 1: max}[dir[1]]([i for i in rows[x] if dir[1]*y-dir[1]*i>0]) if dir[1] != 0 else y
        )

        while (new_pos) in next_rocks:
            new_pos = (new_pos[0]+dir[0], new_pos[1]+dir[1])
        next_rocks.append(new_pos)
    return next_rocks

def part1(height, cols, rows, rocks):   
    return sum(height-x for (x,_) in tilt(cols, rows, rocks, (1,0)))


def part2(height, cols, rows, rocks):
    cycle, history = [(1,0),(0,1),(-1,0),(0,-1)], []
    for step in range(10000):
        rocks = tilt(cols, rows, rocks, cycle[step%4])
        hash = set(rocks)
        if step%50 == 0:
            print(step)
        if hash in history:
            remaining_steps = 1000000000*4 - step
            current_step = history.index(hash)
            cycle_length = len(history) - current_step
            final_step = current_step+remaining_steps%cycle_length
            return sum(height-x for (x,_) in history[final_step-1])
        history.append(hash)


def parse(file):
    data, rocks = file.split('\n'), []
    cols = [[-1, len(data[0])] for _ in range(len(data[0]))]
    rows = [[-1, len(data)] for _ in range(len(data))]
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == '#': 
                cols[j].append(i)
                rows[i].append(j)
            if data[i][j] == 'O': rocks.append((i,j))
    return len(data), cols, rows, tuple(rocks)


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/"+Path(__file__).stem).open(encoding="UTF-8") as f:
        DATA = parse(f.read())

        print(f"Phase 1: {part1(*DATA)}")
        print(f"Phase 2: {part2(*DATA)}")
