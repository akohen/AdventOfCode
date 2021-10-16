from pathlib import Path


def day8(strings):
    total, chars, part2 = 0,0,0
    for str in strings:
        total += len(str)
        i = 0
        while i < len(str):
            if str[i] != '"':
                chars += 1
            else:
                part2 += 2
            if str[i] == '\\':
                if str[i+1]  == '\\' or str[i+1] == '"':
                    i+=1
                    part2 += 2
                elif str[i+1] == "x":
                    i+=3
                    part2 +=1
            i+=1
    return total - chars, part2

if __name__ == "__main__":
    with Path(__file__).parent.joinpath("../input/day8").open(encoding="UTF-8") as f:
        STRINGS = [line.rstrip() for line in f]

        print("Phase 1: {}\nPhase 2: {}".format(*day8(STRINGS)))
