from pathlib import Path
from collections import deque, defaultdict

PIPES = {
    '|': ((-1,0),(1,0)), #is a vertical pipe connecting north and south.
    '-': ((0,-1),(0,1)), # is a horizontal pipe connecting east and west.
    'L': ((-1,0),(0,1)), # is a 90-degree bend connecting north and east.
    'J': ((-1,0),(0,-1)), # is a 90-degree bend connecting north and west.
    '7': ((1,0),(0,-1)), # is a 90-degree bend connecting south and west.
    'F': ((1,0),(0,1)), # is a 90-degree bend connecting south and east.
    '.': ((0,0),(0,0)), # is ground; there is no pipe in this tile.
    'S': ((-1,0),(1,0),(0,-1),(0,1)) # is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
}

def is_connected(maze, start, end):
    if end not in maze:  return False
    if start in [(end[0]+dir[0], end[1]+dir[1])  for dir in maze[end]]: return True
    return False


def part2(data):
    def next_step(start, seen, edges):
        for direction in maze[start]:
            end = (direction[0]+start[0], direction[1]+start[1])
            if end not in seen and end in maze:
                if direction == (0,1): edges[start][0] = True
                if direction == (0,-1): edges[end][0] = True
                if direction == (1,0): edges[start][1] = True
                if direction == (-1,0): edges[end][1] = True
                return end
        return False
    
    # edges = box on the bottom right corner of point x,y (top wall: bool, left wall: bool)
    maze, to_open, seen, edges = {}, deque(), [], defaultdict(lambda:[False, False])
    # Store list of pipe connections in maze
    for x in range(len(data)):
        for y in range(len(data[0])):
            if data[x][y] != '.':
                maze[(x,y)] = PIPES[data[x][y]]
            if data[x][y] == 'S':
                start = (x,y)

    # Ugly hack to generate edges around start pos and initial path
    seen.append(start)
    for dir in PIPES['S']:
        end = (start[0]+dir[0], start[1]+dir[1])
        if end not in seen and end in maze:
            if dir == (0,1): edges[start][0] = True
            if dir == (0,-1): edges[end][0] = True
            if dir == (1,0): edges[start][1] = True
            if dir == (-1,0): edges[end][1] = True
        if is_connected(maze, start, end):
            to_open.append(end)

    # Walk along both sides of the path, furthest point will be the last one added
    while len(to_open) > 1:
        curr = to_open.popleft()
        seen.append(curr)
        nxt = next_step(curr, seen, edges) # Also generates edges, why not
        if nxt: to_open.append(nxt)



    # PART 2
    # Checking which tiles can exit
    def find_connected_tiles(start):
        tiles = []
        if not edges[start][0]: tiles.append((start[0]-1, start[1]))
        if not edges[start][1]: tiles.append((start[0], start[1]-1))
        if not edges[(start[0]+1, start[1])][0]: tiles.append((start[0]+1, start[1]))
        if not edges[(start[0], start[1]+1)][1]: tiles.append((start[0], start[1]+1))
        return tiles
    
    def is_outside(start):
        to_open, current_zone = deque(), set()
        to_open.append(start)
        while len(to_open) > 0:
            curr = to_open.popleft()
            current_zone.add(curr)
            for tile in find_connected_tiles(curr):
                if tile[0] < 0 or tile[1] < 0 \
                        or tile[0] >= len(data) or tile[1] >= len(data[0]) \
                        or tile in outside:
                    outside.update(current_zone)
                    outside.update(set(to_open))
                    return True
                if tile not in current_zone and tile not in to_open: to_open.append(tile)
        stays_inside.update(current_zone)
        return False

    outside, inside, stays_inside = set(), set(), set()
    for x in range(len(data)):
        for y in range(len(data[0])):
            if (x,y) in seen: continue
            if (x,y) in stays_inside: inside.add((x,y))
            elif (x,y) not in outside:
                if not is_outside((x,y)):
                    inside.add((x,y))
    
    return len(seen)//2, len(inside)


def parse(file):
    return [line for line in file.split('\n')]


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/"+Path(__file__).stem).open(encoding="UTF-8") as f:
        DATA = parse(f.read())

        print(f"Phase 2: {part2(DATA)}")
