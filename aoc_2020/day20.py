from pathlib import Path
import sys
from collections import defaultdict, deque

TEST_MODE = bool(len(sys.argv) > 1 and sys.argv[1] == "test")


def phase1(data):
    total = 1
    for tile in data:
        if data[tile]["adjacent"].count(None) == 2:
            total *= tile
    return total

def phase2(data):
    return 2

def rotate_tile(tile):
    rotated = []
    for x in range(len(tile)-1,-1,-1):
        rotated.append("".join([tile[y][x] for y in range(len(tile))]))
    return rotated

def display_tile(tile):
    for line in tile:
        print(line)

def get_edge(tile):
    """
    Returns the binary sum of the top of the tile
    """
    total, flipped = 0, 0
    for i, value in enumerate(tile[0]):
        total += 2 ** i if value == "#" else 0
    for i, value in enumerate(tile[0][::-1]):
        flipped += 2 ** i if value == "#" else 0
    return total, flipped

def get_adjacent(edges, tile, edge):
    for tile_id in edges[edge]:
        if tile_id != tile:
            return tile_id
    return None

def load(data):
    tiles = {}
    edges = defaultdict(list)
    for tile_raw in data:
        tile_id = int(tile_raw[0][5:9])
        tile_data = tile_raw[1:]
        tile_edges = deque()
        current = tile_data
        for _ in range(4):
            current_edge = min(get_edge(current))
            tile_edges.append(current_edge)
            current = rotate_tile(current)
            edges[current_edge].append(tile_id)
        tiles[tile_id] = {"data": tile_data, "edges": tile_edges}
    
    seen = []
    to_open = [(tile_id, current_edge, 0)]
    while len(to_open) > 0:
        tile_id, edge, position = to_open.pop()
        tile = tiles[tile_id]
        seen.append(tile_id)
        shift = position - tile["edges"].index(edge) + 2
        tile["edges"].rotate(shift)
        tile["shift"] = shift
        tile["adjacent"] = []
        for i, edge in enumerate(tile["edges"]):
            new_tile = get_adjacent(edges, tile_id, edge)
            tile["adjacent"].append(new_tile)
            if new_tile and new_tile not in seen:
                to_open.append((new_tile, edge, i))
    return tiles, edges

if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/day20_sample" if TEST_MODE else "input/day20").open() as f:
        DATA, EDGES = load([line.split("\n") for line in f.read().split("\n\n")])

        print(f'Phase 1: {phase1(DATA)}')
        #print(f'Phase 2: {phase2(DATA)}')