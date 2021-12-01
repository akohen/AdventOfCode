import math 

def get_fuel(mass):
  return math.floor(mass/3) - 2

def get_fuel_for_module(module):
  mass = get_fuel(module)
  if mass < 0:
    return 0
  return mass + get_fuel_for_module(mass)
  
if __name__ == "__main__":
  sum_1 = 0
  sum_2 = 0
  for line in open('./input/day1'):
    sum_1 += get_fuel(int(line))
    sum_2 += get_fuel_for_module(int(line))
  print('Puzzle 1 {:0.0f} - Puzzle 2 {:0.0f}'.format(sum_1, sum_2))