from pathlib import Path

def is_winning(board):
    for step in [[25, 5, 1], [5, 1, 5]]:
        for i in range(0, step[0], step[1]):
            for j in range(5):
                if board[i+(j*step[2])] >= 0:
                    break
            else:
                return True
    return False

def phase1(numbers, boards):
    for n in numbers:
        for board in boards:
            if n in board:
                board[board.index(n)] = -1
                if is_winning(board):
                    return sum([x for x in board if x > 0]) * n
    return False

def phase2(numbers, boards):
    won = []
    for n in numbers:
        for i, board in enumerate(boards):
            if n in board:
                board[board.index(n)] = -1
                if is_winning(board):
                    if i not in won:
                        won.append(i)
            if len(won) == len(boards):
                return sum([x for x in boards[won[-1]] if x > 0])* n
    return False

def parse(file):
    numbers, *boards = file.split('\n\n')
    return [int(x) for x in numbers.split(',')], [[int(x) for line in b.split('\n') for x in line.split()] for b in boards]

if __name__ == "__main__":
    with Path(__file__).parent.joinpath("../input/"+Path(__file__).stem).open(encoding="UTF-8") as f:
        NUMBERS, BOARDS = parse(f.read())

        print(f"Phase 1: {phase1(NUMBERS, BOARDS)}")
        print(f"Phase 2: {phase2(NUMBERS, BOARDS)}")
