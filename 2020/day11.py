from pathlib import Path
from collections import defaultdict
import sys

TEST_MODE = bool(len(sys.argv) > 1 and sys.argv[1] == "test")


def display(wait_area):
    for line in wait_area:
        print(''.join(line))


def count_adjacent_seats(seat, wait_area):
    total = 0
    for i in range(max(0,seat[0]-1), min(len(wait_area),seat[0]+2)):
        for j in range(max(0,seat[1]-1), min(len(wait_area[0]),seat[1]+2)):
            total += 1 if (i != seat[0] or j != seat[1]) and wait_area[i][j] == '#' else 0
    return total

def new_seat(seat,wait_area,changes):
    if wait_area[seat[0]][seat[1]] == "L" and count_adjacent_seats(seat, wait_area) == 0:
        changes.append(True)
        return '#'
    if wait_area[seat[0]][seat[1]] == "#" and count_adjacent_seats(seat, wait_area) >= 4: 
        changes.append(True)
        return 'L'
    return wait_area[seat[0]][seat[1]]

def phase1(data):
    changes = [1]
    while len(changes) > 0:
        changes = []
        data, changes = [[new_seat([y,x], data, changes) for x in range(len(data[y]))] for y in range(len(data))], changes
    return sum([line.count('#') for line in data])



def count_visible_seats(seat, wait_area):
    directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,0),(1,-1),(1,1)]
    total = 0
    for direction in directions:
        if is_seat_in_direction(seat, direction, wait_area):
            total += 1
    return total

def is_seat_in_direction(seat, direction, wait_area):
    for i in range(1,len(wait_area)):
        y = seat[0]+ i*direction[0]
        x = seat[1]+ i*direction[1]
        if x < 0 or y < 0 or x >= len(wait_area[0]) or y >= len(wait_area):
            return False
        if wait_area[y][x] == 'L':
            return False
        if wait_area[y][x] == '#':
            return True
    return False

def new_seat2(seat,wait_area,changes):
    if wait_area[seat[0]][seat[1]] == "L" and count_visible_seats(seat, wait_area) == 0:
        changes.append(True)
        return '#'
    if wait_area[seat[0]][seat[1]] == "#" and count_visible_seats(seat, wait_area) >= 5: 
        changes.append(True)
        return 'L'
    return wait_area[seat[0]][seat[1]]

def phase2(data):
    changes = [1]
    while len(changes) > 0:
        changes = []
        data, changes = [[new_seat2([y,x], data, changes) for x in range(len(data[y]))] for y in range(len(data))], changes
    return sum([line.count('#') for line in data])

if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/day11_sample" if TEST_MODE else "input/day11").open() as f:
        WAITAREA = [line.strip() for line in f]

        print(f'Phase 1: {phase1(WAITAREA)}')
        print(f'Phase 2: {phase2(WAITAREA)}')