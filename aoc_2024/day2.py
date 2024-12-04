from pathlib import Path

def is_steps_valid(steps):
    if steps[0] < -3 or steps[-1] > 3: return False
    if steps[0] * steps[-1] < 0: return False
    if steps.count(0) > 0: return False
    return True


def get_steps(report):
    return sorted(report[i+1] - report[i] for i in range(len(report)-1))


def part1(reports):
    reports_steps = [get_steps(report) for report in reports]
    return sum(is_steps_valid(report_steps) for report_steps in reports_steps)


def part2(reports):
    def is_valid(report):
        if is_steps_valid(get_steps(report)):
            return True
        for i in range(len(report)):
            if is_steps_valid(get_steps(report[0:i]+report[i+1:])):
                return True
        return False
    return sum(is_valid(report) for report in reports)


def parse(file):
    return [[int(x) for x in line.split()] for line in file.split('\n')]


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/"+Path(__file__).stem).open(encoding="UTF-8") as f:
        DATA = parse(f.read())

        print(f"Phase 1: {part1(DATA)}")
        print(f"Phase 2: {part2(DATA)}")
