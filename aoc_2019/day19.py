from intcode_computer import intcode_computer

def scan_beam(program):
  count = 0
  
  x, y, xmin, xmax, new_line = 0,0,0,10,True
  while y < 50:
    out = intcode_computer(program, [x,y]).execute().output()
    if out == 1:
      if new_line: xmin = x
      x += 1
      new_line = False
      count += 1
      xmax = x+1
    elif (new_line and x < xmax):
      x += 1
    else:
      y += 1
      x = xmin
      new_line = True

  return count

def phase2(program):
  def check_square(x,y):
    return intcode_computer(program, [x+99,y-99]).execute().output() == 1
  
  x, y, xmin, xmax, new_line = 0, 400, 0, 500, True
  while True:
    out = intcode_computer(program, [x,y]).execute().output()
    if out == 1:
      if check_square(x,y): return x * 10000 + y-99
      y += 1
      xmin = x
      xmax = x+2
    elif (new_line and x < xmax):
      x += 1
    else:
      y += 1
      x = xmin
      new_line = True

if __name__ == "__main__":
  with open('./input/day19') as f:
    program = [int(i) for i in next(f).split(',')]
    print(scan_beam(program))
    print(phase2(program))