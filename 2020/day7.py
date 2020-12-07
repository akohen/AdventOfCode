from pathlib import Path
import sys
import regex

test_mode = True if len(sys.argv) > 1 and sys.argv[1] == "test" else False

def phase1(rules):
    total = 0
    for color in rules:
        if can_contain(rules, color, "shiny gold"):
            total += 1
    return total

def can_contain(rules, outer, inner):
    if inner in rules[outer]:
        return True
    if rules[outer] == {}:
        return False
    for color in rules[outer]:
        if can_contain(rules, color, inner):
            return True
    return False

def phase2(rules):
    return count_bags(rules, "shiny gold") -1

def count_bags(rules, bag):
    total = 1
    for color in rules[bag]:
        total += int(rules[bag][color]) * count_bags(rules, color)
    return total

def load(data):
    rules = {}
    for line in data:
        matches = regex.match(r"(\w+ \w+) bags contain(?: (\d+) (\w+ \w+) bags?,?)*.", line)
        rules[matches.captures(1)[0]] = {}
        for idx, color in enumerate(matches.captures(3)):
            rules[matches.captures(1)[0]][color] = matches.captures(2)[idx]
    return rules

if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/day7_sample" if test_mode else "input/day7").open() as f:
        data = load([line.rstrip("\n") for line in f])
        
        print('Phase 1: {}'.format(phase1(data)))
        print('Phase 2: {}'.format(phase2(data)))