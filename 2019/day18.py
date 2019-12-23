move = {
    0: lambda x : (x[0], x[1]+1),
    1: lambda x : (x[0], x[1]-1),
    2: lambda x : (x[0]-1, x[1]),
    3: lambda x : (x[0]+1, x[1])
  }

def is_crossable(tile):
  return tile == '.' or ord(tile) > 96

def get_type(tile):
  if tile == '.' or tile == '@': return 'empty'
  if tile == '#': return 'wall'
  if ord(tile) > 96: return 'key'
  return 'door'

def get_distances(maze, p_start, opened=[]):
  seen = {p_start:0}
  keys = {}
  to_open = [p_start]
  while len(to_open) > 0:
    current = to_open.pop(0)
    for i in range(4):
      p = move[i](current)
      p_value = maze[p[1]][p[0]]
      p_type = get_type(p_value)
      if p_type is not 'wall' and p not in seen:
        seen[p] = seen[current] + 1
        if p_type is 'empty': to_open.append(p)
        if p_value.upper() in opened: to_open.append(p)
        if p_type is 'key' and p_value.upper() not in opened: keys[p_value] = p,seen[current] + 1
  return keys

def find_tile(maze, tile_id):
  for y, line in enumerate(maze):
    for x, val in enumerate(line):
      if val == tile_id:
        return (x,y)
  return None

shortest = float('inf')
def get_shortest_path(maze, start, distance=0, opened=[]):
  global shortest
  if distance > shortest: return float('inf')

  keys = get_distances(maze, start, opened)
  print(opened, keys, distance, shortest)
  sub_distances = []
  if len(keys) == 0: 
    shortest = min(shortest, distance)
    return distance
  for key in keys:
    if key.upper() in opened: continue
    sub_distances.append( get_shortest_path(maze, keys[key][0], distance + keys[key][1], opened + [key.upper()]) )
  return min(sub_distances)

if __name__ == "__main__":
  with open('./input/test') as f:
    maze = [l.rstrip('\n') for l in f]
    print(get_shortest_path(maze, find_tile(maze,'@')))