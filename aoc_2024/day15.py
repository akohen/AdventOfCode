from pathlib import Path


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])

def part1(initial_board, instructions):
    board, robot = {}, (-1,-1)
    for pos, char in initial_board.items():
        if char == '@':
            robot = pos
        else:
            board[pos] = char

    for move in instructions:
        next_pos = add(robot, move)
        if not board.get(next_pos):
            robot = next_pos
        elif board.get(next_pos) == 'O':
            end_pos = add(next_pos, move)
            while board.get(end_pos) and board.get(end_pos) == 'O':
                end_pos = add(end_pos, move)
            if not board.get(end_pos):
                robot = next_pos
                board.pop(next_pos)
                board[end_pos] = 'O'

    return sum(100*y + x for (x,y), char in board.items() if char == 'O')

def part2(initial_board, instructions):
    board, robot = {}, (-1,-1)

    def do_move(pos, direction, confirm=False):
        char = board.get(pos)
        next_pos = add(pos, direction)
        next_char = board.get(next_pos)
        if not next_char:
            if confirm:
                board.pop(pos)
                board[next_pos] = char
            return True
        elif next_char == '#':
            return False
        elif direction == (1,0) or direction == (-1,0): # Horizontal move
            # Check the other half of the box
            if do_move(add(next_pos, direction), direction):
                if confirm:
                    do_move(add(next_pos, direction), direction, True)
                    do_move(next_pos, direction, True)
                    do_move(pos, direction, True)
                return True
            return False
        else: # Vertical move
            offset = add(next_pos, (-1,0) if next_char == ']' else (1,0))
            # Check both halves of the box
            if do_move(next_pos, direction) and do_move(offset, direction):
                if confirm:
                    do_move(next_pos, direction, True)
                    do_move(offset, direction, True)
                    do_move(pos, direction, True)
                return True

        return False

    for (x, y), char in initial_board.items():
        if char == '@':
            robot = (2*x, y)
            board[(2*x, y)] = char
        elif char == '#':
            board[(2*x, y)] = char
            board[(2*x+1, y)] = char
        else:
            board[(2*x, y)] = '['
            board[(2*x+1, y)] = ']'

    for move in instructions:
        if do_move(robot, move, True):
            robot = add(robot, move)
    return sum(100*y + x for (x,y), char in board.items() if char == '[')


def parse(file):
    DIRECTIONS = {
        '>': (1, 0),
        '<': (-1, 0),
        '^': (0, -1),
        'v': (0, 1),
    }
    raw_board, raw_instructions = file.split('\n\n')
    board = {
        (x, y): char
        for y, line in enumerate(raw_board.split('\n'))
        for x, char in enumerate(line)
        if char != '.'
    }
    instructions = [DIRECTIONS[char] for char in raw_instructions.replace('\n', '')]
    return board, instructions


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/"+Path(__file__).stem).open(encoding="UTF-8") as f:
        DATA = parse(f.read())

        print(f"Phase 1: {part1(*DATA)}")
        print(f"Phase 2: {part2(*DATA)}")
