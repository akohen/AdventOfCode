from pathlib import Path

def phase1(segments):
    count = 0
    for line in segments:
        for digit in line[1]:
            if len(digit) in (2,3,4,7):
                count+=1
    return count


def phase2(segments):
    count = 0
    for line in segments:
        numbers = [0]*10
        #1,4,7,9
        for digit in line[0]:
            if len(digit) == 2:
                numbers[1] = digit
            elif len(digit) == 3:
                numbers[7] = digit
            elif len(digit) == 4:
                numbers[4] = digit
            elif len(digit) == 7:
                numbers[8] = digit
        bd = numbers[4] - numbers[1]

        for digit in line[0]:
            #0,6,9
            if len(digit) == 6 and len(bd - digit) == 1:
                numbers[0] = digit
            elif len(digit) == 6 and len(numbers[1] - digit) == 0:
                numbers[9] = digit
            elif len(digit) == 6:
                numbers[6] = digit
            #2,3,5
            elif len(digit) == 5 and len(bd - digit) ==0:
                numbers[5] = digit
            elif len(digit) == 5 and len(numbers[1] - digit) == 1:
                numbers[2] = digit
            elif len(digit) == 5:
                numbers[3] = digit

        for i, num in enumerate(line[1]):
            count += 10**(3-i) * numbers.index(num)
    return count


def parse(file):
    return [[[set(x) for x in part.split(' ')] for part in line.split(' | ')] for line in file.split('\n')]

if __name__ == "__main__":
    with Path(__file__).parent.joinpath("../input/"+Path(__file__).stem).open(encoding="UTF-8") as f:
        SEGMENTS = parse(f.read())

        print(f"Phase 1: {phase1(SEGMENTS)}")
        print(f"Phase 2: {phase2(SEGMENTS)}")
