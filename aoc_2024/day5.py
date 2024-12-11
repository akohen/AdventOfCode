from pathlib import Path


def is_valid(rules, update):
    for rule in rules:
        if rule[0] in update and rule[1] in update \
            and update.index(rule[0]) > update.index(rule[1]):
            return False
    return True


def part1(rules, updates):
    return sum(
        update[len(update) // 2]
        for update in updates
        if is_valid(rules, update)
    )


def part2(rules, updates):
    incorrect_updates = [
        update
        for update in updates
        if not is_valid(rules, update)
    ]

    for update in incorrect_updates:
        while not is_valid(rules, update):
            for a,b in rules:
                if a not in update or b not in update:
                    continue
                if update.index(a) > update.index(b):
                    update[update.index(a)], update[update.index(b)] = b,a

    return sum(update[len(update) // 2] for update in incorrect_updates)


def parse(file):
    rules, updates = file.split('\n\n')
    return [
        [[int(page) for page in rule.split('|')] for rule in rules.split('\n')],
        [[int(page) for page in update.split(',')] for update in updates.split('\n')]
    ]


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/"+Path(__file__).stem).open(encoding="UTF-8") as f:
        DATA = parse(f.read())

        print(f"Phase 1: {part1(*DATA)}")
        print(f"Phase 2: {part2(*DATA)}")
