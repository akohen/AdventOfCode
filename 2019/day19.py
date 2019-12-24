from intcode_computer import intcode_computer

def scan_beam(program):
  count = 0
  for x in range(50):
    for y in range(50):
      out = intcode_computer(program, [x,y]).execute().output()
      if out == 1: count += 1
  print(count)

if __name__ == "__main__":
  with open('./input/day19') as f:
    program = [int(i) for i in next(f).split(',')]
    comp = intcode_computer(program)
    scan_beam(program)