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
    segments = [range(seeds[i], seeds[i]+seeds[i+1]) for i in range(0,len(seeds),2)]

    for mapping in maps:
        segments_next, segments_unchanged = [], []
        for [dest, source, length] in mapping:
            range_map = range(source, source+length)
            for s in segments:
                range_before = range(s.start, min(s.stop, range_map.start)) or None
                range_inter = range(max(s.start,range_map.start), min(s.stop,range_map.stop)) or None
                range_after = range(max(s.start, range_map.stop), s.stop) or None
                if range_before: segments_unchanged.append(range_before)
                if range_after: segments_unchanged.append(range_after)
                if range_inter: segments_next.append(range(range_inter.start+dest-source, range_inter.stop+dest-source))
            segments = segments_unchanged # a segment can only be matched once, so we only recheck the parts that have not yet been matched
            segments_unchanged = []
        segments += segments_next

    return min(s.start for s in segments)


def parse(file):
    blocs = file.split('\n\n')
    seeds = [int(x) for x in blocs[0][7:].split(' ')]
    return seeds, [[[int(x) for x in line.split(' ')] for line in bloc.split('\n')[1:]] for bloc in blocs[1:]]


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/"+Path(__file__).stem).open(encoding="UTF-8") as f:
        DATA = parse(f.read())

        print(f"Phase 1: {part1(*DATA)}")
        print(f"Phase 2: {part2(*DATA)}")
