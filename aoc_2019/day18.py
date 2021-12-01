from collections import defaultdict
from string import ascii_lowercase

move = {
    0: lambda x : (x[0], x[1]+1),
    1: lambda x : (x[0], x[1]-1),
    2: lambda x : (x[0]-1, x[1]),
    3: lambda x : (x[0]+1, x[1]),
    4: lambda x : (x[0]+1, x[1]+1),
    5: lambda x : (x[0]+1, x[1]-1),
    6: lambda x : (x[0]-1, x[1]+1),
    7: lambda x : (x[0]-1, x[1]-1)
  }

def get_type(tile):
  if tile in ['.', '!', '@', '$', '%']: return 'empty'
  if tile == '#': return 'wall'
  if ord(tile) > 96: return 'key'
  return 'door'

class Pathfinder:
  def __init__(self, maze):
    self.maze = maze
    self.paths = {}
    self.compute_paths()
  
  def get_reachable_keys(self, start, opened):
    return [
      k for k in self.paths[start] 
      if set(k[2]).issubset(set(opened)) and k[1].upper() not in opened
    ]

  def get_distances(self, pos):
    """
    Returns the list of keys reachable from the chosen position, in the form:
    (distance to key, key, list of keys required)
    """
    seen = {pos: 0}
    keys = []
    to_open = [(pos, [])]
    while len(to_open) > 0:
      current, required_keys = to_open.pop(0)
      for i in range(4):
        p = move[i](current)
        p_value = self.maze[p[1]][p[0]]
        p_type = get_type(p_value)
        if p_type is not 'wall' and p not in seen:
          seen[p] = seen[current] + 1
          if p_type is 'empty': to_open.append((p, required_keys))
          if p_type is 'door': to_open.append((p, required_keys + [p_value]))
          if p_type is 'key': 
            to_open.append((p, required_keys))
            keys.append((seen[current] + 1, p_value, required_keys))
    return keys

  def compute_paths(self):
    for l in ascii_lowercase:
      pos = find_tile(self.maze, l)
      if pos is None: return
      self.paths[l] = self.get_distances(pos)

def find_tile(maze, tile_id):
  for y, line in enumerate(maze):
    for x, val in enumerate(line):
      if val == tile_id:
        return (x,y)
  return None

def get_shortest_path(maze, start, phase2=False, debug=False):
  finder = Pathfinder(maze)
  finder.paths['@'] = finder.get_distances(start)
  start_keys = []
  if phase2:
    reachable = [k[1] for k in finder.paths['@']]
    for l in ascii_lowercase:
      if l not in reachable: start_keys.append(l.upper())
  shortest = defaultdict(lambda: 999999)
  to_open = [(0, '@', start_keys)]
  goal = 999999
  i = 0
  skipped = 0

  while len(to_open) > 0:
    i += 1
    distance, current, opened = to_open.pop(0)
    keys = finder.get_reachable_keys(current, opened)
    
    if len(keys) == 0: goal = distance
    shortest[frozenset(opened + [current])] = min(shortest[frozenset(opened + [current])], distance)

    filtered = [
      (distance + k[0], k[1], opened + [k[1].upper()]) for k in keys 
      if distance+k[0] < goal and distance + k[0] < shortest[frozenset(opened + [k[1], k[1].upper()])]
    ]
    to_open = filtered + to_open
    skipped += len(keys) - len(filtered)

    if i%10000 == 0 and debug:
      print('goal',goal,'queue',len(to_open),'seen',len(shortest), 'step', i, 'skipped', skipped)
    
  return goal

def phase2(maze):
  center = find_tile(maze, '@')

  new_maze = []
  for idx, line in enumerate(maze):
    if idx == center[1]: new_line = line[:center[0]-1] + '###' + line[center[0]+2:]
    elif abs(idx - center[1]) == 1 : new_line = line[:center[0]-1] + '@#@' + line[center[0]+2:]
    else: new_line = line
    new_maze.append(new_line)
  
  distance = 0
  for i in range(4,8):
    start = move[i](center)
    distance += get_shortest_path(new_maze, start, True)
  return distance

if __name__ == "__main__":
  with open('./input/day18') as f:
    maze = [l.rstrip('\n') for l in f]
    print('Phase 1: {}'.format(get_shortest_path(maze, find_tile(maze, '@'))))
    print('Phase 2: {}'.format(phase2(maze)))