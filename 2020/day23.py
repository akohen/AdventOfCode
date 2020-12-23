import sys
TEST_MODE = bool(len(sys.argv) > 1 and sys.argv[1] == "test")


def phase1(data, steps=10):
    for step in range(steps):
        destination = data[0] - 1 or 9
        while destination in data[1:4]:
            destination = destination - 1 or 9
        index = data.index(destination) + 1
        data = data[4:index] + data[1:4] + data[index:9] + [data[0]]

    return "".join([str(i) for i in data[data.index(1)+1:]+data[:data.index(1)]])

def phase2(data):
    data = data + [10]
    # cups[x] returns the next clockwise cup from cup X
    cups = [-1] + [data[data.index(i) + 1] for i in range(1, 10)] + list(range(11,1000001)) + [data[0]]
    current = data[0]
    for step in range(10000000):
        val, pickup = current, []
        for _ in range(3):
            val = cups[val]
            pickup += [val]
        destination = current - 1 or 1000000
        while destination in pickup:
            destination = destination - 1 or 1000000
        rest = cups[destination]
        next_val = cups[val]
        cups[destination] = cups[current]
        cups[val] = rest
        cups[current] = next_val
        current = next_val
        if step%10000==0: print(str(step/100000)+"%", end="\r")
    return cups[1] * cups[cups[1]]

def load(data):
    return [int(i) for i in data]

if __name__ == "__main__":
    DATA = load("389125467" if TEST_MODE else "247819356")

    print('Phase 1: {}'.format(phase1(DATA,100)))
    print('Phase 2: {}'.format(phase2(DATA)))