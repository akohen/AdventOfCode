from pathlib import Path

def phase1(elfs):
    return max([sum(elf) for elf in elfs])


def phase2(elfs):
    return sum(sorted([sum(elf) for elf in elfs])[-3:])


def parse(file):
    return [[int(x) for x in elf.split('\n')] for elf in file.split('\n\n')]


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/"+Path(__file__).stem).open(encoding="UTF-8") as f:
        ELFS = parse(f.read())

        print(f"Phase 1: {phase1(ELFS)}")
        print(f"Phase 2: {phase2(ELFS)}")
