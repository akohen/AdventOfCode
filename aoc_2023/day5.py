from pathlib import Path

def part1(seeds, maps):
    results = []
    for current in seeds:
        for mapping in maps:
            for [dest, source, length] in mapping:
                if current in range(source,source+length):
                    current += dest-source
                    break
        results.append(current)
    return min(results)


def part2(seeds, maps):
    segments = [[seeds[i], seeds[i]+seeds[i+1]-1] for i in range(0,len(seeds),2)]

    for mapping in maps:
        segments_next, segments_unchanged = [], []
        for [dest, source, length] in mapping:
            for s in segments:
                if s[1] < source or s[0] >= source+length: # no intersection
                    segments_unchanged.append(s)
                else: # at least part of the segment matches
                    if s[0] < source: # before the intersection
                        segments_unchanged.append([s[0], source-1])
                    if s[1] > source+length-1: # after the intersection
                        segments_unchanged.append([source+length, s[1]])
                    start = max(source, s[0])
                    end = min(s[1], source+length-1)
                    segments_next.append([start+dest-source, end+dest-source])
            segments = segments_unchanged # a segment can only be matched once, so we only recheck the parts that have not yet been matched
            segments_unchanged = []
        segments += segments_next

    return min(list(zip(*segments))[0])


def parse(file):
    blocs = file.split('\n\n')
    seeds = [int(x) for x in blocs[0][7:].split(' ')]
    return seeds, [[[int(x) for x in line.split(' ')] for line in bloc.split('\n')[1:]] for bloc in blocs[1:]]


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/"+Path(__file__).stem).open(encoding="UTF-8") as f:
        DATA = parse(f.read())

        print(f"Phase 1: {part1(*DATA)}")
        print(f"Phase 2: {part2(*DATA)}")
