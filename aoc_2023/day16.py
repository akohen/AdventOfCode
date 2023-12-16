from pathlib import Path
from collections import deque

N, S, W, E = (-1,0), (1,0), (0,-1), (0,1)

def part1(mirrors, size):
    return find_rays(mirrors, size, (0,-1,E))

def part2(mirrors, size):
    beams = ([(x, -1, E) for x in range(size[0])] +
        [(-1, y, S) for y in range(size[1])] +
        [(x, size[1], W) for x in range(size[0])] +
        [(size[0], y, N) for y in range(size[1])])
    return max(find_rays(mirrors, size, beam) for beam in beams)

def find_rays(mirrors, size, start):
    energized, rays, to_open = set(), set(), deque([start])

    while len(to_open) > 0:
        (x,y, direction) = to_open.popleft()
        x += direction[0]
        y += direction[1]
        while 0<=x<size[0] and 0<=y<size[1]:
            energized.add((x,y))
            if (x,y,direction) in mirrors:
                for new_dir in mirrors[(x,y,direction)]:
                    if (x,y,new_dir) not in rays:
                        rays.add((x,y,new_dir))
                        to_open.append((x,y,new_dir))
                break
            x += direction[0]
            y += direction[1]

    return len(energized)


def parse(file):
    data, mirrors = file.split('\n'), {}
    for x in range(len(data)):
        for y in range(len(data[0])):
            if data[x][y] == '|':
                mirrors[(x,y,W)] = [N,S]
                mirrors[(x,y,E)] = [N,S]
            elif data[x][y] == '-':
                mirrors[(x,y,N)] = [E,W]
                mirrors[(x,y,S)] = [E,W]
            elif data[x][y] == '/':
                mirrors[(x,y,N)] = [E]
                mirrors[(x,y,S)] = [W]
                mirrors[(x,y,W)] = [S]
                mirrors[(x,y,E)] = [N]
            elif data[x][y] == '\\':
                mirrors[(x,y,N)] = [W]
                mirrors[(x,y,S)] = [E]
                mirrors[(x,y,W)] = [N]
                mirrors[(x,y,E)] = [S]
    return mirrors, (len(data), len(data[0]))


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/"+Path(__file__).stem).open(encoding="UTF-8") as f:
        DATA = parse(f.read())

        print(f"Phase 1: {part1(*DATA)}")
        print(f"Phase 2: {part2(*DATA)}")
