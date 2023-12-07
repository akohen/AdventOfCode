from pathlib import Path
from collections import Counter

STEP = 16

def part1(hands):
    def score_hand(hand):
        card_order_value = sum(card*(STEP**i) for i, card in enumerate(reversed(hand)))
        top = Counter(sorted(hand, reverse=True)).most_common(2) # [(card, count), ..]
        
        if top[0][1] == 5:
            return 7*STEP**5 + card_order_value
        if top[0][1] == 4:
            return 6*STEP**5 + card_order_value
        if top[0][1] == 3 and top[1][1] == 2:
            return 5*STEP**5 + card_order_value
        if top[0][1] == 3:
            return 4*STEP**5 + card_order_value
        if top[0][1] == 2 and top[1][1] == 2:
            return 3*STEP**5 + card_order_value
        if top[0][1] == 2:
            return 2*STEP**5 + card_order_value
        return card_order_value
    
    hands_scored = sorted((score_hand(hand[0]), hand[1]) for hand in hands)
    return sum(i*score for i, (_, score) in enumerate(hands_scored, 1))


def part2(hands):
    def score_hand(hand):
        card_order_value = sum(card*(STEP**i) for i, card in enumerate(reversed(hand)))
        counts = Counter(sorted(hand, reverse=True))
        jokers, counts[0]  = counts[0], 0 # Jokers cannot make a combination by themselves
        top = counts.most_common(2) # [(card, count), ..]
        
        if top[0][1] + jokers == 5:
            return 7*STEP**5 + card_order_value
        if top[0][1] + jokers  == 4:
            return 6*STEP**5 + card_order_value
        if top[0][1] + jokers  == 3 and top[1][1] == 2:
            return 5*STEP**5 + card_order_value
        if top[0][1] + jokers  == 3:
            return 4*STEP**5 + card_order_value
        if top[0][1] == 2 and top[1][1]  == 2:
            return 3*STEP**5 + card_order_value
        if top[0][1] + jokers  == 2:
            return 2*STEP**5 + card_order_value
        return card_order_value
    
    hands_scored = sorted((score_hand(hand[0]), hand[1]) for hand in hands)
    return sum(i*score for i, (_, score) in enumerate(hands_scored, 1))


def parse(file):
    CARDS = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    return [[[CARDS.index(x) for x in hand[0]], int(hand[1])] for line in file.split('\n') if (hand := line.split(' '))]

def parse2(file):
    CARDS = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']
    return [[[CARDS.index(x) for x in hand[0]], int(hand[1])] for line in file.split('\n') if (hand := line.split(' '))]


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/"+Path(__file__).stem).open(encoding="UTF-8") as f:
        DATA = f.read()

        print(f"Phase 1: {part1(parse(DATA))}")
        print(f"Phase 2: {part2(parse2(DATA))}")
