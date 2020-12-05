from pathlib import Path
import day5

def test_phase1():
    with Path(__file__).parent.joinpath("input/day5_sample").open() as f:
        boarding_passes = [line.strip() for line in f]
        seats = day5.get_seats(boarding_passes)
        assert day5.phase1(seats) == 820


def test_seat_ids():
    seats = [("FBFBBFFRLR", 357), ("BFFFBBFRRR", 567), ("FFFBBBFRRR", 119), ("BBFFBBFRLL", 820)]
    for s in seats:
        assert day5.get_seat(s[0])[2] == s[1]