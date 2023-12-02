from pathlib import Path
import math

def part1(data, cubes):
    def is_valid(game):
        return all(a <= b for round in game for a,b in zip(round, cubes))
    return sum([id for id, game in enumerate(data, 1) if is_valid(game)])


def part2(data):
    def get_power(game):
        return math.prod([max(i) for i in zip(*game)])
    return sum([get_power(game) for game in data])


def parse(file):
    '''returns [  
        [[r,g,b],[r,g,b]...] ,
        ...   
    ]'''
    def rgb(str):
        result = [0,0,0]
        for cubes in str.split(', '):
            v, c = cubes.split(' ')
            result[{'red':0, 'green':1, 'blue':2}[c]] = int(v)
        return result

    return [
        [rgb(x) for x in line.split(': ')[1].split('; ')]
        for line in file.split('\n')
    ]


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/"+Path(__file__).stem).open(encoding="UTF-8") as f:
        DATA = parse(f.read())

        print(f"Phase 1: {part1(DATA, [12,13,14])}")
        print(f"Phase 2: {part2(DATA)}")
