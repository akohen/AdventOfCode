def string_to_segments(string):
  x = 0
  y = 0
  segments = []
  for move in string.split(','):
    (direction, distance) = (move[0], int(move[1:]))
    new_point = [(x,y)]
    if direction == 'U':
      y += distance
    elif direction == 'D':
      y -= distance
    elif direction == 'L':
      x -= distance
    elif direction == 'R':
      x += distance
    new_point.append((x,y))
    segments.append(new_point)
  return segments

def get_intersection(line1, line2):
  def check(line1, line2):
    if (line2[0][0] >= min(line1[0][0],line1[1][0]) # This assumes line1 is horizontal and line2 vertical
        and line2[0][0] <= max(line1[0][0],line1[1][0])
        and line1[0][1] >= min(line2[0][1],line2[1][1]) 
        and line1[0][1] <= max(line2[0][1],line2[1][1])):
      return (line2[0][0],line1[0][1])
  if (col := check(line1, line2)):
    return col
  elif (col := check(line2, line1)):
    return col

def get_intersections(segments1, segments2):
  collisions = []
  for line1 in segments1:
    for line2 in segments2:
      if (col := get_intersection(line1, line2)):
        collisions.append(col)

  return collisions[1:] # remove (0,0) from the list

def get_manhattan_distance(a, b):
  x = abs(b[0]-a[0])
  y = abs(b[1]-a[1])
  return max(x,y)

def get_closest_intersection(intersections):
  distance = float("inf")
  for point in intersections:
    distance = min(distance, get_manhattan_distance((0,0), point))
  return distance

def steps_to_intersection(point, wire):
  steps = 0
  for line in wire:
    if not get_intersection([point, point], line):
      steps += get_manhattan_distance(line[0], line[1])
    else:
      steps += get_manhattan_distance(line[0], point)
      return steps

def get_intersection_with_fewest_steps(intersections, wire_1, wire_2):
  distance = float("inf")
  for point in intersections:
    distance = min(distance, steps_to_intersection(point, wire_1) + steps_to_intersection(point, wire_2))
  return distance

if __name__ == "__main__":
  with open('./input/day3') as f:
    wire_1 = string_to_segments(next(f))
    wire_2 = string_to_segments(next(f))
    intersections = get_intersections(wire_1, wire_2)
    print('Closest intersection: {}'.format(get_closest_intersection(intersections)))
  print('Fewest steps to intersection: {}'.format(get_intersection_with_fewest_steps(intersections, wire_1, wire_2)))