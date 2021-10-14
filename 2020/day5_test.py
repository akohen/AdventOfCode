from pathlib import Path
import day5

def test_phase1():
    with Path(__file__).parent.joinpath("input/day5_sample").open() as f:
        boarding_passes = [line.strip() for line in f]
        seats = day5.get_seats(boarding_passes)
        assert day5.phase1(seats) == 820
