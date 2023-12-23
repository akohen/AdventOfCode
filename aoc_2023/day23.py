from pathlib import Path
from collections import deque


SLOPES = {'v': (1,0), '>': (0,1), '<': (0,-1), '^': (-1,0)}
def p(point, data): return data[point[0]][point[1]]
def add(p1, p2): return (p1[0]+p2[0], p1[1]+p2[1])

def part1(data):
    start, end, paths = (0,1), (len(data)-1, len(data[0])-2), []
    to_open = [[start]]
    while len(to_open) > 0:
        curr = to_open.pop()
        if curr[-1] == end:
            paths.append(len(curr) -1)
            if len(paths) > 8: return max(paths) # 8 ça suffit
            continue
        for s, d in SLOPES.items():
            point  = add(curr[-1], d)
            val = p(point, data) 
            if point in curr or val == "#": continue
            if val != '.' and val != s: continue
            to_open.append(curr + [point])
    return max(paths)

def part2(data):
    def find_junctions():
        to_open, junctions, seen = deque([(start, 0)]), [], set()
        while len(to_open) > 0:
            curr, count = to_open.pop(), 0
            seen.add(curr[0])
            for d in SLOPES.values():
                point = add(curr[0], d)
                val = p(point, data)
                if point == end: continue
                if point in seen or val == "#": continue
                to_open.append((point, curr[1]+1))
                count += 1
            if count > 1: junctions.append(curr[0])
        return junctions


    def find_paths(start, junctions):
        to_open, paths = deque([[start]]), {}
        while len(to_open) > 0:
            curr = to_open.popleft()
            for d in SLOPES.values():
                point = add(curr[-1], d)
                val = p(point, data)
                if point in curr or val == "#": continue
                if point in junctions:
                    paths[point] = len(curr)
                    continue
                to_open.append(curr + [point])
        return paths

    start, end, distances, paths = (0,1), (len(data)-1, len(data[0])-2), {}, []
    junctions = find_junctions() + [end, start] # Could have been done while finding paths, don't care
    for j in junctions:
        if j == end: continue
        distances[j] = find_paths(j, junctions)


    to_open = deque([([start],0)])
    while len(to_open) > 0:
        path, dist = to_open.pop() # from the right, we want the longest path
        for j in distances[path[-1]]:
            if j in path: continue
            if j == end:
                paths.append(dist + distances[path[-1]][j])
                if len(paths) > 8: return max(paths) # 8 ça suffit
                continue
            to_open.append((path + [j],dist + distances[path[-1]][j]))



def parse(file):
    return [line for line in file.split('\n')]


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/"+Path(__file__).stem).open(encoding="UTF-8") as f:
        DATA = parse(f.read())

        print(f"Phase 1: {part1(DATA)}")
        print(f"Phase 2: {part2(DATA)}")
