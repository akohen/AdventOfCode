from pathlib import Path
import re
import sys

TEST_MODE = bool(len(sys.argv) > 1 and sys.argv[1] == "test")


def get_rule(rules, rule_id, phase2=False):
    if rules[rule_id][0] == '"':
        return rules[rule_id][1:-1]
    else:
        result = ""
        for val in rules[rule_id].split(" "):
            if val == "|":
                result += "|"
            else:
                result += get_rule(rules, int(val), phase2)
        result = "({})".format(result)
        if phase2 == True and rule_id == 8:
            result += '+'
        if phase2 == True and rule_id == 11:
            result = '(' + get_rule(rules, 42) + '{1}' + get_rule(rules,31) + '{1})|'
            result += '(' + get_rule(rules, 42) + '{2}' + get_rule(rules,31) + '{2})|'
            result += '(' + get_rule(rules, 42) + '{3}' + get_rule(rules,31) + '{3})|'
            result += '(' + get_rule(rules, 42) + '{4}' + get_rule(rules,31) + '{4})'
            result = "({})".format(result)
        return result
 
def phase1(rules, messages):
    rule = re.compile("^{}$".format(get_rule(rules, 0)))
    return sum([1 for message in messages if rule.match(message)])

def phase2(rules, messages):
    rule = re.compile("^{}$".format(get_rule(rules, 0, True)))
    return sum([1 for message in messages if rule.match(message)])

def load(data):
    rules = {}
    for r in data[0]:
        rule = r.split(": ")
        rules[int(rule[0])] = rule[1]
    return rules, data[1]

if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/day19_sample" if TEST_MODE else "input/day19").open() as f:
        DATA, MESSAGES = load([line.split("\n") for line in f.read().split("\n\n")])

        print('Phase 1: {}'.format(phase1(DATA, MESSAGES)))
        print('Phase 2: {}'.format(phase2(DATA, MESSAGES)))