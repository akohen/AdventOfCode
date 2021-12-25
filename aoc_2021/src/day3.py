from pathlib import Path

def phase1(numbers):
    counts = [0] * len(numbers[0])
    for num in numbers:
        for i,n in enumerate(num):
            counts[i] += int(n)
    gamma = int(''.join(['1' if i > len(numbers)/2 else '0' for i in counts]),2)
    epsilon = int(''.join(['0' if i > len(numbers)/2 else '1' for i in counts]),2)
    return gamma * epsilon

def rating(numbers, type='oxygen', bit=0):
    if len(numbers) == 1:
        return numbers[0]
    
    count, num0, num1 = 0, [], []
    for num in numbers:
        if num[bit] == '1':
            count = count + 1
            num1.append(num)
        else:
            num0.append(num)
    if type == 'co2':
        num0, num1 = num1, num0
    if count >= len(numbers) / 2:
        return rating(num1, type, bit+1)
    else:
        return rating(num0, type, bit+1)

def phase2(numbers):
    return int(rating(numbers),2) * int(rating(numbers, 'co2'),2)

def parse(file):
    return file.splitlines()

if __name__ == "__main__":
    with Path(__file__).parent.joinpath("../input/"+Path(__file__).stem).open(encoding="UTF-8") as f:
        VALUES = parse(f.read())

        print(f"Phase 1: {phase1(VALUES)}")
        print(f"Phase 2: {phase2(VALUES)}")
