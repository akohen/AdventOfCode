from pathlib import Path
import sys
import re


def get_seats(boarding_passes):
    return [get_seat(p) for p in boarding_passes]

def phase1(seats):
    return max(seats,key=lambda x: x[2])[2]

def get_seat(boarding_pass):
    row = int(boarding_pass[0:7].replace('F','0').replace('B',"1"),2)
    column = int(boarding_pass[7:10].replace('L','0').replace('R',"1"),2)
    return row, column, row*8+column

def phase2(seats):
    max_id = phase1(seats)
    max_row = -1
    max_col = -1
    for seat in seats:
        max_row = max(max_row, seat[0])
        max_col = max(max_col, seat[1])
    for x in range(1, max_row+1):
        for y in range(0, max_col+1):
            if (x,y,x*8+y) not in seats and (x*8+y) < max_id:
                return x*8+y

if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/day5").open() as f:
        boarding_passes = [line.strip() for line in f]
        seats = get_seats(boarding_passes)

        print('Phase 1: {}'.format(phase1(seats)))
        print('Phase 2: {}'.format(phase2(seats)))
