from pathlib import Path


def phase1(reindeers, seconds):
    return max([
        seconds//r['cycle'] * r['active'] * r['speed'] + min(r['active'],seconds%r['cycle'])*r['speed']
        for r in reindeers
    ])


def phase2(reindeers, seconds):
    for t in range(seconds):
        for r in reindeers:
            if t % r['cycle'] < r['active']:
                r['dist'] += r['speed']
        best = max([r['dist'] for r in reindeers])
        for r in reindeers:
            if r['dist'] == best:
                r['score'] += 1
    return max([r['score'] for r in reindeers])


def parse(text):
    return [
        {"speed": int(r[3]), "active": int(r[6]), "cycle": int(r[6])+int(r[-2]), "dist": 0, "score": 0}
        for r in [line.split(' ') for line in text]
    ]


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("../input/day14").open(encoding="UTF-8") as f:
        REINDEERS = parse(f)

        print(f"Phase 1: {phase1(REINDEERS, 2503)}")
        print(f"Phase 2: {phase2(REINDEERS, 2503)}")
