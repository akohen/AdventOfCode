from collections import deque

def phase1(players, rounds):
    marbles = deque([0])
    scores = [0] * players
    for i in range(1, rounds+1):
        if i % 23 == 0:
            marbles.rotate(7)
            scores[i%len(scores)] += i + marbles.pop()
            marbles.rotate(-1)
        else:
            marbles.rotate(-1)
            marbles.append(i)
    return max(scores)

if __name__ == "__main__":        
    print('Phase 1: {}'.format(phase1(486,70833)))
    print('Phase 1: {}'.format(phase1(486,7083300)))
