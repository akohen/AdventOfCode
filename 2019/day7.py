from intcode_computer import intcode_computer
import itertools

def find_max(program, phase):
  phases = list(itertools.permutations(phase))
  max_phase = 0
  for phase in phases:
    max_phase = max(max_phase, get_thruster_value(program, phase))
  return max_phase

def get_thruster_value(prg, phase):
  current = 0
  amps = [intcode_computer(program, [phase[i]], stop_on_output=True) for i in range(5)]
  amps[0].input_values.append(0)
  while(amps[current].halted is not True):
    amps[current].execute()
    if(len(amps[current].output_values)):
      out = amps[current].output_values.pop()
    else:
      return out
    current = (current + 1) % 5
    amps[current].input_values.append(out)

if __name__ == "__main__":
  with open('./input/day7') as f:
    program = [int(i) for i in next(f).split(',')]
    print('Step 1 : {}'.format(find_max(program, [0, 1, 2, 3, 4])))
    print('Step 2 : {}'.format(find_max(program, [5, 6, 7, 8, 9])))