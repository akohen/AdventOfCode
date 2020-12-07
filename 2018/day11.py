from pathlib import Path
import sys
import re

test_mode = True if len(sys.argv) > 1 and sys.argv[1] == "test" else False

def phase2(grid):
    best, best_box = 0, ()
    for size in range(10,17):
        val, box = largest(size, grid)
        if val > best:
            best_box = box, size
            best = val
    return best_box

def get_power_level(x,y,serial):
    rack = x + 10
    return (rack * (rack * y + serial)//100)%10-5

def get_grid(serial):
    grid = []
    for x in range(301):
        grid.append([get_power_level(x,y,serial) for y in range(301)])
    return grid

def largest(size, grid):
    best, best_coords = 0, ()
    for x in range(1,301-size):
        for y in range(1,301-size):
            val = 0
            for i in range(size):
                for j in range(size):
                    val += grid[x+i][y+j]
            if val > best:
                best = val
                best_coords = (x, y)
    return best, best_coords

if __name__ == "__main__":
    serial = 42 if test_mode else 7989
    grid = get_grid(serial)
    print('Phase 1: {}'.format(largest(3, grid)))
    print('Phase 2: {}'.format(phase2(grid)))