from pathlib import Path
from queue import PriorityQueue


def get_heatloss(data, min_count=0, max_count=3):
    seen, to_open = set(), PriorityQueue()
    to_open.put((int(data[0][1]), (0,1), (0,1), 0))
    to_open.put((int(data[1][0]), (1,0), (1,0), 0))
    while not to_open.empty():
        total, curr, d, count = to_open.get()
        if curr == (len(data)-1, len(data[0])-1) and count >= min_count:
            return total

        if (curr, d, count) in seen: continue
        seen.add((curr, d, count))

        for (next_c,next_d) in [(count+1,d),(0,(-d[1],d[0])),(0,(d[1],-d[0]))]:
            next_pos = (curr[0]+next_d[0], curr[1]+next_d[1])
            if next_c >= max_count: continue
            if next_d != d and min_count > (count+1): continue
            if not 0<=next_pos[0]<len(data) or not 0<=next_pos[1]<len(data[0]): continue
            to_open.put((
                total+int(data[next_pos[0]][next_pos[1]]),
                next_pos,
                next_d,
                next_c
            ))


def part1(data):
    return get_heatloss(data)


def part2(data):
    return get_heatloss(data,4,10)


def parse(file):
    return file.splitlines()


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/"+Path(__file__).stem).open(encoding="UTF-8") as f:
        DATA = parse(f.read())

        print(f"Phase 1: {part1(DATA)}")
        print(f"Phase 2: {part2(DATA)}")
