from pathlib import Path
import sys
import re

test_mode = True if len(sys.argv) > 1 and sys.argv[1] == "test" else False


def is_complete(p):
    for key in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]:
        if key not in p: 
            return False
    return True

def phase1(passports):
    return len([True for p in passports if is_complete(p)])


def is_valid(p):
    patterns = {
        "byr": r"^19[2-9]\d|200[0-2]$",
        "iyr": r"^201\d|2020$",
        "eyr": r"^202\d|2030$",
        "hgt": r"^(1[5-8]\d|19[0-3])cm|(59|6\d|7[0-6])in$",
        "hcl": r"^#[0-9a-f]{6}$",
        "ecl": r"^(amb|blu|brn|gry|grn|hzl|oth)$",
        "pid": r"^\d{9}$"
        }
    for val in patterns:
        try:
            if not re.match(patterns[val], p[val]):
                raise ValueError(val)
        except:
            return False
    return True

def phase2(passports):
    return len([True for p in passports if is_valid(p)])


def load(data):
    passports = []
    for p in [p.split("\n") for p in data.split("\n\n")]:
        passport = {}
        for line in p:
            for i in line.split(' '):
                [key, value] = i.split(":")
                passport[key] = value
        passports.append(passport)
    return passports

if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/day4_sample" if test_mode else "input/day4").open() as f:
        PASSPORTS = load(f.read())

        print('Phase 1: {}'.format(phase1(PASSPORTS)))
        print('Phase 2: {}'.format(phase2(PASSPORTS)))
