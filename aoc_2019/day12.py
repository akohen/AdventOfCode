import re
import copy
import math
from functools import reduce 

def update_velocities(moons):
  for moon in moons:
    for moon2 in moons:
      if moon != moon2:
        for i in range(3):
          if moon[0][i] > moon2[0][i]:  moon[1][i] -= 1
          if moon[0][i] < moon2[0][i]: moon[1][i] += 1

def get_energy(moons):
  total = 0
  for moon in moons:
    total += sum(map(abs,moon[0])) * sum(map(abs,moon[1]))
  return total

def simulate(moons, steps=1):
  for i in range(steps):
    update_velocities(moons)
    for moon in moons:
      moon[0] = [sum(x) for x in zip(moon[0],moon[1])]

def lcm(n):
  return reduce(lambda a,b: a*b // math.gcd(a,b), n)

def get_frequencies(moons):
  org = copy.deepcopy(moons)
  freq = [0,0,0]
  count = 0
  while freq.count(0) > 0:
    simulate(moons)
    count += 1
    for i in range(3):
      if [(moon[0][i],moon[1][i]) for moon in moons] == [(moon[0][i],moon[1][i]) for moon in org] and freq[i] == 0:
        freq[i] = count
  return freq

if __name__ == "__main__":
  with open('./input/day12') as f:
    moons = [[list(map(int,re.findall(r'-?\d+',l))),[0,0,0]] for l in f]
    simulate(moons, 1000)
    print(get_energy(moons))
    print(lcm(get_frequencies(moons)))