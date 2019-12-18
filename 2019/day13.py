from intcode_computer import intcode_computer

def count_blocks(input_string):
  return input_string[2::3].count(2)

def find_tile(screen, tile_id):
  for i in range(int(len(screen) / 3)):
    if screen[3*i+2] == tile_id:
      return (screen[3*i],screen[3*i+1])
  return None

def play(comp):
  paddle = find_tile(comp.execute().output_values, 3)[0]
  while comp.halted == False:
    ball = find_tile(comp.output_values, 4)
    action = 0
    if paddle < ball[0]: action = 1
    if paddle > ball[0]: action = -1
    paddle += action
    comp.input(action).clear().execute()
  return comp.output()

if __name__ == "__main__":
  with open('./input/day13') as f:
    program = [int(i) for i in next(f).split(',')]
    print(count_blocks(intcode_computer(program).execute().output_values))
    program[0] = 2
    print(play(intcode_computer(program)))