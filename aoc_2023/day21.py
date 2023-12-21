from pathlib import Path


def count_plots(data, steps):
    size = len(data)
    seen, total, edges, next = {(size//2, size//2):0}, [1], [1], [(size//2, size//2)]
    for i in range(steps):
        to_open, next = next, []
        while len(to_open) > 0:
            x,y = to_open.pop()
            for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                next_x, next_y = x+dx, y+dy
                if data[next_x%size][next_y%size] == '#': continue
                if (next_x, next_y) in seen: continue
                seen[(next_x, next_y)] = i+1
                next.append((next_x, next_y))
        total.append(len(next) + (total[i-1] if i > 0 else 0))
        edges.append(len(next))
    return total


def part1(data, steps=6):
    return count_plots(data, steps)[-1]


def part2(data):
    size = len(data)
    n, r  = 26501365//size, 26501365%size

    #return 14840*(n+1)*(n+1)-14740*(n+1)+3651 # Wolfram alpha solution
    total = count_plots(data, r+2*size)
    a = total[r+2*size] - total[r+size]
    b = total[r+2*size] + total[r] - 2*total[r+size]
    
    return total[r+2*size] + (n-2)*(2*a + (n-1)*b)//2


def parse(file):
    return file.split('\n')


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/"+Path(__file__).stem).open(encoding="UTF-8") as f:
        DATA = parse(f.read())

        print(f"Phase 1: {part1(DATA, 64)}")
        print(f"Phase 2: {part2(DATA)}")
