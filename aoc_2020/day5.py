from pathlib import Path


def get_seats(boarding_passes):
    return [get_seat(p) for p in boarding_passes]

def phase1(seats):
    return max(seats)[0]

def get_seat(boarding_pass):
    row = int(boarding_pass[0:7].replace('F','0').replace('B',"1"),2)
    column = int(boarding_pass[7:10].replace('L','0').replace('R',"1"),2)
    return row*8+column, row, column

def phase2(seats):
    seats = sorted(seats)
    for i in range(len(seats)-1):
        if seats[i+1][0] == seats[i][0]+2:
            return seats[i][0]+1

if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/day5").open() as f:
        boarding_passes = [line.strip() for line in f]
        seats = get_seats(boarding_passes)

        print(f'Phase 1: {phase1(seats)}')
        print(f'Phase 2: {phase2(seats)}')
