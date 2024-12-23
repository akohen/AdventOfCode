from pathlib import Path

def part1(data):
    total = 0
    cursor, left, right = 0, 0, len(data) - 1
    while left <= right:
        if left%2 == 0:
            block_id = left//2
            block_length = data[left]
            disk_space = data[left]
            left += 1
        else:
            block_id = right//2
            if disk_space == 0:
                disk_space = data[left]
            if block_length == 0:
                block_length = data[right]
            if disk_space > block_length:
                right -= 2
            else:
                data[right] -= disk_space
                left += 1
        while block_length > 0 and disk_space > 0:
            block_length -= 1
            disk_space -= 1
            total += cursor * block_id
            cursor += 1
    return total


def part2(data):
    disk = [
        (i//2 if i%2==0 else -1, file)
        for i, file in enumerate(data)
    ]

    result, cursor = 0, len(disk)-1
    while cursor > 0:
        move_id, move_length = disk[cursor]
        cursor -= 1
        if move_id == -1:
            continue
        for i, (block_id, block_length) in enumerate(disk):
            if block_id == move_id:
                break
            if block_id > -1:
                continue
            if block_length >= move_length:
                disk[cursor+1] = (-1, move_length)
                disk[i] = (move_id, move_length)
                if block_length >= move_length:
                    disk = disk[:i+1] + [(-1, block_length - move_length)] + disk[i+1:]
                    cursor += 1
                break
    
    for (block_id, block_length) in disk:
        for i in range(block_length):
            if block_id > -1:
                result += cursor * block_id
            cursor += 1
    return result


def parse(file):
    return [int(x) for x in file]


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/"+Path(__file__).stem).open(encoding="UTF-8") as f:
        DATA = parse(f.read())

        print(f"Phase 1: {part1(DATA.copy())}")
        print(f"Phase 2: {part2(DATA)}")
