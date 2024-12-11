from pathlib import Path

def rotate(data):
    return list(map(''.join, zip(*reversed(data))))

def diagonal(data):
    return [
        ''.join(
            data[x][i-x] for x in range(i+1)
            if 0 <= x < len(data) and 0 <= i-x < len(data[0])
        ) for i in range(len(data)+len(data[0])-1)
    ]

def part1(data):
    total = 0
    for _ in range(4):
        total += sum(line.count('XMAS') for line in data)
        total += sum(line.count('XMAS') for line in diagonal(data))
        data = rotate(data)
    return total


def part2(data):
    total = 0
    for x in range(1,len(data)-1):
        for y in range(1,len(data[0])-1):
            if data[x][y] == 'A':
                d1 = data[x-1][y-1] + data[x+1][y+1]
                d2 = data[x-1][y+1] + data[x+1][y-1]
                if d1 in ['MS','SM'] and d2 in ['MS','SM']:
                    total += 1
    return total


def parse(file):
    return [line for line in file.split('\n')]


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/"+Path(__file__).stem).open(encoding="UTF-8") as f:
        DATA = parse(f.read())

        print(f"Phase 1: {part1(DATA)}")
        print(f"Phase 2: {part2(DATA)}")
