from pathlib import Path
import sys
import re

TEST_MODE = bool(len(sys.argv) > 1 and sys.argv[1] == "test")

def phase1(policies):
    return len([1 for p in policies if p["password"].count(p["char"]) <= p["max"] and p["password"].count(p["char"]) >= p["min"] ])

def phase2(policies):
    return len([1 for p in policies if ((p["password"][p["min"]-1] == p["char"]) ^ (p["password"][p["max"]-1] == p["char"]))])

if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/day2_sample" if TEST_MODE else "input/day2").open() as f:
        regex = re.compile(r'(\d+)-(\d+) (\w): (\w+)')
        policies = [
            {"min": int(matches[1]), "max": int(matches[2]), "char": matches[3], "password": matches[4]} 
            for line in f if (matches := regex.match(line)) ]
        
        print(f'Phase 1: {phase1(policies)}')
        print(f'Phase 2: {phase2(policies)}')
