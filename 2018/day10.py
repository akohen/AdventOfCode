from pathlib import Path
import sys
import re

test_mode = True if len(sys.argv) > 1 and sys.argv[1] == "test" else False

def calc_at_second(data, second):
    points = []
    for point in data:
        new_x = point[0]+second*point[2]
        new_y = point[1]+second*point[3]
        points.append([new_x, new_y])
    return points

def find_corners(data, second):
    corners = [99999999,99999999,-99999999,-99999999]
    for point in data:
        new_x = point[0]+second*point[2]
        new_y = point[1]+second*point[3]
        corners = [min(corners[0], new_x), min(corners[1], new_y), max(corners[2], new_x), max(corners[3], new_y)]
    return corners

def display_points(points, corners):
    for y in range(corners[1], corners[3]+1):
        line = ""
        for x in range(corners[0], corners[2]+1):
            line += "X" if [x,y] in points else "."        
        print(line)
    return

def box_size(corners):
    return (corners[2]-corners[0])*(corners[2]-corners[0])+(corners[3]-corners[1])*(corners[3]-corners[1])

def phase1(data):
    distance = box_size(find_corners(data,0))
    for i in range(0,15000):
        prev = distance
        distance = box_size(find_corners(data,i))
        if prev < distance:
            display_points(calc_at_second(data, i-1), find_corners(data,i-1))
            return i-1

if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/day10_sample" if test_mode else "input/day10").open() as f:
        points =  [
            [int(i) for i in matches.group(1,2,3,4)] 
            for line in f if (matches := re.match(r"^position=<\s*(-?\d+),\s*(-?\d+)> velocity=<\s*(-?\d+),\s*(-?\d+)>$", line))]
            

        print('Phase 2: {}'.format(phase1(points)))