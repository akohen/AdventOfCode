from pathlib import Path

def bounding_box(x, y, l):
    return [x-1, y-l, x+1, y+1]

def is_inside(point, box):
    if point[0] < box[0]: return False
    if point[0] > box[2]: return False
    if point[1] < box[1]: return False
    if point[1] > box[3]: return False
    return True

def part1(numbers, symbols): 
    return sum(
        n[0] for n in numbers 
        if any(is_inside(s[1:], bounding_box(*n[1:])) for s in symbols)
    )


def part2(numbers, symbols):
    result = 0
    for s in symbols:
        if s[0] == '*':
            adjacent = [n[0] for n in numbers if is_inside(s[1:], bounding_box(*n[1:]))]
            if len(adjacent) == 2:
                result += adjacent[0] * adjacent[1]
    return result

def parse(file):
    numbers, symbols, data, curr = [], [], file.split('\n'), ''
    for x in range(len(data)):
        for y in range(len(data[0])):
            if str.isdigit(data[x][y]):
                curr += data[x][y]
            if curr and not str.isdigit(data[x][y]):
                numbers.append((int(curr),x,y-1,len(curr)))
                curr = ''
            if curr and y == len(data[0])-1:
                numbers.append((int(curr),x,y,len(curr)))
                curr = ''
            if not str.isdigit(data[x][y]) and data[x][y] != '.':
                symbols.append((data[x][y],x,y))
    return numbers, symbols


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/"+Path(__file__).stem).open(encoding="UTF-8") as f:
        DATA = parse(f.read())

        print(f"Phase 1: {part1(*DATA)}")
        print(f"Phase 2: {part2(*DATA)}")
