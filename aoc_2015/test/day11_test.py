from aoc_2015.src import day11

def test_phase1():
    assert day11.is_valid("hijklmmn") is False
    assert day11.is_valid("abbceffg") is False
    assert day11.is_valid("abbcegjk") is False
    assert day11.is_valid("abcdffaa") is True
