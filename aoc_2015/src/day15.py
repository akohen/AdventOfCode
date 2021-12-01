from pathlib import Path


def phase1(ingredients):
    total = 100
    best, best2, c = 0, 0, [0,0,0,0]
    for c[0] in range(total):
        for c[1] in range(total-c[0]):
            for c[2] in range(total-c[1]-c[0]):
                c[3] = total-c[2]-c[1]-c[0]
                score = 1
                for i in range(4):
                    score = score * max(0, sum([c[j]*ingredients[j][i] for j in range(4)]))
                best = max(best,score)
                if sum([c[j]*ingredients[j][4] for j in range(4)]) == 500:
                    best2 = max(best2,score)
    return best, best2


def parse(text):
    return [
        [int(i.rstrip(',')) for i in r[2::2]]
        for r in [line.rstrip().split(' ') for line in text]
    ]


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("../input/day15").open(encoding="UTF-8") as f:
        INGREDIENTS = parse(f)

        print(phase1(INGREDIENTS))
