from pathlib import Path
from collections import deque
from itertools import islice
import sys

TEST_MODE = bool(len(sys.argv) > 1 and sys.argv[1] == "test")

def get_score(p1, p2):
    winner, total = p1 if len(p2) == 0 else p2, 0
    for index, card in enumerate(winner):
        total += card * (len(winner) - index)
    return total

def phase1(players):
    while len(players[0]) != 0 and len(players[1]) != 0:
        c = players[0].popleft(), players[1].popleft()
        winner = 0 if c[0] > c[1] else 1
        players[winner] += [c[winner],c[winner^1]]
    return get_score(*players)

def hash(players):
    value = ""
    for card in players[0]:
        value += str(card) + ","
    value += ';'
    for card in players[1]:
        value += str(card) + ","
    return value

def recursive_combat(players):
    history = []
    while len(players[0]) != 0 and len(players[1]) != 0:
        round_hash = hash(players)
        if round_hash in history:
            return 0,0,0
        else:
            history.append(round_hash)
        c = players[0].popleft(), players[1].popleft()
        if c[0] <= len(players[0]) and c[1] <= len(players[1]):
            winner = recursive_combat(
                [deque(islice(players[0],0,c[0])), 
                deque(islice(players[1],0,c[1]))]
            )[0]
        else:
            winner = 0 if c[0] > c[1] else 1
        players[winner] += [c[winner],c[winner^1]]
    return winner, players

def phase2(players):
    _, players = recursive_combat(players)
    return get_score(*players)

def load(data):
    return deque([int(card) for card in data[1:]])

if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/day22_sample" if TEST_MODE else "input/day22").open() as f:
        P1, P2 = [load(line.split("\n")) for line in f.read().split("\n\n")]

        print('Phase 1: {}'.format(phase1([P1.copy(), P2.copy()])))
        print('Phase 2: {}'.format(phase2([P1, P2])))