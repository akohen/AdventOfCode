from pathlib import Path
from functools import reduce
import re

def part1(data):
    return sum(reduce(lambda a,c:(a+ord(c))*17%256, s, 0) for s in data)


def part2(data):
    boxes = [{} for _ in range(256)]
    for s in data:       
        label, op, val = re.match('(\w+)(=|-)(\d*)', s).groups()
        box_id = reduce(lambda a,c:(a+ord(c))*17%256, label, 0)
        if op == '=':
            boxes[box_id][label] = int(val)
        elif label in boxes[box_id]: 
            del boxes[box_id][label]

    return sum((1+i)*a*b for i in range(256) for a,b in enumerate(boxes[i].values(),1))


def parse(file):
    return file.split(',')


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/"+Path(__file__).stem).open(encoding="UTF-8") as f:
        DATA = parse(f.read())

        print(f"Phase 1: {part1(DATA)}")
        print(f"Phase 2: {part2(DATA)}")
