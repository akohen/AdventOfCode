from pathlib import Path
from collections import deque

def phase1(data, _, distances):
    best, to_open = 0, deque([(0, 'AA', [], 30)])

    while len(to_open) > 0:
        total, pos, seen, time = to_open.pop()
        valves_to_see = [v for v in sorted(distances[pos], key=distances[pos].get) if v not in seen and distances[pos][v] < time - 1]
        best_possible = total + sum(data[v]['flow']*(time-1-distances[pos][v]) for v in valves_to_see)
        if best_possible > best:
            for valve in valves_to_see:
                time_left = time - distances[pos][valve] - 1
                next_state = [total + time_left * data[valve]['flow'], valve, seen + [valve], time_left]
                to_open.appendleft(next_state)
                if total + time_left * data[valve]['flow'] > best:
                    best = total + time_left * data[valve]['flow']
    return best


def phase2(data, valves_with_flow, distances):
    results, to_open = [], deque([(0, 'AA', [], 26)])

    while len(to_open) > 0:
        total, pos, seen, time = to_open.pop()
        valves_to_see = (v for v in sorted(distances[pos], key=distances[pos].get) if v not in seen and distances[pos][v] < time - 1)
        for valve in valves_to_see:
            time_left = time - distances[pos][valve] - 1
            next_state = [total + time_left * data[valve]['flow'], valve, seen + [valve], time_left]
            to_open.appendleft(next_state)
            if len(seen) > len(valves_with_flow)//2 - 4 and len(seen) < 4+len(valves_with_flow)//2:
                results.append(next_state)

    best = 0
    sorted_results = sorted(results,key=lambda x:x[0], reverse=True)
    for a in sorted_results:
        for b in sorted_results:
            if len(set(a[2]).intersection(b[2])) == 0:
                best = max(a[0] + b[0], best)
                break
            if a[0] + b[0] < best:
                break
    return best


def parse(file):
    data = {
        line[6:8]: {'flow': int(line[23:line.index(';')]), 'tunnels': [v[-2:] for v in line[42:].split(',')]}
        for line in file.split('\n')}

    def get_path(start, end):
        to_open = deque([(start,[])])
        while len(to_open) > 0:
            curr = to_open.popleft()
            if curr[0] == end:
                return curr[1]
            for tunnel in data[curr[0]]['tunnels']:
                if tunnel not in curr[1]:
                    to_open.append((tunnel, curr[1] + [tunnel]))

    valves_with_flow = [v for v in data if data[v]['flow'] > 0]

    distances = {a:
        {b : len(get_path(a,b)) for b in valves_with_flow if a != b}
        for a in valves_with_flow + ['AA']
    }

    return data, valves_with_flow, distances


if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/"+Path(__file__).stem).open(encoding="UTF-8") as f:
        DATA = parse(f.read())

        print(f"Phase 1: {phase1(*DATA)}")
        print(f"Phase 2: {phase2(*DATA)}")
