from pathlib import Path
from heapq import heappush, heappop
from math import prod

def part1(boxes, connections=1000):
    distances = []
    for i, box1 in enumerate(boxes):
        for j, box2 in enumerate(boxes[i+1:], start=i+1):
            heappush(distances, (sum((a - b)**2 for a, b in zip(box1, box2)), (i, j)))

    circuits = []
    circuits_map = {i: [i] for i in range(len(boxes))}
    for _ in range(connections):
        _, (i, j) = heappop(distances)
        circuit_a, circuit_b = circuits_map[i], circuits_map[j]
        if circuit_a is circuit_b:
            continue
        new_circuit = circuit_a + circuit_b
        if len(circuit_a) > 1:
            circuits.remove(circuit_a)
        if len(circuit_b) > 1:
            circuits.remove(circuit_b)
        circuits.append(new_circuit)
        for box_index in new_circuit:
            circuits_map[box_index] = new_circuit

    return prod(sorted(len(c) for c in circuits)[-3:])


def part2(boxes):
    distances = []
    for i, box1 in enumerate(boxes):
        for j, box2 in enumerate(boxes[i+1:], start=i+1):
            heappush(distances, (sum((a - b)**2 for a, b in zip(box1, box2)), (i, j)))

    circuits = []
    circuits_map = {i: [i] for i in range(len(boxes))}
    while True:
        _, (i, j) = heappop(distances)
        circuit_a, circuit_b = circuits_map[i], circuits_map[j]
        if circuit_a is circuit_b:
            continue
        new_circuit = circuit_a + circuit_b
        if len(circuit_a) > 1:
            circuits.remove(circuit_a)
        if len(circuit_b) > 1:
            circuits.remove(circuit_b)
        circuits.append(new_circuit)
        for box_index in new_circuit:
            circuits_map[box_index] = new_circuit
        if len(circuits) == 1 and len(circuits[0]) == len(boxes):
            return boxes[i][0] * boxes[j][0]


def parse(file):
    return [[int(x) for x in line.split(',')] for line in file.splitlines()]


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/"+Path(__file__).stem).open(encoding="UTF-8") as f:
        DATA = parse(f.read())

        print(f"Phase 1: {part1(DATA)}")
        print(f"Phase 2: {part2(DATA)}")