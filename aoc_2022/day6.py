from pathlib import Path

def phase1(data, size):
    for i in range(0, len(data)-size):
        if len(set(data[i:i+size])) == size:
            return i + size
    return -1


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/"+Path(__file__).stem).open(encoding="UTF-8") as f:
        DATA = f.read()

        print(f"Phase 1: {phase1(DATA, 4)}")
        print(f"Phase 2: {phase1(DATA, 14)}")
