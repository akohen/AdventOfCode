from pathlib import Path

def apply_fold(dots, fold):
    new_dots = []
    for dot in dots:
        new_dots.append(tuple(
            dot[i] - 2 * max(dot[i]-fold[i], 0) 
            for i in range(2)
        ))
    return set(new_dots)

def display(dots, bounds):
    str = ['']
    for y in range(bounds[1]):
        str.append(''.join(['#' if (x,y) in dots else '.' for x in range(bounds[0])]))
    return str

def part1(dots, folds):
    return len(apply_fold(dots, folds[0]))


def part2(dots, folds):
    bounds = [999,999]
    for fold in folds:
        bounds = [min(bounds[0], fold[0]), min(bounds[1], fold[1])]
        dots = apply_fold(dots, fold)
    return '\n'.join(display(dots, bounds))


def parse(file):
    dots, folds = file.split('\n\n')
    return [
        [tuple(int(x) for x in dot.split(',')) for dot in dots.split('\n')],
        [
            [int(line[13:]) if line[11] == i else 99999 for i in ['x', 'y']]
            for line in folds.split('\n')
        ]
    ]


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("../input/"+Path(__file__).stem).open(encoding="UTF-8") as f:
        DATA = parse(f.read())

        print(f"Phase 1: {part1(*DATA)}")
        print(f"Phase 2: {part2(*DATA)}")
