from pathlib import Path
import sys
import re


TEST_MODE = bool(len(sys.argv) > 1 and sys.argv[1] == "test")

def is_field_valid(rules, value):
    for i in rules:
        for rule in rules[i]:
            if value >= rule[0] and value <= rule[1]:
                return True
    return False

def is_field_valid_for_rule(rules, value):
    for rule in rules:
        if value >= rule[0] and value <= rule[1]:
            return True
    return False

def is_ticket_valid(rules, ticket):
    for val in ticket:
        if not is_field_valid(rules, val):
            return False
    return True

def phase1(rules, tickets):
    total = 0
    for ticket in tickets:
        for val in ticket:
            total += val if not is_field_valid(rules, val) else 0
    return total


def phase2(rules, tickets, your_ticket):
    valid_tickets = [ticket for ticket in tickets if is_ticket_valid(rules, ticket)]
    possible_labels = [list(rules.keys()) for i in range(len(your_ticket))]
    for ticket in valid_tickets: # remove impossible fields for each position for each ticket
        for i, val in enumerate(ticket):
            for label in possible_labels[i]:
                if not is_field_valid_for_rule(rules[label], val):
                    possible_labels[i].remove(label)
        
    labels = {}
    for _ in range(len(your_ticket)): # find single possible choice, remove it from all others, assume worst case of 1 removal by pass
        for i, label in enumerate(possible_labels):
            if len(label) == 1:
                found = label[0]
                labels[found] = i
                for l in possible_labels:
                    if found in l:
                        l.remove(found)
    
    result = 1
    for label in labels:
        if label[:9] == "departure":
            result *= your_ticket[labels[label]]
    return result

def load(data):
    rules = {}
    your_ticket = [int(i) for i in data[1][1].split(',')]
    for line in data[0]: #rules
        matches = re.match(r"(\w+(?: \w+)?): (\d+)-(\d+) or (\d+)-(\d+)", line).groups()
        rules[matches[0]] = ((int(matches[1]),int(matches[2])), (int(matches[3]), int(matches[4])))
    tickets = [[int(i) for i in line.split(',')] for line in data[2][1:]]
    return (rules, your_ticket, tickets)

if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/day16_sample2" if TEST_MODE else "input/day16").open() as f:
        RULES, YOUR_TICKET, TICKETS = load([line.split("\n") for line in f.read().split("\n\n")])

        print('Phase 1: {}'.format(phase1(RULES, TICKETS)))
        print('Phase 2: {}'.format(phase2(RULES, TICKETS, YOUR_TICKET)))