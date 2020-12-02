from pathlib import Path
import sys
import re

test_mode = True if len(sys.argv) > 1 and sys.argv[1] == "test" else False

def phase1(policies):
    return len([1 for p in policies if p["password"].count(p["char"]) <= p["max"] and p["password"].count(p["char"]) >= p["min"] ])

def phase2(policies):
    def is_valid(p):
        if p["password"][p["min"]-1] == p["password"][p["max"]-1]:
            return False
        if p["password"][p["min"]-1] != p["char"] and p["password"][p["max"]-1] != p["char"]:
            return False
        return True
    return len([1 for policy in policies if is_valid(policy)])

if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/day2_sample" if test_mode else "input/day2").open() as f:
        regex = re.compile(r'(\d+)-(\d+) (\w): (\w+)')
        policies = [
            {"min": int(matches[1]), "max": int(matches[2]), "char": matches[3], "password": matches[4]} 
            for line in f if (matches := regex.match(line)) ]
        
        print('Phase 1: {}'.format(phase1(policies)))
        print('Phase 2: {}'.format(phase2(policies)))