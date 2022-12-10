from pathlib import Path

def phase1(data, max_cycle = 220):
    x, i, to_add, result = 1, 0, 0, 0
    for cycle in range(2,max_cycle+1):
        if to_add != 0:
            x += to_add
            to_add = 0
        elif data[i] == 'noop':
            i += 1
        else:
            to_add = int(data[i][5:])
            i += 1
        if cycle in [20,60,100,140,180,220]:
            result += cycle * x
    return result


def phase2(data, max_cycle = 240):
    x, i, to_add, result = 1, 0, 0, 0
    output = '\n#'
    for cycle in range(1, max_cycle):
        if to_add != 0:
            x += to_add
            to_add = 0
        elif data[i] == 'noop':
            i += 1
        else:
            to_add = int(data[i][5:])
            i += 1
        output += '#' if cycle % 40 in range(x-1, x+2) else '.'
        if cycle%40 == 39:
            output += '\n'
    return output


def parse(file):
    return file.split('\n')


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/"+Path(__file__).stem).open(encoding="UTF-8") as f:
        DATA = parse(f.read())

        print(f"Phase 1: {phase1(DATA)}")
        print(f"Phase 2: {phase2(DATA)}")
