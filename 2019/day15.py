from intcode_computer import intcode_computer
from collections import defaultdict
import math
import operator

move = {
    1: lambda x : (x[0], x[1]+1),
    2: lambda x : (x[0], x[1]-1),
    3: lambda x : (x[0]-1, x[1]),
    4: lambda x : (x[0]+1, x[1])
  }

def map_maze(comp):
  maze = defaultdict(lambda:-1)
  position = (0,0)

  def get_direction(p, w):
    """ This method tries to keep the last wall seen on our left 
    V<<
    VW^
    >>^
    """
    angle = (math.atan2(p[1] - w[1], p[0] - w[0])) % (2 * math.pi)
    if angle == 0: return 1 # NORTH
    if angle <= math.pi / 2: return 3 # WEST
    if angle <= math.pi: return 2 # SOUTH
    if angle <= 1.5 * math.pi: return 4 # EAST
    return 1 # NORTH

  last_wall = (-500,0)
  for i in range(5000):
    direction = get_direction(position,last_wall)
    target_pos = move[direction](position)
    comp.input_values.append(direction)
    out = comp.execute().output_values.pop()
    maze[target_pos] = out
    if out == 0: last_wall = target_pos
    else: position = target_pos
    if out == 2: exit_position = target_pos
  return (maze, exit_position)

def find_shortest_path(p_start, p_goal, maze):
  seen = defaultdict(lambda:99999)
  to_open = [p_start]
  seen[p_start] = 0
  while len(to_open) > 0:
    current = to_open.pop()
    for i in range(1,5):
      p = move[i](current)
      if maze[p] > 0 and p not in seen:
        seen[p] = min(seen[p], seen[current] + 1)
        to_open.append(p)
  return seen

def print_maze(maze):
  for y in range(21,-20,-1):
    line = [maze[(x,y)] for x in range(-21,20)]
    print("".join(map(str, line)).replace('-1','.').replace('0','x').replace('1',' '))

if __name__ == "__main__":
  with open('./input/day15') as f:
    comp = intcode_computer([int(i) for i in next(f).split(',')], stop_on_output=True)
    (maze, exit_position) = map_maze(comp)
    # print_maze(maze)
    shortest = find_shortest_path(exit_position, (0,0), maze)
    print(shortest[(0,0)])
    print(max(shortest.iteritems(), key=operator.itemgetter(1))[1])