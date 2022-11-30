from pathlib import Path
from typing import DefaultDict

def phase1(fish, days):
    for _ in range(days):
        for i in range(9):
            fish[i-1] = fish[i]
        fish[8] = fish[-1]
        fish[6] += fish[-1]
        del fish[-1]

    return sum(fish.values())



def parse(file):
    fish = DefaultDict(int)
    for i in [int(x) for x in file.split(',')]:
        fish[i] += 1
    return fish

if __name__ == "__main__":
    with Path(__file__).parent.joinpath("../input/"+Path(__file__).stem).open(encoding="UTF-8") as f:
        FISH = parse(f.read())

        print(f"Phase 1: {phase1(FISH.copy(), 80)}")
        print(f"Phase 2: {phase1(FISH, 256)}")
