from pathlib import Path

def neighbors(l,x,y):
    total = 0
    if x > 0:
        total += l[x-1][max(0,y-1):min(len(l),y+2)].count('#')
    total += l[x][max(0,y-1):min(len(l),y+2)].count('#')
    if x < len(l)-1:
        total += l[x+1][max(0,y-1):min(len(l),y+2)].count('#')
    return total

def is_on(lights, x, y):
    n = neighbors(lights, x, y)
    if n == 3:
        return True
    if n == 4 and lights[x][y] == '#':
        return True
    return False

def phase1(lights, steps):
    for i in range(steps):
        lights = [
            ''.join(
                '#' if is_on(lights, i, j) else '.'
                for j in range(len(lights))
            )
            for i in range(len(lights))
        ]
    
    return sum([l.count('#') for l in lights])


def phase2(lights, steps):
    lights[0] = '#'+lights[0][1:-1]+'#'
    lights[-1] = '#'+lights[-1][1:-1]+'#'
    for i in range(steps):
        lights = [
            ''.join(
                '#' if is_on(lights, i, j) else '.'
                for j in range(len(lights))
            )
            for i in range(len(lights))
        ]
        lights[0] = '#'+lights[0][1:-1]+'#'
        lights[-1] = '#'+lights[-1][1:-1]+'#'
    
    return sum([l.count('#') for l in lights])


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("../input/day18").open(encoding="UTF-8") as f:
        LIGHTS = [line.rstrip() for line in f]

        print(f"Phase 1: {phase1(LIGHTS, 100)}")
        print(f"Phase 2: {phase2(LIGHTS, 100)}")
