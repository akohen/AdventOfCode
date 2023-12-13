from pathlib import Path

def part1(data):
    def find_reflecion(arr):
        for i in range(1,len(arr)):
            l = arr[i-min(i,len(arr)-i) : i]
            r = arr[min(len(arr),2*i)-1 : i-1 : -1]
            if l == r: return i
        return 0

    def pattern_value(pattern):
        cols, rows = [0]*len(pattern[0]), [0]*len(pattern)
        for i in range(len(rows)):
            for j in range(len(cols)):
                if pattern[i][j] == '#':
                    cols[j] += 2**i
                    rows[i] += 2**j
        return find_reflecion(cols) + 100*find_reflecion(rows)

    return sum(pattern_value(pattern) for pattern in data)


def part2(data):
    def find_reflecion(arr):
        for i in range(1,len(arr)):
            l = arr[i-min(i,len(arr)-i) : i]
            r = arr[min(len(arr),2*i)-1 : i-1 : -1]
            diff = [(l[i],r[i]) for i in range(len(l)) if l[i] != r[i]]
            if len(diff) == 1:
                if len([x for x in zip(*diff[0]) if x[0] != x[1]]) == 1:
                    return i
                
        return 0

    def pattern_value(pattern):
        cols, rows = ['']*len(pattern[0]), ['']*len(pattern)
        for i in range(len(rows)):
            for j in range(len(cols)):
                cols[j] += pattern[i][j]
                rows[i] += pattern[i][j]
        return find_reflecion(cols) + 100*find_reflecion(rows)

    return sum(pattern_value(pattern) for pattern in data)


def parse(file):
    return [pattern.split('\n') for pattern in file.split('\n\n')]


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/"+Path(__file__).stem).open(encoding="UTF-8") as f:
        DATA = parse(f.read())

        print(f"Phase 1: {part1(DATA)}")
        print(f"Phase 2: {part2(DATA)}")
