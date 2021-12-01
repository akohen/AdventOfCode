from pathlib import Path
from functools import reduce
from operator import add


def find_corners(points):
    """Top left and bottom right corners of the points provided"""
    xmin = xmax = points[0][0]
    ymin = ymax = points[0][1]
    for point in points:
        xmax = max(xmax, point[0])
        xmin = min(xmin, point[0])
        ymax = max(ymax, point[1])
        ymin = min(ymin, point[1])
    return ((xmin,ymin),(xmax,ymax))

def get_distance(a, b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])

def is_on_border(corners, point):
    if point[0] == corners[0][0] or point[0] == corners[1][0] or point[1] == corners[0][1] or point[1] == corners[1][1]:
        return True
    return False

def measure_area(corners, points):
    """Count how many coordinates are closest to each point using Manhattan distance.
    Ties are not counted. 
    If the border of the grid is closest to a point, that point is marked as infinite"""
    for x in range(corners[0][1], corners[1][1]+1):
        for y in range(corners[0][1], corners[1][1]+1):
            distances = sorted([(get_distance([x,y],point),i) for i, point in enumerate(points)])
            if distances[0][0] < distances[1][0]: #discard ties
                points[distances[0][1]][2] += 1
                if is_on_border(corners, [x, y]): # Mark infinite areas
                    points[distances[0][1]][3] = 1

def measure_safe_area(corners, points, max_distance):
    """Count how many coordinates are within max_distance of all points"""
    total_area = 0
    for x in range(corners[0][1], corners[1][1]+1):
        for y in range(corners[0][1], corners[1][1]+1):
            distance = reduce(add,[get_distance([x,y], point) for point in points])
            if distance < max_distance:
                total_area += 1
    return total_area


if __name__ == "__main__":
  with Path(__file__).parent.joinpath("input/day6").open() as f:
    points = [[int(coord) for coord in line.split(',')]+[0,0] for line in f] # x,y, count, is_infite

    corners = find_corners(points)
    measure_area(corners, points)

    max_area = 0
    for idx, point in enumerate(points):
        if point[2] > max_area and point[3] == 0:
            max_area = point[2]
    
    print('Phase 1: {}'.format(max_area))
    print('Phase 2: {}'.format(measure_safe_area(corners, points, 10000)))

    