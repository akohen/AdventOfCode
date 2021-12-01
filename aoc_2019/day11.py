from intcode_computer import intcode_computer

def paint(computer):
  position = (0,0)
  direction = 0
  # 0 = UP, 1 = LEFT, 2 = DOWN, 3 = RIGHT
  action = { 0: lambda x : (x[0],x[1]+1), 1: lambda x : (x[0]-1,x[1]), 2: lambda x : (x[0],x[1]-1), 3: lambda x : (x[0]+1,x[1]) }
  seen = {}
  while computer.execute().halted == False:
    seen[position] = computer.output_values.pop()

    rotation = computer.execute().output_values.pop()
    direction = (direction - 2 * rotation + 1) % 4

    position = action[direction](position)
    computer.input_values.append(seen.get(position, 0))
  return seen

def display_code(paint):
  for y in range(7):
    print(''.join(['.' if paint.get((x,-y), 0) == 1 else ' ' for x in range(40)]))

if __name__ == "__main__":
  with open('./input/day11') as f:
    program = [int(i) for i in next(f).split(',')]
    print('Phase 1: {}'.format(len(paint(intcode_computer(program, [0], stop_on_output=True)))))
    display_code(paint(intcode_computer(program, [1], stop_on_output=True)))