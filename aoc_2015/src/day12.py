from pathlib import Path
import json


def phase1(node):
    if isinstance(node, int):
        return node
    
    if isinstance(node, list):
        return sum([phase1(n) for n in node])
    
    if isinstance(node, dict):
        return sum([phase1(n) for n in node.values()])
    return 0


def phase2(node):
    if isinstance(node, int):
        return node
    
    if isinstance(node, list):
        return sum([phase2(n) for n in node])
    
    if isinstance(node, dict):
        if "red" in node.values():
            return 0
        return sum([phase2(n) for n in node.values()])
    return 0

def parse(text):
    return json.loads(text)

if __name__ == "__main__":
    with Path(__file__).parent.joinpath("../input/day12").open(encoding="UTF-8") as f:
        FILE = parse(f.read())

        print(f"Phase 1: {phase1(FILE)}")
        print(f"Phase 2: {phase2(FILE)}")
