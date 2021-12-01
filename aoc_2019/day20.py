from collections import defaultdict
from string import ascii_uppercase
move = {
    0: lambda x : (x[0], x[1]+1),
    1: lambda x : (x[0], x[1]-1),
    2: lambda x : (x[0]-1, x[1]),
    3: lambda x : (x[0]+1, x[1])
  }

class Maze:
  def __init__(self, data):
    self.data = data
    self.parse()

  @property
  def x(self): return len(data[0])

  @property
  def y(self): return len(data)

  def __call__(self, p):
    if p[0] < 0 or p[1] < 0 or p[0] >= self.x or p[1] >= self.y: return ''
    return self.data[p[1]][p[0]]

  def get_exit(self, point):
    if point not in self.points: return None
    current_point = self.points[point]
    for exit in maze.teleports[current_point]:
      if exit != point: return exit

  def parse(self):
    self.teleports = defaultdict(list)
    self.points = {}
    self.distances = {}
    for y in range(self.y):
      for x in range(self.x):
        char = self((x,y))
        if char in ascii_uppercase:
          if self((x,y+1)) in ascii_uppercase and self((x,y+2)) == '.' : 
            self.teleports[char+self((x,y+1))].append((x,y+2))
            self.points[(x,y+2)] = char+self((x,y+1))
          if self((x,y-1)) in ascii_uppercase and self((x,y-2)) == '.' : 
            self.teleports[self((x,y-1))+char].append((x,y-2))
            self.points[(x,y-2)] = self((x,y-1))+char
          if self((x+1,y)) in ascii_uppercase and self((x+2,y)) == '.' : 
            self.teleports[char+self((x+1,y))].append((x+2,y))
            self.points[(x+2,y)] = char+self((x+1,y))
          if self((x-1,y)) in ascii_uppercase and self((x-2,y)) == '.' : 
            self.teleports[self((x-1,y))+char].append((x-2,y))
            self.points[(x-2,y)] = self((x-1,y))+char

    for k in self.points: # this creates the list of all points reachable for each teleporter entrance/exit
      self.distances[k] = self.get_distances(k)

  def get_distances(self, pos):
    """
    Returns the list of keys reachable from the chosen position, in the form:
    (distance to key, key, list of keys required)
    """
    seen = {pos: 0}
    result = []
    to_open = [pos]
    while len(to_open) > 0:
      current = to_open.pop(0)
      for i in range(4):
        p = move[i](current)
        p_value = self(p)
        if p_value == '.' and p not in seen:
          seen[p] = seen[current] + 1
          to_open.append(p)
          if p in self.points: result.append((p, seen[current] + 1))
    return result

def phase1(maze):
  to_open = [(0, maze.teleports['AA'][0], [])]
  min_distance = 999999999

  while len(to_open) > 0:
    distance, current, seen = to_open.pop(0)
    current_point = maze.points[current]
    if current_point == 'ZZ':
      min_distance = min(distance, min_distance)
      continue
  
    for point, d in maze.distances[current] + [(p,1) for p in maze.teleports[current_point] if p != current]:
      if point not in seen:
        to_open.append((distance + d, point, seen+[current]))
  return min_distance
  
def phase2(maze):
  def is_outer_portal(p):
    if p[1] == 2 or p[1] == 112 or p[0] == 2 or p[0] == 114: return True
    else: return False
  to_open = [(0, (maze.teleports['AA'][0], 0), [])]
  min_distance = 20000
  i = 0

  while len(to_open) > 0:
    i+=1
    distance, current, seen = to_open.pop(0)
    depth = current[1]
    if i%100000 == 0 : print(i,len(to_open), min_distance,depth,len(seen))
    if depth < 0 or depth > 50 or distance > min_distance: continue
  
    for point, d in maze.distances[current[0]]:
      if maze.points[point] == 'ZZ' and depth == 0:
        min_distance = min(distance + d, min_distance)
        continue
      if distance + d > min_distance: continue
      point_exit = maze.get_exit(point)
      if point_exit is None: continue
      if is_outer_portal(point) == False:
        if (point_exit, depth+1) not in seen:
          to_open.append((distance + d + 1, (point_exit, depth+1), seen+[current]))
      elif depth > 0 and (point_exit, depth-1) not in seen:
        to_open.append((distance + d + 1, (point_exit, depth-1), seen+[current]))
      
  return min_distance

if __name__ == "__main__":
  with open('./input/day20') as f:
    data = [l.rstrip('\n') for l in f]
    maze = Maze(data)
    print(phase1(Maze(data)))
    print(phase2(Maze(data)))
