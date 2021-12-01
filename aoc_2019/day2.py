import math 

def process_intcode(program):
  pointer = 0
  while pointer < len(program):
    if program[pointer] == 1:
      program[program[pointer+3]] = program[program[pointer+1]] + program[program[pointer+2]]
    elif program[pointer] == 2:
      program[program[pointer+3]] = program[program[pointer+1]] * program[program[pointer+2]]
    else:
      return program
    pointer += 4

def find_verb(program_org):
  for i in range(0,100):
      for j in range(0,100):
        program = list(program_org)
        program[1] = i
        program[2] = j
        if process_intcode(program)[0] == 19690720:
          return (i,j)

if __name__ == "__main__":
  for line in open('./input/day2'):
    program = [int(i) for i in line.split(',')]
    print(find_verb(program))