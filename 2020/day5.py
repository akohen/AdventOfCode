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
    seats = sorted(seats, key=lambda x: x[2])
    for i in range(len(seats)-1):
        if seats[i+1][2] == seats[i][2]+2:
            return seats[i][2]+1

if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/day5").open() as f:
        boarding_passes = [line.strip() for line in f]
        seats = get_seats(boarding_passes)

        print('Phase 1: {}'.format(phase1(seats)))
        print('Phase 2: {}'.format(phase2(seats)))
