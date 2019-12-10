import math

def get_asteroids(map):
  asteroids = []
  for i in range(len(map)):
    for j in range(len(map[i])):
      if map[i][j] == '#':
        asteroids.append((j,i))
  return asteroids

def get_angle(point, reference):
  return (math.atan2(point[0] - reference[0], reference[1] - point[1])) % (2 * math.pi)

def get_distance(point, reference):
  return math.hypot(reference[1] - point[1], reference[0] - point[0])

def select_spot(asteroids):
  max_count = 0
  for i in range(len(asteroids)):
    count = len(set([get_angle(a, asteroids[i]) for a in asteroids]))
    if count > max_count:
      max_count = count
      max_asteroid = i
  return max_count, max_asteroid

def find_order(asteroids, ref):
  angles = sorted([(get_angle(a, ref), get_distance(a, ref), a) for a in asteroids if a is not ref])
  seen = [angles.pop(0)]
  i = 0
  while len(seen) < 200:
    if angles[i][0] != seen[-1][0]:
      seen.append(angles.pop(i))
    else: i = i+1
    i = i % len(angles)
  return seen[-1][2][0] * 100 + seen[-1][2][1]

if __name__ == "__main__":
  with open('./input/day10') as f:
    map = [line.rstrip('\n') for line in f]
    asteroids = get_asteroids(map)
    seen,laser = select_spot(asteroids)
    res = find_order(asteroids,asteroids[laser])
    print('Phase 1: {}\nPhase 2: {}'.format(seen, res))
    