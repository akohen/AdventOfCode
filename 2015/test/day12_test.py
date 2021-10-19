from src import day12

def test_phase1():
    assert day12.phase1(day12.parse('[1,2,3]')) == 6
    assert day12.phase1(day12.parse('{"a":2,"b":4}')) == 6
    assert day12.phase1(day12.parse('{"a":{"b":4},"c":-1}')) == 3
    assert day12.phase1(day12.parse('{"a":[-1,1]}')) == 0

def test_phase2():
    assert day12.phase2(day12.parse('[1,2,3]')) == 6
    assert day12.phase2(day12.parse('[1,{"c":"red","b":2},3]')) == 4
    assert day12.phase2(day12.parse('{"d":"red","e":[1,2,3,4],"f":5}')) == 0
    assert day12.phase2(day12.parse('[1,"red",5]')) == 6
